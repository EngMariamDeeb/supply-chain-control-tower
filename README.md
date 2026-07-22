# Supply Chain Control Tower (SCCT)

## 📌 Overview
The Supply Chain Control Tower (SCCT) is a data analytics project that provides visibility into core supply chain operations. It uses realistic simulated data to analyze performance and calculate key supply chain KPIs such as on-time delivery rate, fill rate, and inventory turnover.

This project is being built as a learning journey by an Industrial Engineering student to apply supply chain concepts through hands-on data analysis, programming, and dashboard development.

## 🚧 Project Status
In progress — **Phase 1: Python fundamentals applied to supply chain data**

Current focus: designing and building a realistic, rule-based data generator to replace the small sample dataset, so KPIs can be tested against a larger, more representative set of orders.

## 🗺️ Roadmap
- **Phase 1 — Python Basics:** Read and clean data, calculate KPIs, build simple visualizations, generate realistic simulated data
- **Phase 2 — SQL Database:** Design and populate a relational database, connect Python to SQL
- **Phase 3 — Power BI Dashboard:** Build an interactive executive dashboard
- **Phase 4 — Advanced Features (stretch goals):** Demand forecasting, delay prediction, inventory alerts

## 🛠️ Tech Stack
- **Python** — data processing and KPI calculations (pandas, matplotlib)
- **SQL** — relational database for structured storage
- **Power BI** — interactive dashboards and visual reporting

## 📁 Repository Structure
SCCT/
├── data/          # Sample/simulated supply chain datasets (CSV)
├── notebooks/     # Exploratory data analysis (Jupyter notebooks)
├── src/           # Python scripts for data loading, cleaning, KPI logic, and visualization
└── README.md      # Project documentation
## 📊 Planned KPIs
- On-time delivery rate ✅
- Fill rate ✅
- Currently delayed orders ✅
- Delivered late count ✅
- Inventory turnover (planned)
- Average lead time (planned)
- Supplier reliability score (planned)

## Key Results So Far
Using the sample supply chain dataset, the project currently calculates:
- **On-Time Delivery Rate:** 50.0%
- **Fill Rate:** 89.2%
- **Currently Delayed Orders:** 2
- **Delivered Late:** 3

These KPIs are calculated using **pandas**, with KPI logic organized in `src/kpis.py` and pipeline orchestration in `src/main.py`.

*Note: based on a small sample dataset (12 orders) created for early-stage learning purposes. See below for the in-progress data generator that will replace this.*

## 🧪 In Progress: Realistic Data Generator
To move beyond the small sample dataset, a rule-based synthetic data generator is being designed to simulate a more realistic supply chain, including:
- **13 suppliers** and **3 warehouses**, each with an independent reliability/congestion score
- **20 products** and **25 customers**, drawn from fixed pools to allow realistic repeat orders
- **500 simulated orders**, with outcomes (on-time, delayed, cancelled, pending) driven by a weighted risk model combining supplier reliability, warehouse congestion, and delivery destination — rather than pure random values
- Delay severity and quantity shortfalls modeled as separate, independently-driven phenomena, matching how real operational disruptions tend to behave

This generator is currently in the design phase; implementation is the next step.

## 👤 Author
Mariam Deeb — Industrial Engineering student, building this project to develop practical skills in Python, SQL, and Power BI applied to supply chain analytics.