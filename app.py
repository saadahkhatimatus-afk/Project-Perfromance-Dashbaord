import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# =====================================================
# 1. LOAD DATA
# =====================================================

df_scurve = pd.read_csv("data/data_scurve.csv")
df_summary = pd.read_csv("data/data_summary.csv")

# =====================================================
# 2. DATA CLEANING
# =====================================================

# Convert numeric columns safely
numeric_cols = ["Planned_Value", "Earned_Value", "Actual_Cost"]

df_summary[numeric_cols] = df_summary[numeric_cols].apply(
    pd.to_numeric, errors="coerce"
)

df_summary = df_summary.dropna()

# Convert Date column to datetime and sort
df_scurve["Date"] = pd.to_datetime(df_scurve["Date"], errors="coerce")
df_scurve = df_scurve.sort_values("Date")

# =====================================================
# 3. FEATURE ENGINEERING (EVM CALCULATION)
# =====================================================

# Variance Calculations
df_summary["Cost_Variance"] = (
    df_summary["Earned_Value"] - df_summary["Actual_Cost"]
)

df_summary["Schedule_Variance"] = (
    df_summary["Earned_Value"] - df_summary["Planned_Value"]
)

# Aggregate Totals
total_pv = df_summary["Planned_Value"].sum()
total_ev = df_summary["Earned_Value"].sum()
total_ac = df_summary["Actual_Cost"].sum()

# Defensive Division
spi = total_ev / total_pv if total_pv != 0 else 0
cpi = total_ev / total_ac if total_ac != 0 else 0

# =====================================================
# 4. PERFORMANCE CLASSIFICATION
# =====================================================

def classify_index(value):
    if value >= 1:
        return "On Track"
    elif value >= 0.9:
        return "Warning"
    else:
        return "Critical"

spi_status = classify_index(spi)
cpi_status = classify_index(cpi)

# =====================================================
# 5. VISUALIZATION
# =====================================================

fig_scurve = px.line(
    df_scurve,
    x="Date",
    y=["Planned_Value", "Earned_Value", "Actual_Cost"],
    title="Project S-Curve Performance",
    markers=True
)

fig_scurve.update_layout(
    xaxis_title="Date",
    yaxis_title="Value",
    legend_title="Metrics"
)

# =====================================================
# 6. DASH APP LAYOUT
# =====================================================

app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([

    html.H1(
        "Construction Project Performance Intelligence Dashboard",
        className="text-center my-4"
    ),
    dbc.Row([

        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("Schedule Performance Index (SPI)"),
            html.H2(f"{spi:.2f}"),
            html.P(f"Status: {spi_status}")
        ])), width=6),

        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("Cost Performance Index (CPI)"),
            html.H2(f"{cpi:.2f}"),
            html.P(f"Status: {cpi_status}")
        ])), width=6),
    ], className="mb-4"),
    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_scurve), width=12)
    ])

], fluid=True)

# =====================================================
# 7. RUN SERVER
# =====================================================

if __name__ == "__main__":
    app.run_server(debug=True)
