import validators
import streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import UnstructuredURLLoader

# Streamlit Page Config
st.set_page_config(page_title="LangChain: Summarize Website Text", page_icon="🦜")
st.title("🦜 LangChain: Summarize Website Text")
st.subheader('Summarize URL')

# Sidebar for API Key input
with st.sidebar:
    groq_api_key = st.secrets["GROQ_API_KEY"] if "GROQ_API_KEY" in st.secrets else st.text_input("Groq API Key", value="", type="password")

# Input for Website URL
generic_url = st.text_input("Enter Website URL")

# On button click
if st.button("Summarize the Content from Website"):
    if not groq_api_key.strip():
        st.error("Please provide your Groq API key.")
    elif not generic_url.strip() or not validators.url(generic_url):
        st.error("Please enter a valid website URL.")
    else:
        try:
            with st.spinner("Loading and summarizing content..."):
                # Load data from URL
                loader = UnstructuredURLLoader(
                    urls=[generic_url],
                    ssl_verify=False,
                    headers={
                        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                                      "Chrome/116.0.0.0 Safari/537.36"
                    }
                )
                docs = loader.load()

                # Optional: Limit number of documents to avoid token overload
                docs = docs[:3]  # adjust if needed

                # Initialize Groq LLM
                llm = ChatGroq(model="llama3-8b-8192", groq_api_key=groq_api_key)

                # Load summarization chain without passing custom prompt
                chain = load_summarize_chain(llm, chain_type="map_reduce")

                # Run the chain and display output
                output_summary = chain.run(docs)
                st.success(output_summary)

        except Exception as e:
            st.error(f"❌ Error occurred: {e}")
