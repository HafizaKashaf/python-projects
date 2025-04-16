import streamlit as st  # UI
import pandas as pd     # Data handling
from io import BytesIO  # For temporary file storage

# Page setup
st.set_page_config(page_title="📄 File Converter & Cleaner", layout="wide")

# Title and description
st.title("📄 File Converter & Cleaner")
st.write("Upload your CSV or Excel file and convert it to the desired format. You can also clean the data by removing duplicates and missing values 🚀.")

# File uploader
uploaded_files = st.file_uploader("Upload your CSV or Excel file", type=["csv", "xlsx"], accept_multiple_files=True)

if uploaded_files:
    for file in uploaded_files:
        ext = file.name.split(".")[-1]
        df = pd.read_csv(file) if ext == "csv" else pd.read_excel(file)

        st.subheader(f"🔎 Data Preview of {file.name}")
        st.dataframe(df.head())

        # Fill missing values
        if st.checkbox(f"🧩 Fill Missing Values - {file.name}"):
            df.fillna(df.select_dtypes(include=["number"]).mean(), inplace=True)
            st.success("✅ Missing values filled successfully!")
            st.dataframe(df.head())

        # Select columns to keep
        selected_columns = st.multiselect(
            f"🧮 Select columns to keep - {file.name}",
            df.columns.tolist(),
            default=df.columns.tolist()
        )
        df = df[selected_columns]
        st.dataframe(df.head())

        # Show chart
        if st.checkbox(f"📊 Show Chart - {file.name}") and not df.select_dtypes(include="number").empty:
            st.bar_chart(df.select_dtypes(include="number").iloc[:, :2])

        # Choose output format
        format_choice = st.radio(f"🔀 Convert {file.name} to:", ["CSV", "Excel"], key=f"format_{file.name}")

        # Create download button
        if st.button(f"⬇ Download {file.name} as {format_choice}", key=f"download_{file.name}"):
            output = BytesIO()
            if format_choice == "CSV":
                df.to_csv(output, index=False)
                mimetype = "text/csv"
                new_file_name = file.name.replace(ext, "csv")
            else:
                df.to_excel(output, index=False)
                mimetype = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
                new_file_name = file.name.replace(ext, "xlsx")

            output.seek(0)

            # Display download button
            st.download_button(
                label="📂 Click here to download",
                data=output,
                file_name=new_file_name,
                mime=mimetype,
                key=f"download_button_{file.name}"
                )

            # 🎉 Success message
            st.success("✅ File is ready! Click the button above to download 🎉")
            st.balloons()
