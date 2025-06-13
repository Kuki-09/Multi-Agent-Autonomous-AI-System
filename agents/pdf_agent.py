from langchain_community.document_loaders import PyPDFLoader
from memory.shared_memory import memory_store

def process_pdf(pdf_path):
    loader = PyPDFLoader(pdf_path)
    pages = loader.load()
    full_text = "\n".join(page.page_content for page in pages)
    result = {}

    result["text_snippet"] = full_text
    memory_store["pdf"] = result
