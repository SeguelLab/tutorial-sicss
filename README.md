# tutorial-sicss

### Purpose: Hands-on SICSS tutorial notebooks, will flip to public after polishing

## Overview

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

We will explain how to store your key securely, such as using environment variables or secret management tools.

Please follow the platform's ethical guidelines and terms of service.

### Learning Goals
By the end of this tutorial, you should be able to:

Build basic LLM agents for data classification

Apply prompt engineering techniques

Automate web-based information retrieval

Reflect on the reliability, reproducibility, and ethics of these tools in research.

### Extensions and Directions
We will also discuss how these techniques can be extended to:

Classifying and annotating your own research datasets

Supporting qualitative coding workflows

Searching across open-access archives or academic corpora

### License & Credits
This material is part of a research and teaching initiative affiliated with [Toronto Metropolitan University].
Please cite appropriately if you use or modify these materials.

👨‍🏫 Authors: Pedro Seguel, Artin Majd, Tharu Yakkala Arachchilage Don, Afeef Shaikh

---

## Structure of the Repository
```
tutorial-sicss/
├── data   
|   └── sports_teams.csv # sample data for notebook 3
├── notebooks
|   ├── 1.OpenAI_API_Tutorial.ipynb # Simple Open AI API example
|   ├── 2.LLM_Agent_+_WebSearch_tool_Tutorial.ipynb # LLM agent example
|   ├── 3.LangChain_Agent_WebSearch_Team_Classifier.ipynb # LLM agent classification example
|   └── 4.Model_Evaluation.ipynb # Model evaluation metrics
|   └── 5.Tutorial_Cleaning_Messy_Names_with_Dedupe.ipynb # Fuzzy Matching
├── slides
├── .env.template # Sample environment variable setup
├── README.md # Main documentation
├── requirements.txt # Dependencies
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

**[NOTE] DO NOT PUT API KEYS DIRECTLY IN YOUR CODE/NOTEBOOKS**

Instead, we will put them into a .env file, which will then be loaded as a system variable.

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

Alternatively, you can also enter your API key using the getpass library, which will be shown in the `OPENAI_API_Tutorial`. 

## Tutorial Workflow

### [1️⃣ OpenAI API Tutorial](notebooks/1.OpenAI_API_Tutorial.ipynb)

In this first tutorial, you will call the OpenAI API with a prompt and print out the response you get from ChatGPT. We will be using gpt-3.5-turbo for this, but you can use other models you have access to as well.

You will learn the basic syntax and process of making a simple call to the OpenAI API, and the meaning of some parameters that we pass into the call.

### [2️⃣ LLM Agent + WebSearch](notebooks/2.LLM_Agent_+_WebSearch_tool_Tutorial.ipynb)

Now, going beyond just using a simple question and response, we use LangChain, a library for AI Agent orchestration. Using a web search tool
called Tavily AI, it will first search the web to get more information in order to answer the question. This is then passed on to the LLM (ChatGPT) to obtain a final result.


### [3️⃣ LangChain Agent and Classification](notebooks/3.LangChain_Agent_WebSearch_Team_Classifier.ipynb)

Building on our earlier work with LangChain and Taverly, we will utilize the agent to classify some data. We have some sample data of different sports teams where
The agent will attempt to determine which sport the sports team belongs to by combining web searches and GPT.

### [4️⃣ How to evaluate classification models](notebooks/4.Model_Evaluation.ipynb)

We are working with a technique called zero-shot classification, which is an unsupervised approach that doesn't require any labeled data. If we did use labeled data, how can we make sure that the predictions/classifications from the model are correct? We will look at a few model evaluation measures that will allow us to compare different results. We will be using precision, recall, F1-score, and accuracy. These metrics can be used to compare different models and are the most widely used metrics for classification tasks.

### [Bonus: 5 Using Fuzzy Matching to Clean Organizational Names](notebooks/4.Model_Evaluation.ipynb)

This notebook walks through the process of identifying and resolving inconsistencies in organization names using fuzzy matching techniques with the `dedupe` Python library. Includes basic cleaning, model training, clustering of similar names, and assigning canonical names. 
