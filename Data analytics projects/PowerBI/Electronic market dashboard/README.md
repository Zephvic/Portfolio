# Capstone Electronics Market Revenue Dashboard — Power BI

![Electronics Market Revenue Dashboard](electronic%20market%20dashboard.png)

## Table of Contents

- [Description](#description)
- [Objectives](#objectives)
- [Tools and Technologies](#tools-and-technologies)
- [Dataset](#dataset)
- [Process](#process)
- [Key Performance Indicators](#key-performance-indicators)
- [Findings](#findings)
- [Recommendations](#recommendations)
- [Conclusion](#conclusion)
- [Contact Me](#contact-me)

## Description

This project builds an interactive Power BI dashboard for an electronics firm operating across Asia, the U.K., and the U.S.A. It analyzes revenue performance across sales representatives, product categories, and regions, and breaks it down further by quarter and customer demographics to support data-driven decisions.

## Objectives

The analysis set out to answer a few core business questions:

- Which products and sales reps generate the most revenue?
- Are there age or gender differences in sales performance?
- Which regions perform best, and which lag behind?
- How does revenue move across quarters and months?

## Tools and Technologies

- Power BI for visualization
- Excel for the source dataset
- Power Query for cleaning and transformation
- DAX for custom measures

## Dataset

The dataset covers 3,264 electronics sales transactions across Asia, the U.K., and the U.S.A. Key fields include sales rep details (name, gender, age, rank level), product category, region, and revenue by year, quarter, and month.

- [View dataset](data/Electronic%20Market%20dataset.xlsx)

## Process

**Cleaning and transformation**
Merged first and last name into a single full name field, standardized date, quarter, and month formatting, and converted revenue into a consistent numeric type. Added a few derived columns, including age group and revenue per sale.

**Data modeling**
Built relationships between the sales, product, and region tables using rep ID, product ID, and store ID as keys.

**Analysis**
Looked at revenue by region, by quarter and month, by product category, by age group and gender, and by sales rep rank level.

**Dashboard development**
Put together KPI cards for the headline numbers, bar charts for revenue by region and rank level, a treemap for revenue by product category, a line chart for the monthly trend, a column chart for revenue by quarter, and slicers to filter by product type.

## Key Performance Indicators

| KPI | Value |
|---|---|
| Total Revenue | $127M |
| Total Transactions | 3,264 |
| Total Products | 4 |
| Average Age | 34.24 |

## Findings

Asia is the clear top-performing region, bringing in $78.7M, while the U.S.A. generates the least at $16.6M — the U.K. sits in between at $32.1M.

Smartphones dominate product sales, accounting for about 62% of total revenue ($78.9M), well ahead of accessories ($21.1M), tablets ($14.2M), and laptops, the smallest category at $13.2M.

QTR 1 generated the highest revenue ($47.8M), with a steady decline through the rest of the year, bottoming out in QTR 3 at $17.3M.

A small group of reps — led by Andrew T. and Louis N. — bring in a disproportionate share of total revenue, and the A1 rank level alone accounts for nearly half of all revenue.

Male reps generated significantly more total revenue than female reps, and a higher average per sale too, which points to more than just a headcount difference.

## Recommendations

Invest further in the Asian market, since it's already the strongest performer, and look into what's holding the U.S.A. back before assuming it's just a smaller market.

Keep marketing and inventory focus on smartphones, but also dig into why laptops underperform relative to accessories and tablets, which are smaller categories but not by nearly as much.

Study what top reps like Andrew T. and Louis N. do differently, and see if it can be taught to the rest of the team.

Look into what drove the QTR 1 peak and whether any of it — a promotion, timing, pricing — can be repeated in QTR 3, the weakest quarter.

Look more closely at the gender gap in rep performance before drawing conclusions — it could be tenure, territory, or something else worth identifying.

## Conclusion

This project shows how raw sales data can be turned into a dashboard that actually tells you something — where the revenue is coming from, who's driving it, and where the business is leaving money on the table. It also reflects the kind of practical, business-first approach to data analysis I look to apply in real work.

## Contact Me

- [Email](mailto:zephvic@gmail.com)
- [LinkedIn](https://www.linkedin.com/in/victoryzeph)
- [GitHub](https://github.com/Zephvic)
