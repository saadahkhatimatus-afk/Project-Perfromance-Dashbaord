# Construction Project Performance Dashboard

An interactive dashboard built using Python, Dash, and Plotly to monitor construction project performance through weighted stage tracking and S-Curve analysis.

---

## 📌 Project Objective

This project aims to monitor and analyze construction project performance by comparing Planned vs Actual progress across multiple project stages.

The dashboard provides visibility into:

- Monthly performance deviation
- Cumulative progress tracking
- Weighted stage contribution
- Overall project health classification

---

## 📊 Dataset Description

### 1. data_curve.csv

This dataset tracks monthly S-Curve progress.

Columns:

- Calendar Year → Project year
- Calendar Month → Month name
- Project Month → Sequential project timeline
- Plan Monthly Progress (%) → Planned progress for the month
- Plan Cumulative Progress (%) → Planned cumulative progress
- Actual Monthly Progress (%) → Actual monthly progress
- Actual Cumulative Progress (%) → Actual cumulative progress
- Deviation (%) → Difference between Actual and Planned cumulative progress

---

### 2. data_summary.csv

Stage-based weighted performance tracking.

Columns:

- Stage → Engineering, Procurement, Construction, Commissioning
- W/F (%) → Weight Factor of each stage in total project
- Plan (Previous Month)
- Actual (Previous Month)
- Monthly Variance
- Plan (Cumulative)
- Actual (Cumulative)
- Cumulative Variance
- Status → Performance classification (On-Track, Minor Deviation, Critical)

---

## 📐 Performance Metrics Logic

### Monthly Variance
Monthly Variance = Actual (This Month) - Planned (This Month)

### Cumulative Variance
Cumulative Variance = Actual (Cumulative) - Planned (Cumulative)

### Weighted Overall Progress
Overall Progress = Σ(Stage Progress × Weight Factor)

### Status Classification
- On-Track → Variance within acceptable threshold
- Minor Deviation → Small negative variance
- Critical → Significant negative variance

---

## 🚀 Dashboard Features

- Executive KPI Summary
- S-Curve Visualization (Planned vs Actual)
- Stage-Level Performance Breakdown
- Variance Monitoring
- Performance Status Classification

---

## 🛠 Installation

1. Clone repository

git clone https://github.com/your-username/Project-Performance-Dashboard.git

2. Install dependencies

pip install -r requirements.txt

3. Run the application

python app.py

---

## 🎯 Business Impact

This dashboard helps project managers:

- Detect schedule deviation early
- Monitor stage-level contribution
- Improve decision-making
- Reduce risk of schedule overrun

---

## 🔮 Future Improvements

- Earned Value Management (CPI & SPI)
- Forecasting completion date
- Delay prediction model
- Integration with live database
