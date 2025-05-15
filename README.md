# tutorial-sicss

### Purpose: Hands-on SICSS tutorial notebooks, will flip to public after polish

## 🌟 Overview

In this tutorial, you will learn how to:

- Set up and use LLM agents through APIs (e.g., OpenAI, DeepSeek)
- Classify structured datasets using agents
- Conduct guided web search tasks with agent-based tools
- Customize prompts and manage API calls responsibly
- Understand practical use cases and limitations

This tutorial is designed for researchers with varying levels of coding experience. Some familiarity with Python or R is helpful, but not required.

### 🔐 API Access and Privacy
This tutorial requires access to an LLM API (e.g., OpenAI, DeepSeek, etc.).

API keys will not be shared publicly.

We will explain how to store your key securely (e.g., using environment variables or secret management tools).

Please follow ethical guidelines and platform terms of service.

### 🧠 Learning Goals
By the end of this tutorial, you should be able to:

Build basic LLM agents for data classification

Apply prompt engineering techniques

Automate web-based information retrieval

Reflect on the reliability, reproducibility, and ethics of these tools in research

### 📦 Extensions and Directions
We will also discuss how these techniques can be extended to:

Classifying and annotating your own research datasets

Supporting qualitative coding workflows

Searching across open-access archives or academic corpora

### 🤝 License & Credits
This material is part of a research and teaching initiative affiliated with [your institution/project].
Please cite appropriately if you use or modify these materials.

👨‍🏫 Authors: [Add your names here]

---

## 🧱 Structure of the Repository
```
tutorial-sicss/
├── data
|    └── sample_dataset.csv # Dataset with 'name' column
|
├── notebooks
|   └── tutorial.ipynb # Jupyter Notebook walkthrough
|
├── outputs
|
├── src # python scripts used in tutorial
|    └── agent.py   # Agent logic and API interface
|
├── utils # helper scripts
|    └── api_helpers.py # Web search, prompt engineering etc.
|
├── README.md # Main documentation
├── requirements.txt
├── .env.template # Sample environment variable setup
```
---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/YourOrg/tutorial-sicss.git
cd tutorial-sicss
```
### 2. Load dependencies

```bash
python -m venv venv # create python virtual environment
source venv/bin/activate   # or venv\\Scripts\\activate on Windows
pip install -r requirements.txt # install required dependencies
```

### 3. Proper use of API Keys

**[NOTE] DO NOT PUT API KEYS DIRECTLY IN YOUR CODE/NOTEBOOKS.**

Instead we will put them into a .env file, which will then be loaded as a system variable.

You can start by making a copy of the file `.env.template` and saving it as `.env`, and putting your
API key in there.

The file should look like this.
```
OPENAI_API_KEY="Enter your api key here"
```
Loading the API key:
```python
from python-dotenv import load_dotenv
import os

load_dotenv()

openai_api_key = os.getenv("OPENAI_API_KEY")
```

file_path = "/mnt/data/README_tutorial_sicss.md"
with open(file_path, "w") as file:
file.write(readme_content)

file_path

Mostrar siempre los detalles

Copiar
