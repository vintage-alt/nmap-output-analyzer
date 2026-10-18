# analyze_ports.py
import json
from pydantic import BaseModel
from typing import List
from ollama import chat

class PortRisk(BaseModel):
    port: int
    service: str
    purpose: str          
    risk: str             
    suggestion: str       

class ScanReport(BaseModel):
    summary: str
    ports: List[PortRisk]

def analyze_ports(open_ports: list) -> ScanReport:
    prompt = f"""You are a defensive security analyst. Below is a list of open ports and services:
{json.dumps(open_ports, indent=2)}

For each port, explain:
1. The normal purpose of this service
2. Possible security risks if exposed
3. A defensive verification direction (e.g., "check if the version has known CVEs" or "verify authentication is enabled")

Be concise. Do not suggest attacking anything."""

    response = chat(
        model='qwen2.5:7b-instruct',   
        messages=[{'role': 'user', 'content': prompt}],
        format=ScanReport.model_json_schema(),  
        options={'temperature': 0}
    )
    return ScanReport.model_validate_json(response.message.content)