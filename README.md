# Supply Chain Control Tower (SCCT)

## 📌 Overview
The Supply Chain Control Tower (SCCT) is a data analytics project that provides visibility into core supply chain operations. It uses a rule-based synthetic dataset to analyze performance and calculate key supply chain KPIs — on-time delivery rate, fill rate, average lead time, and per-supplier/per-warehouse breakdowns.

This project is being built as a learning journey by an Industrial Engineering student to apply supply chain concepts through hands-on data analysis, programming, and dashboard development.

## 🚧 Project Status
In progress — **Phase 2 — SQL Database:Design and populate a relational database, connect Python to SQL**

## 🗺️ Roadmap
- **Phase 1 — Python Basics:** Read and clean data, calculate KPIs, build simple visualizations, generate realistic simulated data ✅
- **Phase 2 — SQL Database:** Design and populate a relational database, connect Python to SQL
- **Phase 3 — Power BI Dashboard:** Build an interactive executive dashboard
- **Phase 4 — Advanced Features (stretch goals):** Demand forecasting, delay prediction, inventory alerts

## 🛠️ Tech Stack
- **Python** — data processing and KPI calculations (pandas, matplotlib)
- **SQL** — relational database for structured storage (Phase 2)
- **Power BI** — interactive dashboards and visual reporting (Phase 3)

## 📁 Repository Structure
SCCT/
├── data/ # Generated supply chain datasets (CSV, gitignored)
├── notebooks/
│ └── archive/ # Early exploratory analysis, superseded by src/kpis/
├── src/
│ ├── main.py # Pipeline orchestration
│ ├── data_loader.py # CSV loading with validation
│ ├── data_cleaning.py # Date parsing, delay-day calculation
│ ├── data_generator.py # Rule-based synthetic data generator
│ ├── visualizations.py # Chart functions
│ └── kpis/
│ ├── orders.py # On-time rate, fill rate, average lead time, delivered-late count
│ ├── supplier.py # Per-supplier reliability & fill rate
│ └── warehouse.py # Per-warehouse on-time rate
├── .gitignore
└── README.md

## 📊 KPIs

**Orders**
- On-time delivery rate ✅
- Fill rate ✅
- Delivered late count ✅
- Average lead time ✅ 

**Supplier**
- Supplier reliability — observed on-time rate per supplier ✅
- Supplier fill rate ✅

**Warehouse**
- Warehouse on-time rate ✅

**Deferred to Phase 2/3**
- Inventory turnover — needs stock-level and cost data the current order-level schema doesn't have. Will require an `inventory_snapshots` table once the SQL layer exists.

## Realistic Data Generator
`src/data_generator.py` builds a synthetic but rule-driven supply chain:
- **13 suppliers** and **3 warehouses**, each with an independent reliability/congestion score
- **20 products** and **25 customers**, drawn from fixed pools to allow realistic repeat orders
- **500 simulated orders**, with outcomes (pending, cancelled, delayed, delivered) driven by a weighted risk model: 50% supplier reliability, 30% warehouse congestion, 20% destination risk — not pure randomness
- Delay severity and quantity shortfalls modeled as independent phenomena, matching how real operational disruptions tend to behave

## 👤 Author
Mariam Deeb — Industrial Engineering student, building this project to develop practical skills in Python, SQL, and Power BI applied to supply chain analytics.