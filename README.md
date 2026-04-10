# 🧠 Concept Simplifier Tool (AI Powered)

A simple AI-powered CLI tool that simplifies complex topics into easy-to-understand explanations using **Strands Agents** and **Ollama (LLaMA 3.1)**.

---

## 🚀 Features

- Simplifies complex concepts into beginner-friendly language  
- Uses local AI model (no API cost)  
- Fast and lightweight CLI application  
- Works completely offline using Ollama  

---

## 🛠️ Tech Stack

- Python 🐍  
- Strands Agent Framework  
- Ollama (LLaMA 3.1)  
- Local LLM inference  

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/concept-simplifier.git
cd concept-simplifier
pip install strands ollama strands-agents-tools
ollama pull llama3.1
ollama run llama3.1
python app.py