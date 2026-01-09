# 📄 FileMind – AI That Reads and Responds

FileMind is an **AI-powered chatbot** built with **Streamlit**, **LangChain**, and **OpenAI** that can read your **PDF/CSV** files and answer questions using the file’s content as context.  
It supports multi-turn conversations with memory, making it perfect for interactive Q&A sessions.

---

## 🚀 Features
- 📂 **Upload PDF/CSV files** and query them instantly
- 💬 **Conversational AI** with chat history using LangChain’s `ConversationBufferMemory`
- 🤖 Powered by **OpenAI GPT** models via LangChain
- 📑 Extracts file content using **PyMuPDF (`fitz`)** and **pandas**
- 🖥 Simple, clean **Streamlit** UI

---

## 🧱 Tech Stack
- **Python 3.10+**
- **Streamlit**
- **LangChain**
- **OpenAI API**
- **PyMuPDF (`fitz`)**
- **pandas**

---

---

## 🧑‍💻 Setup Instructions

### 1. Clone the Repo

```bash
git clone https://github.com/yourusername/FileMind.git
cd FileMind
````

### 2. Create Virtual Environment (optional but recommended)

```bash
python -m venv venv
# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

> If `PyPDF2` or `streamlit` are missing, you can install them individually:

```bash
pip install PyPDF2 streamlit langchain openai python-dotenv pandas
```

---

## 🔑 Setup API Keys

Create a `.env` file in the root directory:

```bash
touch .env
```

Add your OpenAI API key:

```env
OPENAI_API_KEY=your-openai-api-key
```

> You can get your OpenAI API key from [https://platform.openai.com/account/api-keys](https://platform.openai.com/account/api-keys)

---

## 📁 File Upload Format

* PDF: Any readable text-based document
* CSV: Well-formatted table with headers

Once uploaded, FileMind can answer questions **based on the content** of the file.

---

## ▶️ Run the App

```bash
streamlit run app.py
```

Then open your browser and go to:
`http://localhost:8501`

---

## 📌 File Structure

```
FileMind/
│
├── app.py               # Main Streamlit app
├── requirements.txt     # Dependencies
├── .env                 # API Key file (you create this)
├── utils.py             # File processing helper functions
├── README.md            # This file
├── demo.png             # Optional screenshot for GitHub
```

---

## 📣 Future Ideas

* Add support for DOCX or XLSX files
* User login with session-based chat history
* Choice of LLMs (GPT-4, LLaMA 2, Mistral, etc.)
* Export full chat as PDF

---

## 📝 License

This project is licensed under the MIT License.

---

## 🙋‍♀️ Contact

Created by **Nitin Rathour**.
Feel free to raise issues or feature requests.

---

```

Let me know if you'd like:
- A sample `requirements.txt`
- GitHub repo structure auto-upload
- Deployment instructions (Streamlit Cloud, Hugging Face Spaces, etc.)
```
