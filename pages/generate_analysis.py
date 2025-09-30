import pandas as pd
import streamlit as st
from src.cloud_io import MongoIO
from src.constants import SESSION_PRODUCT_KEY
from src.utils import fetch_product_names_from_cloud
from src.data_report.generate_data_report import DashboardGenerator

mongo_con = MongoIO()


def create_analysis_page(review_data: pd.DataFrame):
    if review_data is not None:

        st.dataframe(review_data)
        if st.button("Generate Analysis"):
            dashboard = DashboardGenerator(review_data)

            # Display general information
            dashboard.display_general_info()

            # Display product-specific sections
            dashboard.display_product_sections()


try:

    if st.session_state.data:
        data = mongo_con.get_reviews(product_name=st.session_state[SESSION_PRODUCT_KEY])
        create_analysis_page(data)

    else:
        with st.sidebar:
            st.markdown("""
            No Data Available for analysis. Please Go to search page for analysis.
            """)
except AttributeError:
    product_name = None
    st.markdown(""" # No Data Available for analysis.""")

