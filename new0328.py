import streamlit as st
import numpy as np
import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt
import seaborn as sns

# Set page config
apptitle = 'DSSI New App'

st.set_page_config(page_title=apptitle, layout='wide')

st.title('My First Streamlit Application')
st.write('Reference: https://docs.streamlit.io/en/stable/api.html#display-data')
st.balloons()

# Load diabetes dataset
st.subheader('**Iris Flower Data**')
db = datasets.load_iris()

df = pd.DataFrame(db.data, columns=db.feature_names)

col1, col2 = st.columns([2,1])
with col1:
    st.dataframe(df, use_container_width=True)
with col2:
    fig, ax = plt.subplots(figsize=(6, 3))
    if 1==1:
        column_to_plot = db.feature_names[0]
        df[column_to_plot].hist(bins = 10, ax=ax)
        fig.suptitle(f"{column_to_plot} Distribution")
        st.pyplot(fig)
