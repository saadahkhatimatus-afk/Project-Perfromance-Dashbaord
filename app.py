import pandas as pd
import plotly.express as px
from dash import Dash, dcc, html
import dash_bootstrap_components as dbc

# Load datasets
df_scurve = pd.read_csv("data/data_scurve.csv")
df_summary = pd.read_csv("data/data_summary.csv")

# === KPI Calculation ===
total_pv = df_summary["Planned_Value"].sum()
total_ev = df_summary["Earned_Value"].sum()
total_ac = df_summary["Actual_Cost"].sum()

spi = total_ev / total_pv
cpi = total_ev / total_ac

# === S-Curve Figure ===
fig_scurve = px.line(
    df_scurve,
    x="Date",
    y=["Planned_Value", "Earned_Value", "Actual_Cost"],
    title="Project S-Curve Performance"
)

# === App ===
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

app.layout = dbc.Container([

    html.H1("Construction Project Performance Intelligence Dashboard",
            className="text-center my-4"),

    dbc.Row([
        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("Schedule Performance Index (SPI)"),
            html.H2(f"{spi:.2f}")
        ])), width=6),

        dbc.Col(dbc.Card(dbc.CardBody([
            html.H5("Cost Performance Index (CPI)"),
            html.H2(f"{cpi:.2f}")
        ])), width=6),
    ], className="mb-4"),

    dbc.Row([
        dbc.Col(dcc.Graph(figure=fig_scurve), width=12)
    ]),

], fluid=True)

if __name__ == "__main__":
    app.run_server(debug=True)
