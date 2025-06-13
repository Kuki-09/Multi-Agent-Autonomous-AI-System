from memory.shared_memory import memory_store
from langchain_ollama import OllamaLLM

llm = OllamaLLM(model="mistral") 


def classify_input(text):
    prompt = f"""
    You are an expert AI input classifier.
    
    Respond in exactly this format only:
    Format: <PDF/JSON/Email>
    Intent: <Invoice/Request for Quotation (RFQ)/Complaint/Regulation/Fraud Risk>
    ---
    
    Example 1:
    Input:
    Subject: Quotation Request – Conference Room Equipment

    Dear Supplier,

    We are planning to set up a new conference room at our Noida office and are exploring suppliers for the required equipment.

    Items Needed:
    - Projector (HD, ceiling-mounted) – 2 units
    - 65-inch LED Display Panels – 3 units
    - Wireless Presentation Device – 2 units
    - Audio System with Ceiling Speakers – 1 full set

    Please share your commercial offer with unit pricing, delivery lead time, warranty coverage, and installation charges if applicable.

    Kindly send your quote by July 10, 2025.

    Regards,  
    Facilities Procurement Team  
    Vertex Solutions Pvt. Ltd.


    Output:
    Format: Email
    Intent: Request for Quotation

    Example 2:
    Input:
    {{
    "sender_name": "Alice Smith",
    "company": "Global Tech",
    "request_type": "Invoice",
    "invoice_number": "INV-1234",
    "total_amount": 1250.00,
    "items": [...]
    }}
    Output:
    Format: JSON
    Intent: Invoice
    
    Example 3:
    Input:
    Invoice Number: INV-1234  
    Total Due: $1,250  
    Due Date: March 5, 2025  
    Includes: 5 chairs, 3 desks

    Output:
    Format: PDF  
    Intent: Invoice
    
    Example 4:
    Input:
    To whom it may concern,  
    I received a damaged product in my last shipment from your company. Despite multiple emails, I have not heard back. Please address this complaint immediately.  
    Thanks,  
    Ravi Mehta

    Output:
    Format: Email
    Intent: Complaint
    
    Example 5:
    Input:
    Subject: Urgent: Potential Internal Security Breach
    
    Hi Security Team,
    During our weekly audit, we discovered unauthorized access to sensitive internal financial records by an unknown system user. Multiple transactions appear to have been triggered from unverified IPs, and several login attempts bypassed the standard MFA protocol.
    This pattern raises serious fraud concerns. We recommend immediate lockdown of affected systems and investigation by the Fraud Risk Unit.

    Regards,  
    Nina Das  
    Cybersecurity Lead  
    Northshore Capital

    Output:
    Format: PDF
    Intent: Fraud Risk
    
    Example 6:
    Input:
    Subject: Mandatory Data Governance Policy – Effective July 2025

    Dear Team,

    In accordance with the revised national Data Privacy Regulation Act 2025, all departments must update their data handling protocols. New audit procedures and encryption standards must be implemented before Q3 to ensure legal compliance.
    Non-adherence may result in penalties.
    Please review the attached regulation document and ensure department-wide awareness.

    Regards,  
    Legal Compliance Cell  
    Aether Data Services

    Output:
    Format: PDF
    Intent: Regulation
    
    Example 7:
    Subject: Request for Quotation – Printer Cartridges

    Dear Supplier,

    Please provide a quotation for the supply of 50 black and 50 color printer cartridges (Model: HP 202A). Include unit price, taxes, and delivery charges.
    Send your quote by July 5, 2025.

    Regards,  
    Admin Team  
    NextGen Solutions Pvt. Ltd.

    --
    Now Classify the Following input:
    {text}
    
    """
    result = llm.invoke(prompt)
    print(result)
    format_detected = extract_format(result)
    intent_detected = extract_intent(result)

    memory_store['classification'] = {
        "format": format_detected,
        "intent": intent_detected
    }
    return format_detected, intent_detected

def extract_format(result):
    for line in result.splitlines():
        if "Format:" in line:
            return line.split(":")[1].strip()
    return "Unknown"

def extract_intent(result):
    for line in result.splitlines():
        if "Intent:" in line:
            return line.split(":")[1].strip()
    return "Unknown"
