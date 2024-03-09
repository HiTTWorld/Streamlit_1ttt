import pandas as pd
import streamlit as st


st.set_page_config(page_title="Streamlit_TEST")
st.title('사탕사탕')

st.write("우리 다같이 언제보냐 파일이나 올려봐라 ㅋㅋㅋ")

# Title of the app
st.title('Excel/CSV File Data Viewer')

# File uploader widget
uploaded_file = st.file_uploader("Choose an Excel or CSV file", type=['csv', 'xlsx'])

if uploaded_file is not None:
    try:
        if uploaded_file.type == "text/csv":
            # For CSV files
            df = pd.read_csv(uploaded_file)
        elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet":
            # For Excel files
            df = pd.read_excel(uploaded_file)

        # Display the first 5 rows of the DataFrame
        st.dataframe(df.head())

    except Exception as e:
        st.error(f"Error: {e}")
else:
    st.info('Upload a file to display the data')

