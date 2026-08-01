# 🚀 OrbitDesk AI Support Agent

The OrbitDesk AI Support Agent is a Retrieval-Augmented Generation (RAG) application designed to answer OrbitDesk support queries using internal documentation and resolved support cases. The system combines semantic document retrieval with a local Large Language Model (LLM) to generate accurate, source-grounded responses. It also supports query classification, answer verification, clarification requests, escalation handling, and structured JSON output.

---

## 📌 Features

- 🧠 Intelligent Query Triage
- 📚 Retrieval-Augmented Generation (RAG)
- 🔍 FAISS Vector Similarity Search
- 📖 Knowledge Base & Resolved Case Retrieval
- ⚡ Priority-Based Document Ranking
- 🤖 Local LLM Response Generation
- ✅ Answer Verification
- 👨‍💻 Human Escalation Workflow
- ❓ Clarification Workflow
- 🚫 Out-of-Scope Detection
- 📊 Confidence Scoring
- 📝 Source Attribution
- 📦 Structured JSON Responses
- 🏗️ Modular LangGraph Pipeline

---

# 🏗️ System Architecture


![System Architecture](diagrams/architecturediagram.png)

---

# ⚙️ Workflow

```text
                    User Question
                          │
                          ▼
                   Triage Node
                          │
      ┌───────────────────┼────────────────────┐
      │                   │                    │
      ▼                   ▼                    ▼
 Answerable      Requires Escalation    Out of Scope
      │                   │                    │
      ▼                   ▼                    ▼
 Retrieval         Escalation        Out-of-Scope
      │             Response            Response
      ▼
 Generator
      │
      ▼
 Verifier
      │
      ▼
 Final JSON Response
```

---

# 🛠️ Technology Stack

| Category | Technology |
|----------|------------|
| Language | Python |
| Workflow | LangGraph |
| Vector Search | FAISS |
| Embeddings | Sentence Transformers |
| LLM | TinyLlama (Local LLM) |
| Deep Learning | PyTorch |
| Logging | Python Logging |
| Data Storage | Knowledge Base & Resolved Cases |

---

# 📂 Project Structure

```text
orbitdesk-support-agent/
│
├── app.py
├── graph.py
├── config.py
├── state.py
├── build_index.py
├── requirements.txt
├── README.md
│
├── models/
│   └── llm.py
│
├── nodes/
│   ├── triage.py
│   ├── retrieval.py
│   ├── generator.py
│   └── verifier.py
│
├── utils/
│   ├── embeddings.py
│   ├── loader.py
│   └── logger.py
│
├── knowledge_base/
├── resolved_cases/
├── vector_store/
│
├── diagram/
│   └── architecturediagram.png
│
└── screenshots/
    ├── Screenshot 1.png
    ├── Screenshot 2.png
    ├── Screenshot 3.png
    ├── Screenshot 4.png
    ├── Screenshot 5.png
    ├── Screenshot 6.png
    └── Screenshot 7.png
```

---

# 🚀 Installation

## 1️⃣ Clone the Repository

```bash
git clone https://github.com/Dhanushsj12/orbitdesk-support-agent.git
```

```bash
cd orbitdesk-support-agent
```

---

## 2️⃣ Create a Virtual Environment

```bash
python -m venv .venv
```

---

## 3️⃣ Activate the Environment

### Windows

```bash
.venv\Scripts\activate
```

---

## 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 5️⃣ Build the FAISS Index

```bash
python build_index.py
```

---

## 6️⃣ Run the Application

```bash
python app.py
```

---

# 📥 Sample Input

```text
Can a Viewer create API credentials?
```

---

# 📤 Sample Output

```json
{
  "classification": "answerable",
  "answer": "No. Viewers cannot create workspace API credentials. Only Owners and Admins can create or revoke workspace API credentials.",
  "confidence": 0.9,
  "verified": true,
  "requires_human": false,
  "reason": "Answer verified.",
  "sources": [
    {
      "source_id": "05_api_credentials",
      "type": "knowledge_base"
    },
    {
      "source_id": "02_roles_and_permissions",
      "type": "knowledge_base"
    }
  ]
}
```

---
# 📸 Application Demonstration

## ✅ Answerable Query

**Question**

```text
Can a Viewer create API credentials?
```

<p align="center">
    <img src="screenshots/Screenshot%201.png" width="950">
</p>

---

## 🔐 Security Question

**Question**

```text
What should I do if my API credential secret is exposed?
```

<p align="center">
    <img src="screenshots/Screenshot%202.png" width="950">
</p>

---

## 👨‍💼 Admin Permissions

