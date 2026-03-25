import streamlit as st
import re

def extract_names(text):
    # Simple regex to find names (this is just a placeholder and can be improved)
    return re.findall(r'\b[A-Z][a-z]+ [A-Z][a-z]+\b', text)

st.title("Name Extraction App")

st.write("Enter text to extract names:")
input_text = st.text_area("Input Text")

if st.button("Extract Names"):
    if input_text:
        names = extract_names(input_text)
        if names:
            st.success("Extracted Names:")
            st.write(", ".join(names))
        else:
            st.warning("No names found.")
    else:
        st.error("Please enter some text.")