# Biscuit Sales & Profitability Analysis (Python)

## 📌 Project Overview
This project analyzes a **2024 retail biscuit transaction dataset** to understand revenue and profit drivers across **products, customer locations, payment methods, age groups, and sales representatives**.  
It demonstrates end‑to‑end analytics: data cleaning, KPI calculation, and visualization.

## 🗂️ Dataset
- Source file (provided): `ZEPH ANALYSIS.xlsx`
- Cleaned CSV used in this repo: `data/biscuit_sales_2024.csv` (12,000 transactions)

Key fields include: transaction date, buyer demographics, product code/brand, quantity, revenue, cost, profit, and payment method.

## 🎯 KPIs (from this dataset)
- **Total orders:** 12,000
- **Total units sold:** 3,050,309
- **Total revenue:** 61,567,883
- **Total profit:** 26,784,833
- **Overall profit margin:** 43.5%

Highlights:
- **Top brand by revenue:** Shortbread (13,973,760)
- **Top location by revenue:** San Antonio (7,343,282)
- **Top sales rep by revenue:** Travis Doyle (10,880,651)
- **Best month:** 2024-01 (7,878,885)

## 📈 Visual Outputs
Sample charts are included:
- `monthly_revenue.png`
- `top_brands_revenue.png`
- `top_locations_revenue.png`
- `revenue_by_payment.png`
- `revenue_by_sales_rep.png`
- `profit_margin_by_brand.png`

## 🛠️ Tools Used
- Python
- Pandas
- Matplotlib

## ▶️ How to Run
```bash
pip install -r requirements.txt
python biscuit_sales_analysis.py
```

The script will:
- load `data/biscuit_sales_2024.csv`
- compute KPIs
- save charts to the project folder

## ✅ What This Shows
- Data preparation and validation
- KPI building (revenue, profit, margin)
- Group-by analysis (product, location, sales reps, demographics)
- Communicating insights through visuals
