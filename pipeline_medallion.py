from pyspark.sql import SparkSession
from pyspark.sql.functions import unix_timestamp, trim, col, when

def main():
    spark = SparkSession.builder.appName("TransportMedallion").getOrCreate()

    # Load Bronze Layer (raw data)
    bronze_df = spark.read.option("header", True).csv("/data/dfTransjakarta180kRows.csv")

    bronze_df.write.mode("overwrite").parquet("/bronze/transport")

    silver_df = bronze_df \
        .withColumn("tapInTime", trim(col("tapInTime"))) \
        .withColumn("tapOutTime", trim(col("tapOutTime"))) \
        .filter(col("tapInTime").isNotNull() & col("tapOutTime").isNotNull()) \
        .withColumn("tapInTS", unix_timestamp("tapInTime", "yyyy-MM-dd HH:mm:ss")) \
        .withColumn("tapOutTS", unix_timestamp("tapOutTime", "yyyy-MM-dd HH:mm:ss")) \
        .withColumn("tapInTS_valid", when(col("tapInTS").isNotNull(), 1).otherwise(0)) \
        .withColumn("tapOutTS_valid", when(col("tapOutTS").isNotNull(), 1).otherwise(0))

    invalid_rows = silver_df.filter((col("tapInTS_valid") == 0) | (col("tapOutTS_valid") == 0)).count()
    print(f"Jumlah baris dengan timestamp parsing gagal: {invalid_rows}")

    silver_df_valid = silver_df.filter((col("tapInTS_valid") == 1) & (col("tapOutTS_valid") == 1))

    silver_df_final = silver_df_valid.filter(col("tapOutTS") >= col("tapInTS")) \
        .withColumn("durationMinutes", (col("tapOutTS") - col("tapInTS")) / 60)

    silver_df_final.write.mode("overwrite").parquet("/silver/transport_clean")

    gold_df = silver_df_final.groupBy("corridorID", "corridorName") \
        .avg("durationMinutes") \
        .withColumnRenamed("avg(durationMinutes)", "avgDurationMinutes")

    gold_df.write.mode("overwrite").parquet("/gold/transport_summary")

    spark.stop()

if __name__ == "__main__":
    main()
