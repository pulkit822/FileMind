import os
import tempfile
import pandas as pd
import PyPDF2
import streamlit as st
from langchain_community.chat_models import ChatOpenAI
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

# Initialize OpenAI model
llm = ChatOpenAI(openai_api_key=api_key, model_name="gpt-3.5-turbo")

# Set up memory
memory = ConversationBufferMemory(input_key="question", memory_key="chat_history")

# Prompt template
template = """
You are an intelligent data science assistant. Use the context from file if available.

Context from file:
{context}

Question: {question}
"""
prompt = PromptTemplate(input_variables=["context", "question"], template=template)

# Create chain
chain = LLMChain(llm=llm, prompt=prompt, memory=memory)

# Streamlit app
st.set_page_config(page_title="🧠 IntelliChat")
st.title("🧠 Intellichat")
st.markdown("""#### Ask questions from data science domain or upload a file (PDF/CSV).""")

# Initialize session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "file_context" not in st.session_state:
    st.session_state.file_context = ""

# File uploader
uploaded_file = st.file_uploader("📎 Upload PDF or CSV", type=["pdf", "csv"])
if uploaded_file:
    try:
        if uploaded_file.type == "application/pdf":
            reader = PyPDF2.PdfReader(uploaded_file)
            text = "\n".join(page.extract_text() or "" for page in reader.pages)
        elif uploaded_file.type == "text/csv":
            df = pd.read_csv(uploaded_file)
            text = df.to_string(index=False)
        else:
            text = ""
        st.session_state.file_context = text[:3000]  # truncate to avoid prompt overflow
        st.success("File uploaded and parsed successfully!")
    except Exception as e:
        st.error(f"Error parsing file: {e}")

# Predefined questions
options = [
    "Explain PCA in simple terms.",
    "What is the bias-variance tradeoff?",
    "Difference between bagging and boosting?",
    "What is regularization in ML?"
]
selected_question = st.selectbox("Select a question:", options)
custom_question = st.text_input("Or ask your own question:")

final_question = custom_question.strip() if custom_question else selected_question

# Submit button
if st.button("Ask") and final_question:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": final_question, "context": st.session_state.file_context})
        st.session_state.chat_history.append((final_question, response["text"]))

# Display chat history
for i, (q, a) in enumerate(st.session_state.chat_history[::-1]):
    st.markdown(f"**You:** {q}")
    st.markdown(f"**Bot:** {a}")
    if i < len(st.session_state.chat_history) - 1:
        st.markdown("---")
