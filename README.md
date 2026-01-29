# Diabetes Big Data Analysis using PySpark

📌 Project Overview

This project performs **big data analysis on a diabetes dataset** using **Apache Spark (PySpark)**.
The goal is to analyze health indicators such as **Glucose** and **BMI** and compare them based on diabetes **Outcome** (diabetic vs non-diabetic).

The script demonstrates how Spark can efficiently process and analyze large datasets using distributed computing.

---

#🛠️ Technologies Used

* **Python**
* **Apache Spark (PySpark)**
* **Spark SQL & DataFrame API**

---

## 📂 Dataset Description

* **File name:** `diabetes.csv`
* **Source:** Local system
* **Format:** CSV
* **Key Columns Used:**

  * `Glucose` – Blood glucose level
  * `BMI` – Body Mass Index
  * `Outcome` –

    * `0` → Non-diabetic
    * `1` → Diabetic

---

## ⚙️ How the Code Works

### 1️⃣ Create Spark Session

```python
SparkSession.builder.appName("Diabetes Big Data Analysis").getOrCreate()
```

Initializes a Spark application named **Diabetes Big Data Analysis**.

---

### 2️⃣ Load the Dataset

```python
spark.read.csv(..., header=True, inferSchema=True)
```

* Reads the CSV file
* Automatically detects data types
* Uses column headers

---

### 3️⃣ Preview Data

```python
df.show(10)
```

Displays the first 10 rows of the dataset for quick inspection.

---

### 4️⃣ Display Schema

```python
df.printSchema()
```

Shows column names and data types to understand the structure of the dataset.

---

### 5️⃣ Average Glucose Analysis

```python
groupBy("Outcome").agg(avg("Glucose"))
```

Calculates the **average glucose level** for:

* Diabetic patients
* Non-diabetic patients

---

### 6️⃣ Average BMI Analysis

```python
groupBy("Outcome").agg(avg("BMI"))
```

Computes the **average BMI** based on diabetes outcome.

---

### 7️⃣ Patient Count Analysis

```python
groupBy("Outcome").agg(count("*"))
```

Counts the number of patients in each outcome category.

---

### 8️⃣ Stop Spark Session

```python
spark.stop()
```

Gracefully shuts down the Spark application.

---

## 📊 Output Generated

The program prints:

* Dataset preview (first 10 rows)
* Dataset schema
* Average glucose level by outcome
* Average BMI by outcome
* Total patient count by outcome

All results are displayed directly in the console.

---

## ▶️ How to Run the Project

### Prerequisites

* Python installed
* Apache Spark installed
* PySpark configured properly
* Dataset available at the specified path

### Run Command

```bash
python task.py
```

---

##  Use Case

* Big data healthcare analysis
* Diabetes research insights
* Learning PySpark DataFrame operations
* Academic and mini-project purposes



