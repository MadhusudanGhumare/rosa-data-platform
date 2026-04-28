# 🚀 ROSA Data Platform

This project demonstrates a simple **data pipeline architecture** using **PySpark**, following the **Bronze → Silver → Gold** pattern.

---

## 🧱 Architecture

* **Bronze Layer** → Raw data ingestion (CSV → Parquet)
* **Silver Layer** → Cleaned data (filter completed orders)
* **Gold Layer** → Aggregated data (city-wise revenue)

---

## 📁 Project Structure

```
rosa-data-platform/
  data/
    orders.csv
    bronze_orders/
    silver_orders/
    gold_orders/
  rosa_pipeline.py
  requirements.txt
  README.md
```

---

## ⚙️ How to Run

```bash
pip install -r requirements.txt
python3 rosa_pipeline.py
```

---

## 📊 Output

* **Bronze Layer** → Stores raw data in Parquet format
* **Silver Layer** → Filters only completed orders
* **Gold Layer** → Aggregates total revenue by city

---

## 🧰 Tech Stack

* Python 3
* PySpark
* Parquet

---

