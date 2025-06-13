# Multi-Agent Autonomous AI System

This project implements a multi-agent autonomous AI system capable of processing inputs in various formats (Email, JSON, PDF). It classifies the input format and business intent, then routes the input to specialized agents for further processing. The system uses OpenAI's Ollama LLM (Mistral model) for classification and extraction tasks, along with LangChain and PDF loaders.

## Features

- **Input Classification Agent:** Detects input format (Email/JSON/PDF) and business intent (Invoice, RFQ, Complaint, Regulation, Fraud Risk).
- **Email Processing Agent:** Extracts sender name, request intent, tone, and urgency from email text.
- **JSON Processing Agent:** Validates and parses JSON input.
- **PDF Processing Agent:** Extracts text content from PDF files.
- **Shared Memory Store:** Maintains context and state across agents.
- **Streamlit UI:** Web-based interface to upload files and view classified results.

## Technologies Used

- Python 3.x
- LangChain Ollama LLM (`mistral` model)
- PyPDFLoader (for PDF text extraction)
- Streamlit (for UI)
- JSON standard library
