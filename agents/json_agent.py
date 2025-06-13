import json
from memory.shared_memory import memory_store

def process_json(json_text):
    try:
        data = json.loads(json_text)
        memory_store["json"] = {
            "valid": True,
            "data": data
        }
    except Exception as e:
        memory_store["json"] = {
            "valid": False,
            "errors": [str(e)]
        }