**Question**

```text
What permissions does an Admin have?
```

<p align="center">
    <img src="screenshots/Screenshot%203.png" width="950">
</p>

---

## 🚨 Escalation Workflow

**Question**

```text
I followed every troubleshooting step in the documentation but my scheduled export still fails.
```

<p align="center">
    <img src="screenshots/Screenshot%204.png" width="950">
</p>

---

## 🚫 Out-of-Scope Request

**Question**

```text
Can you refund my subscription?
```

<p align="center">
    <img src="screenshots/Screenshot%205.png" width="950">
</p>

---

## ❓ Clarification Workflow (Help)

**Question**

```text
Help
```

<p align="center">
    <img src="screenshots/Screenshot%206.png" width="950">
</p>

---

## ❓ Clarification Workflow (API)

**Question**

```text
API
```

<p align="center">
    <img src="screenshots/Screenshot%207.png" width="950">
</p>

---

# 🔄 Supported Workflows

✔️ Intelligent Query Classification

✔️ Retrieval-Augmented Generation (RAG)

✔️ Knowledge Base Retrieval

✔️ Resolved Case Retrieval

✔️ Local LLM Response Generation

✔️ Answer Verification

✔️ Confidence Scoring

✔️ Human Escalation

✔️ Clarification Requests

✔️ Out-of-Scope Detection

✔️ Source Attribution

✔️ Structured JSON Responses

---
# 🤖 Model Configuration

| Component | Model |
|-----------|-------|
| Large Language Model | TinyLlama-1.1B-Chat-v1.0 |
| Embedding Model | sentence-transformers/all-MiniLM-L6-v2 |
| Vector Database | FAISS (CPU) |
| Workflow Engine | LangGraph |
| Deep Learning Framework | PyTorch |


# 💻 Hardware Configuration

| Component | Specification |
|-----------|---------------|
| Laptop | Samsung Galaxy Book2 |
| Processor | 12th Gen Intel® Core™ i5-1235U (10 Cores, 12 Threads) |
| RAM | 16 GB |
| Storage | SSD |
| Graphics | Intel® Iris® Xe Graphics |
| Operating System | Windows 11 |
| Execution Device | CPU |

# 🎯 Example Use Cases

The OrbitDesk AI Support Agent can assist with:

- User role and permission queries
- API credential management
- Security best practices
- Troubleshooting support issues
- Knowledge Base search
- Resolved case retrieval
- Safe response generation
- Escalation recommendations

# 🤝 AI Assistance Disclosure

During the development of this project, AI-assisted tools (including ChatGPT) were used to:

- Explain technical concepts.
- Assist with debugging and error analysis.
- Improve project documentation.
- Review code structure and implementation approaches.

All project design decisions, workflow implementation, testing, integration, and final validation were completed and verified by the author.

---

# 🚀 Future Enhancements

- 🌐 FastAPI REST API
- 💬 Streamlit Web Interface
- 🐳 Docker Deployment
- ☁️ Cloud Deployment (Azure/AWS/GCP)
- 🔑 Authentication & Authorization
- 🧠 Conversation Memory
- 📄 PDF Knowledge Base Support
- 🔎 Hybrid Search (Keyword + Semantic Search)
- 📊 Analytics Dashboard
- 🔄 Continuous Knowledge Base Updates

---

# 📈 Project Highlights

- Built using **LangGraph** for workflow orchestration.
- Uses **FAISS** for efficient semantic document retrieval.
- Generates grounded responses using a **local LLM**.
- Verifies generated answers before returning them.
- Supports escalation and clarification workflows.
- Produces structured JSON responses with confidence scores and source references.
- Modular architecture for easy extension and maintenance.


# 📁 Repository Contents

- Source Code
- Knowledge Base Documents
- Resolved Support Cases
- FAISS Vector Store
- Architecture Diagram
- Sample Screenshots
- README Documentation
- Requirements File
---

# 👨‍💻 Author

## Dhanush S J

Integrated M.Tech – Software Engineering

Vellore Institute of Technology (VIT)

### GitHub

https://github.com/Dhanushsj12

### LinkedIn

https://www.linkedin.com/in/dhanush-s-j-034147271

---

# 📜 License

This project is intended for educational and internship demonstration purposes.

You may use, modify, and distribute this project in accordance with the terms of the MIT License.

---

# 🙏 Acknowledgements

- LangGraph
- Hugging Face Transformers
- Sentence Transformers
- FAISS
- PyTorch
- TinyLlama
- Python Open Source Community

---

# ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

It helps others discover the project and supports future improvements.
