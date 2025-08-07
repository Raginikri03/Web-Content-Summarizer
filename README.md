## Web Content Summarizer
A simple Streamlit web application that summarizes the content of any website URL using the power of LangChain, Groq API, and LLaMA3.

This app loads a given webpage, extracts its textual content, and produces a concise summary using large language models.

 ## Live App
https://web-content-summarizer-ucxyjzyqdxptk5hvzbpqfb.streamlit.app/

## Features
-Extracts text from any public website URL

-Summarizes long content using LLaMA3 via the Groq API

-Built using LangChain's load_summarize_chain (map_reduce chain)

-Handles multi-page docs with ease

-Secure Groq API key input via .streamlit/secrets.toml

## Tech Stack
Streamlit – Frontend UI

LangChain – Prompting & LLM orchestration

Groq API – LLaMA3 backend

UnstructuredURLLoader – Web content extraction

Transformers – Token counting dependency

## Folder Structure
📦summarizer/
 ┣ 📄app.py
 ┣ 📄requirements.txt
 ┣ 📁.streamlit/
 ┃ ┗ 📄secrets.toml
 ┗ 📄README.md
✅ Requirements
Make sure you have the following installed:

bash
Copy
Edit
pip install -r requirements.txt
Setting up Groq API Key
Create a .streamlit/secrets.toml file in the root of your project:

toml
Copy
Edit
GROQ_API_KEY = "your-groq-api-key"
Never expose your API key publicly!

## Run Locally
bash
Copy
Edit
streamlit run app.py
📸 Screenshots
<!-- Replace with your actual screenshot if available -->

🧠 How It Works
User enters a valid URL

App loads the content using UnstructuredURLLoader

The Groq LLM (LLaMA3) is invoked via LangChain's load_summarize_chain

Final summary is shown in the UI
