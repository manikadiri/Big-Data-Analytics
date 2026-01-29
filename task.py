from pyspark.sql import SparkSession
from pyspark.sql.functions import avg, count

spark = SparkSession.builder.appName("Diabetes Big Data Analysis").getOrCreate()

df = spark.read.csv(r"D:\diabetes.csv", header=True, inferSchema=True)

print("Dataset Preview:")
df.show(10)

print("Schema:")
df.printSchema()

avg_glucose = df.groupBy("Outcome").agg(avg("Glucose").alias("Average_Glucose"))
print("Average Glucose Level by Outcome:")
avg_glucose.show()

avg_bmi = df.groupBy("Outcome").agg(avg("BMI").alias("Average_BMI"))
print("Average BMI by Outcome:")
avg_bmi.show()

patient_count = df.groupBy("Outcome").agg(count("*").alias("Patient_Count"))
print("Patient Count by Outcome:")
patient_count.show()

spark.stop()
