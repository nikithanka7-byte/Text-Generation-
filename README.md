# ✍️ AI Text Generation

<p align="center">
  <b>Generate meaningful text using Artificial Intelligence 🤖</b>
</p>

<p align="center">
  A simple and interactive AI Text Generation web application built with
  <b>Python, Streamlit, Hugging Face Transformers, and Qwen</b>.
</p>

---

## 🌟 Overview

**AI Text Generation** is a web-based application that uses a pre-trained
language model to automatically continue and generate text from a user's
input.

Users can enter a sentence, idea, or starting phrase, adjust the creativity
and output length, and generate AI-powered text through an easy-to-use
Streamlit interface.

---

## ✨ Features

- 🤖 AI-powered text generation
- ✍️ Simple text input interface
- 🎨 Adjustable creativity level
- 📏 Customizable text generation length
- 📝 Real-time word and character counter
- ⚡ Fast text generation using Transformer Pipeline
- 🤗 Hugging Face pre-trained model
- 🌐 Interactive Streamlit interface
- 💻 Easy to run locally

---

## 🖥️ Application Preview

[streamlit-app-2026-09-07-20-06-24.webm](https://github.com/user-attachments/assets/37927527-b6ec-4a7e-8b96-83b653a94ce3)


```text
┌──────────────────────────────────────┐
│        ✍️ Text Generation            │
│                                      │
│  💡 Enter Your Idea                  │
│  ┌──────────────────────────────────┐│
│  │ Artificial Intelligence is...    ││
│  └──────────────────────────────────┘│
│                                      │
│  🎨 Creativity       📏 Text Length  │
│                                      │
│             🚀 Generate              │
│                                      │
│  📝 Generated Result                 │
└──────────────────────────────────────┘


## 🛠️ Technologies Used
Technology and Purpose
🐍 Python -	Application development
🎈 Streamlit -	Web interface
🤗 Hugging Face - 	Pre-trained AI model
🔄 Transformers	- Text generation pipeline
🔥 PyTorch - Deep learning framework
🧠 Qwen2.5-0.5B-Instruct	- Text generation model


## 🧠 Model

This project uses:

Qwen/Qwen2.5-0.5B-Instruct

The model is loaded using the Hugging Face Transformers pipeline
for text generation.

pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)


##  🔄 How It Works
             👤 User
                │
                ▼
        ✍️ Enter Starting Text
                │
                ▼
         🌐 Streamlit App
                │
                ▼
      🔄 Transformer Pipeline
                │
                ▼
     🤗 Hugging Face Model
                │
                ▼
        🧠 Qwen Language Model
                │
                ▼
          📝 Generated Text


##  📂 Project Structure
AI-Text-Generation/
│
├── app.py
├── requirements.txt
└── README.md


### 🛠️ Requirements

### 💻 Software Requirements

- Python 3.14
- Visual Studio Code (VS Code)
- Internet Connection

### 📦 Python Libraries

- Streamlit
- Transformers
- PyTorch

### 🤖 Hugging Face Model

- Qwen/Qwen2.5-0.5B-Instruct

### 🔧 Tools & Technologies

| Tool / Technology | Purpose |
|---|---|
| Python 3.14 | Programming Language |
| Streamlit | Web Application Interface |
| Hugging Face Transformers | Transformer Pipeline |
| PyTorch | Deep Learning Framework |
| Qwen2.5-0.5B-Instruct | Text Generation Model |
| VS Code | Development Environment |


###  📦 Installation
1. Clone the Repository
git clone - https://github.com/nikithanka7-byte
2. Open the Project Folder
cd AI-Text-Generation
3. Install Dependencies
pip install streamlit transformers torch


### ▶️ Run the Application

Start the Streamlit application:

python -m streamlit run app.py

The application will be available at:

http://localhost:8501

Open the URL in your browser to use the application.


### 💡 Example

Input
Artificial Intelligence is

AI Generated Text
Artificial Intelligence is transforming the way people
work, learn, communicate, and solve complex problems.
It is becoming an important technology in many fields.

The generated result may vary each time because the model uses
probabilistic text generation.


### 🎨 Generation Controls
Creativity
The Creativity slider controls how diverse the generated text can be.

Lower Value  → More predictable
Higher Value → More creative

Text Length
Users can select the amount of text to generate:

30 → Short
50 → Medium
75 → Long
100 → Longer

###  📊 Text Analysis

Before generating text, the application displays:

📝 Number of words
🔤 Number of characters

This provides a quick overview of the user's input.


### 📚 Applications

This project can be useful for:

✍️ Creative writing
📝 Content generation
📖 Story continuation
💡 Idea generation
🎓 Educational purposes
📰 Article drafting
📢 Content creation
🤖 AI experimentation


### ✅ Advantages
Simple and beginner-friendly
Interactive user interface
Uses a pre-trained language model
No model training required
Customizable text generation
Easy to install and run
Can be extended with additional AI features


### 🚀 Future Enhancements

Some possible improvements include:

🌍 Multi-language text generation
📄 Download generated text as a file
💬 Chat-based AI interface
📚 Text summarization
🔤 Grammar correction
🎙️ Voice input
🔊 Text-to-speech output
🗂️ Generation history
☁️ Online deployment
🧠 Support for multiple AI models


### 🎯 Learning Outcomes

Through this project, I learned:

How to use Hugging Face Transformers
How to load a pre-trained language model
How Transformer pipelines work
How to build an interactive application using Streamlit
How to integrate AI models into Python applications
How to control text generation parameters
How to create and organize an AI project for GitHub


###  👩‍💻 Author
Nikitha R
B.Sc. Computer Science with Artificial Intelligence

### ⭐ Support
If you found this project useful, consider giving the repository a ⭐ on GitHub!

### 📄 License
This project is created for educational and learning purposes.

