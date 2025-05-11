# 🧠 LLM MultiNLP

A multi-functional NLP application built with Streamlit and Hugging Face Transformers, offering real-time interaction with various large language model (LLM) tasks.
You can access the Streamlit
👉 [Launch the Streamlit App](https://llm-multinlp.streamlit.app/)

## 🚀 Features

* **Text Classification**: Assign categories to input text.
* **Summarization**: Generate concise summaries of longer texts.
* **Part-of-Speech Tagging**: Identify grammatical components in sentences.
* **Question Answering**: Extract answers from provided contexts.
* **Text Generation**: Produce coherent text based on prompts.
* **Translation**: Convert text between languages.
* **Masked Word Prediction**: Predict missing words in sentences.([GitHub][1])

## 🛠️ Technologies Used

* **[Streamlit](https://streamlit.io/)**: For building the interactive web interface.
* **[Hugging Face Transformers](https://huggingface.co/transformers/)**: Provides pre-trained models for various NLP tasks.
* **[PyTorch](https://pytorch.org/)**: Deep learning framework underpinning model operations.([GitHub][2])

## 📂 Project Structure

```
LLM-practice/
├── .devcontainer/        # Development container configuration
├── LLM.py                # Core NLP functions
├── LLMapp.py             # Streamlit application script
└── requirements.txt      # Python dependencies
```

## ⚙️ Installation

1. **Clone the repository**:

   ```bash
   git clone https://github.com/Leosce/LLM-practice.git
   cd LLM-practice
   ```

2. **Create a virtual environment** (optional but recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## 🚀 Usage

Run the Streamlit application:

```bash
streamlit run LLMapp.py
```

Upon execution, a web interface will open in your default browser, allowing you to select and interact with various NLP functionalities.

## 📄 License

This project is licensed under the [MIT License](LICENSE).

## 🙌 Acknowledgements

* [Hugging Face](https://huggingface.co/) for providing accessible NLP models.
* [Streamlit](https://streamlit.io/) for simplifying the creation of web applications.([GitHub][1])
