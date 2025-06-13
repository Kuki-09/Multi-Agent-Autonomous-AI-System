import streamlit as st
from agents.classifier_agent import classify_input
from agents.json_agent import process_json
from agents.email_agent import process_email
from agents.pdf_agent import process_pdf
from memory.shared_memory import memory_store

st.title("Multi-Agent Autonomous AI System")

uploaded_file = st.file_uploader("Upload Email (txt), JSON, or PDF", type=["txt", "json", "pdf"])
memory_store.clear()

if uploaded_file is not None:
    file_bytes = uploaded_file.read()
    file_text = file_bytes.decode("utf-8", errors="ignore") if uploaded_file.type != "application/pdf" else ""

    if uploaded_file.type == "application/pdf":
        with open("temp.pdf", "wb") as f:
            f.write(file_bytes)
        file_text = "PDF FILE"  

    format_detected, intent = classify_input(file_text)

    st.write(f"**Format:** {format_detected}, **Intent:** {intent}")

    if format_detected.lower() == "email":
        process_email(file_text)
    elif format_detected.lower() == "json":
        process_json(file_text)
    elif format_detected.lower() == "pdf":
        process_pdf("temp.pdf")  
    else:
        st.warning("Unsupported format detected.")

    st.write("Shared Memory Output:")
    st.json(memory_store)
else:
    st.info("Please upload a file.")
