import streamlit as st
from extractor.extractor import extract_entities
from extractor.parser import format_data
from utils.pdf_generator import render_template, convert_to_pdf

st.set_page_config(page_title="Auto Resume Builder", layout="centered")

st.markdown("""
    <style>
        body {
            background-color: #f9f5e9;
            font-family: "Times New Roman", serif;
        }
        .reportview-container .main {
            background-color: #f9f5e9;
        }
        .block-container {
            padding: 2rem 2rem;
            font-family: "Times New Roman", serif;
        }
        h1, h2, h3, h4 {
            font-family: "Times New Roman", serif;
        }
        .stButton>button {
            font-family: "Times New Roman", serif;
        }
    </style>
""", unsafe_allow_html=True)

st.title("Auto Resume Builder")
st.write("Generate a resume by pasting your info below:")

raw_text = st.text_area("Enter raw resume details here:", height=250)

template_choice = st.selectbox("Choose Resume Style", ["modern", "classic", "minimal"])

if st.button("Generate Resume"):

    if not raw_text.strip():
        st.warning("Please paste some text first.")
    else:
        with st.spinner("Extracting and formatting..."):
            entities = extract_entities(raw_text)
            data = format_data(entities)

            

            html = render_template(data, template_choice)
            

            pdf_path = convert_to_pdf(html)

        with open(pdf_path, "rb") as f:
            st.success("Resume generated successfully!")
            st.download_button(
                label="Download Resume",
                data=f,
                file_name="resume.pdf",
                mime="application/pdf"
            )
