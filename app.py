import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("📊 Data Explorer App")

# Upload CSV
uploaded_file = st.file_uploader("Upload your CSV file", type=["csv"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)

    st.write("### Dataset Preview")
    st.write(df.head())

    # 🔥 Dataset Info
    st.write("### 📌 Dataset Info")
    st.write(df.describe())

    # 🔥 Optional Full Stats
    if st.checkbox("Show Full Statistics"):
        st.write("### 📊 Full Dataset Statistics")
        st.write(df.describe())

    # Select numeric columns
    numeric_columns = df.select_dtypes(include=['int64', 'float64']).columns

    if len(numeric_columns) > 0:
        column = st.selectbox("Select a numeric column", numeric_columns)

        if column:
            data = df[column]

            st.write("### 📈 Statistics")

            mean = data.mean()
            median = data.median()
            std = data.std()
            min_val = data.min()
            max_val = data.max()

            st.write(f"Mean: {mean}")
            st.write(f"Median: {median}")
            st.write(f"Standard Deviation: {std}")
            st.write(f"Min: {min_val}")
            st.write(f"Max: {max_val}")

            # Histogram
            st.write("### 📊 Histogram")

            fig, ax = plt.subplots()
            sns.histplot(data, kde=True, ax=ax)
            st.pyplot(fig)

            # 🔥 Download Report Feature
            report = f"""
Data Explorer Report

Column: {column}

Mean: {mean}
Median: {median}
Standard Deviation: {std}
Min: {min_val}
Max: {max_val}
"""

            st.download_button(
                label="📥 Download Report",
                data=report,
                file_name="data_report.txt",
                mime="text/plain"
            )

            # Insights box
            st.write("### 🧠 Write Your Insights")
            insights = st.text_area("What do you observe from this data?")

    else:
        st.warning("No numeric columns found in dataset.")