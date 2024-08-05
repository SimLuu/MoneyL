import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title('Money Laundering Dashboard')
st.sidebar.header('/content/drive/MyDrive/data/HI-Small_Trans.csv')
uploaded_file = st.sidebar.file_uploader('/content/drive/MyDrive/data/HI-Small_Trans.csv', type="csv")

if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
st.write('### Data', data)
st.write('### Summary', data.describe())

st.write('### Bar Plot')
    if st.sidebar.checkbox('Show bar plot'):
        column = st.sidebar.selectbox('Choose column for bar plot', data.columns)
        fig, ax = plt.subplots()
        data[column].value_counts().plot(kind='bar', ax=ax)
        st.pyplot(fig)

st.write('### Line Plot')
    if st.sidebar.checkbox('Show line plot'):
        column = st.sidebar.selectbox('Choose column for line plot', data.columns)
        fig, ax = plt.subplots()
        data[column].plot(kind='line', ax=ax)
        st.pyplot(fig)

st.write('### Correlation Heatmap')
    if st.sidebar.checkbox('Show correlation heatmap'):
        fig, ax = plt.subplots()
        sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
        st.pyplot(fig)
else:
    st.write('Please upload a CSV file to visualize the data.')

git add app.py
git commit -m "Add Streamlit app"
git push origin main
