from pyspark.sql import SparkSession
from pyspark.sql.functions import col

# --------------------------
# Create Spark Session
# --------------------------
spark = SparkSession.builder \
    .appName("ROSA Data Pipeline") \
    .getOrCreate()

# --------------------------
# BRONZE LAYER (Raw Data)
# --------------------------
bronze_df = spark.read.csv("data/orders.csv", header=True, inferSchema=True)

bronze_df.write.format("parquet") \
    .mode("overwrite") \
    .save("data/bronze_orders")

print("✅ Bronze layer created")

# --------------------------
# SILVER LAYER (Cleaned)
# --------------------------
silver_df = bronze_df.filter(col("status") == "COMPLETED")

silver_df.write.format("parquet") \
    .mode("overwrite") \
    .save("data/silver_orders")

print("✅ Silver layer created")

# --------------------------
# GOLD LAYER (Aggregated)
# --------------------------
gold_df = silver_df.groupBy("city").sum("amount")

gold_df.write.format("parquet") \
    .mode("overwrite") \
    .save("data/gold_orders")

print("✅ Gold layer created")
