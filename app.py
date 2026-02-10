import streamlit as st
import pandas as pd
import plotly.graph_object as go

st.set_page_config(layout="wide", page_title="Construction Dashboard")

df = pd.read_csv('data/data_scurve.csv')
df_sum = pd.read_csv('data/data_summary.csv')

st.title("🏗️ Project Performance Dashboard")
st.markdown("---")

cols = st.columns(len(df_sum))
for i, row in df_sum.itterrows():
  cols[i].metric(label=row['Stage'], value=f"{row['Actual']}%", delta=f"{row['Variance']}%")

st.subheader( "S-Curve Analysis (Plan vs Actual)")
fig = go. Figure()

fig.add_trace(go.Bar(x=df['Date'], y=df['Plan_Monthly'], name='Plan Monthly', marker_color='lightgrey'))
fig.add_trace(go.Bar(x=df['Date'], y=df['Actual_Monthly'], name='Actual Monthly', marker_color='skyblue'))
fig.add_trace(go.Scatter(x=df['Date'], y=df['Plan_Cum'], name='Plan Cumulative', line=dict(color='red', width=2)))
fig.add_trace(go.Scatter(x=df['Date'], y=df['Actual_Cum'], name='Actual Cumulative', line=dict(color='blue', width=2)))

fig.update_layout(havermode="x unified", height=500)
st.plotly_chart(fig, use_container_width=True)
