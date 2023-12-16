import pandas as pd
import streamlit as st
import plotly.express as px

st.set_page_config(layout="wide")

st.title("Main Dashboard Analysis")

# Lê os dados e realiza o tratamento uma vez
df = pd.read_excel("C:\\Users\\arthu\\Downloads\\Data.xlsx")

#1 - data (ano e mês)
df['month'] = df['expected_arrival_date'].dt.strftime('%m/%Y')

sorted_months = sorted(df['month'].unique())
# Barra lateral para filtros
selected_month = st.sidebar.selectbox('Select the month', sorted_months)

# Sidebar filters
with st.sidebar:
    selected_month = st.selectbox('Select the month', df['month'].unique())
    selected_centers = st.multiselect('Select the distribution center', df['distribution_center'].unique())
    selected_country = st.selectbox('Select the Country', df['country'].unique())
    selected_order_type = st.selectbox('Select the Order type', df['order_type'].unique())
    selected_product = st.selectbox('Select the product', df['product'].unique())

# Aplicar todos os filtros de uma vez
filtered_df = df[
    (df['month'] == selected_month) &
    (df['distribution_center'].isin(selected_centers)) &
    (df['country'] == selected_country) &
    (df['order_type'] == selected_order_type) &
    (df['product'] == selected_product)
]

# Gráficos
graph_1 = px.bar(df, x='month', y='currency_conversion_rate_to_eur', color='order_type')
st.plotly_chart(graph_1, use_container_width=True)

col1, col2 = st.columns(2)

graph_2 = px.bar(df, x='month', y='sku_category', orientation="h", color='distribution_center', title='Most popular SKU products in distribution centers')
col1.plotly_chart(graph_2, use_container_width=True)

graph_3 = px.line(filtered_df, x='month', y='item_quantity', title='Production per time. Use the sidebar filter')
col2.plotly_chart(graph_3, use_container_width=True)


