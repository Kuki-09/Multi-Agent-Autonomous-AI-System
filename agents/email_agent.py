from memory.shared_memory import memory_store
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral") 

def process_email(email_body):
    prompt = f"""
   You are an information extraction assistant.

    From the following email, extract:
    - Sender name
    - Request intent (such as complaint, inquiry, quote, etc.)
    - Tone (e.g., Polite, Angry, Threatening)
    - Urgency (Low, Medium, High)

    Email:
    {email_body}

    Respond exactly in this format:

    Sender: <name>  
    Intent: <intent>  
    Tone: <tone>  
    Urgency: <urgency>
    """

    response = llm.invoke(prompt)
    lines = response.strip().split("\n")
    print(lines)
 
    parsed = {
            "sender": lines[0].split(":")[1].strip(),
            "intent": lines[1].split(":")[1].strip(),
            "tone": lines[2].split(":")[1].strip(),
            "urgency": lines[3].split(":")[1].strip()
        }
  
    memory_store["email"] = {"response": parsed}
    return parsed
