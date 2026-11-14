
import streamlit as st

st.title("Investment Calculator")

investment = st.number_input("Initial investment (€)", value=1000.0)
return_rate = st.number_input("Annual return (%)", value=7.0)
years = st.number_input("Number of years", value=10, min_value=1)

final_value = investment * (1 + return_rate / 100) ** years

st.write(f"Final investment value: €{final_value:.2f}")

year_list = list(range(0, years + 1))
value_list = []

for year in year_list:
    value = investment * (1 + return_rate / 100) ** year
    value_list.append(value)

st.line_chart(value_list, x_label="Year", y_label="Investment value (€)")