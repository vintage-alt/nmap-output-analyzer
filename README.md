# AI-Assisted Nmap Reconnaissance Analyzer

## Overview
This project is an applied AI pipeline that bridges traditional network reconnaissance and automated security analysis. It parses raw `nmap` XML output, extracts open ports and service banners, and uses a local Large Language Model (LLM) to generate a structured, defensive-oriented risk report for each exposed service.

## Motivation
During my undergraduate capstone project, I built a Python/Django reconnaissance tool that handled port scanning and DNS lookups. While that project was successful, it relied heavily on manual interpretation of the results. For my Master's application and research interests, I wanted to explore how modern AI can augment this process—specifically, using LLMs not as a chat interface, but as a structured reasoning engine to explain service purposes and suggest defensive verification steps.

## Architecture & "Internal Actions"
The pipeline consists of three core steps:
1. **Parsing (`python-libnmap`)**: Reads the `nmap -sV -oX` XML file and extracts a clean JSON list of open ports, services, and exact version banners.
2. **Prompt Construction**: Formats the parsed data into a strict analytical prompt, instructing the AI to act as a defensive security analyst.
3. **Structured Inference (`Ollama` + `Pydantic`)**: Uses a locally hosted `qwen2.5:7b-instruct` model. Instead of letting the LLM output free-text, the script passes a Pydantic-generated JSON schema directly to Ollama's `format` parameter. This forces the LLM to output structured data (Purpose, Risk, Suggestion) at `temperature=0` to prevent hallucinations.

## Example Output
```text
Port 80 (http)
  Purpose: Web server for serving HTTP content.
  Risk: Vulnerabilities in the web application or Apache itself could be exploited.
  Suggestion: Check for known vulnerabilities in Apache version 2.4.7 (Ubuntu), ensure regular updates, and implement web application firewalling.

How to Run:
Install dependencies: pip install python-libnmap ollama pydantic
Generate a scan: nmap -sV -oX scan.xml scanme.nmap.org
Ensure Ollama is running and the model is pulled: ollama pull qwen2.5:7b-instruct
Run the analyzer: python main.py scan.xml
