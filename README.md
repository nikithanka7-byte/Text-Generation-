# AI Text Generation


  <b>Generate meaningful text using Artificial Intelligence</b>
</p>


  A simple and interactive AI Text Generation web application built with
  <b>Python, Streamlit, Hugging Face Transformers, and Qwen</b>.
</p>

---

## Overview

**AI Text Generation** is a web-based application that uses a pre-trained
language model to automatically continue and generate text from a user's
input.

Users can enter a sentence, idea, or starting phrase, adjust the creativity
and output length, and generate AI-powered text through an easy-to-use
Streamlit interface.

---

## Features

- AI-powered text generation
- Simple text input interface
- Adjustable creativity level
- Customizable text generation length
- Real-time word and character counter
- Fast text generation using Transformer Pipeline
- Hugging Face pre-trained model
- Interactive Streamlit interface
- Easy to run locally

---

## Application Preview



```text
┌──────────────────────────────────────┐
│        Text Generation               │
│                                      │
│  Enter Your Idea                    │
│  ┌──────────────────────────────────┐│
│  │ Artificial Intelligence is...    ││
│  └──────────────────────────────────┘│
│                                      │
│  Creativity       Text Length        │
│                                      │
│             Generate                 │
│                                      │
│  Generated Result                    │
└──────────────────────────────────────┘

# 🤖 AI Text Generation using Qwen

An AI-powered **Text Generation Web Application** built using **Python, Streamlit, Hugging Face Transformers, PyTorch, and Qwen2.5-0.5B-Instruct**.

The application allows users to enter starting text and generate meaningful AI-generated text interactively.

---

## 🚀 Technologies Used

| **Technology**            | **Purpose**              |
| ------------------------- | ------------------------ |
| **Python**                | Application development  |
| **Streamlit**             | Web interface            |
| **Hugging Face**          | Pre-trained AI model     |
| **Transformers**          | Text generation pipeline |
| **PyTorch**               | Deep learning framework  |
| **Qwen2.5-0.5B-Instruct** | Text generation model    |

---

## 🧠 Model

This project uses:

**Qwen/Qwen2.5-0.5B-Instruct**

The model is loaded using the **Hugging Face Transformers pipeline** for text generation.

```python
from transformers import pipeline

generator = pipeline(
    "text-generation",
    model="Qwen/Qwen2.5-0.5B-Instruct"
)
```

---

## 🔄 How It Works

```text
                    ┌───────────────────┐
                    │       User        │
                    └─────────┬─────────┘
                              │
                              ▼
                 ┌────────────────────────┐
                 │ Enter Starting Text    │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │    Streamlit App       │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │ Transformer Pipeline   │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │   Hugging Face Model   │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │ Qwen Language Model    │
                 └───────────┬────────────┘
                             │
                             ▼
                 ┌────────────────────────┐
                 │   Generated Text       │
                 └────────────────────────┘
```

---

## 📊 Project Workflow – SVG Diagram

The following **SVG diagram** shows the complete workflow of the project.

<svg width="700" height="750" viewBox="0 0 700 750" xmlns="http://www.w3.org/2000/svg">

  <style>
    .box {
      fill: #f5f5f5;
      stroke: #222;
      stroke-width: 2;
      rx: 12;
      ry: 12;
    }

    .title {
      font-family: Arial, sans-serif;
      font-size: 22px;
      font-weight: bold;
      fill: #111;
    }

    .text {
      font-family: Arial, sans-serif;
      font-size: 17px;
      font-weight: bold;
      fill: #111;
    }

    .arrow {
      stroke: #222;
      stroke-width: 3;
      marker-end: url(#arrowhead);
    }
  </style>

  <defs>
    <marker id="arrowhead"
            markerWidth="10"
            markerHeight="10"
            refX="8"
            refY="3"
            orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#222"/>
    </marker>
  </defs>

  <text x="350" y="35" text-anchor="middle" class="title">
    AI Text Generation Workflow
  </text>

  <rect x="150" y="65" width="400" height="70" class="box"/>
  <text x="350" y="108" text-anchor="middle" class="text">
    User Input
  </text>

  <line x1="350" y1="135" x2="350" y2="175" class="arrow"/>

  <rect x="150" y="175" width="400" height="70" class="box"/>
  <text x="350" y="218" text-anchor="middle" class="text">
    Streamlit Web Application
  </text>

  <line x1="350" y1="245" x2="350" y2="285" class="arrow"/>

  <rect x="150" y="285" width="400" height="70" class="box"/>
  <text x="350" y="328" text-anchor="middle" class="text">
    Transformers Pipeline
  </text>

  <line x1="350" y1="355" x2="350" y2="395" class="arrow"/>

  <rect x="150" y="395" width="400" height="70" class="box"/>
  <text x="350" y="438" text-anchor="middle" class="text">
    Hugging Face Model
  </text>

  <line x1="350" y1="465" x2="350" y2="505" class="arrow"/>

  <rect x="150" y="505" width="400" height="70" class="box"/>
  <text x="350" y="548" text-anchor="middle" class="text">
    Qwen2.5-0.5B-Instruct
  </text>

  <line x1="350" y1="575" x2="350" y2="615" class="arrow"/>

  <rect x="150" y="615" width="400" height="70" class="box"/>
  <text x="350" y="658" text-anchor="middle" class="text">
    AI Generated Text
  </text>

</svg>

---

## 📁 Project Structure

```text
AI-Text-Generation/
│
├── app.py
├── requirements.txt
└── README.md
```

---

## 💻 Requirements

### Software Requirements

* **Python 3.14**
* **Visual Studio Code (VS Code)**
* **Internet Connection**

### Python Libraries

* **Streamlit**
* **Transformers**
* **PyTorch**
* **Hugging Face Model**
* **Qwen/Qwen2.5-0.5B-Instruct**

---

## 🛠️ Tools & Technologies

| **Tool / Technology**         | **Purpose**               |
| ----------------------------- | ------------------------- |
| **Python 3.14**               | Programming Language      |
| **Streamlit**                 | Web Application Interface |
| **Hugging Face Transformers** | Transformer Pipeline      |
| **PyTorch**                   | Deep Learning Framework   |
| **Qwen2.5-0.5B-Instruct**     | Text Generation Model     |
| **VS Code**                   | Development Environment   |

---

## 📥 Installation

### 1. Clone the Repository

```bash
git clone https://github.com/nikithanka7-byte/Text-Generation-
```

### 2. Open the Project Folder

```bash
cd AI-Text-Generation
```

### 3. Install Dependencies

```bash
pip install streamlit transformers torch
```

---

## ▶️ Run the Application

Start the Streamlit application using:

```bash
python -m streamlit run app.py
```

The application will be available at:

```text
http://localhost:8501
```

Open the URL in your browser to use the application.

---

## 📝 Example

### Input

```text
Artificial Intelligence is
```

### AI Generated Text

```text
Artificial Intelligence is transforming the way people
work, learn, communicate, and solve complex problems.
It is becoming an important technology in many fields.
```

> **Note:** The generated result may vary each time because the model uses probabilistic text generation.

---

## 🎛️ Generation Controls

### 🎨 Creativity

The **Creativity slider** controls how diverse the generated text can be.

* **Lower Value** → More predictable
* **Higher Value** → More creative

### 📏 Text Length

Users can select the amount of text to generate:

| **Value** | **Output** |
| --------: | ---------- |
|    **30** | Short      |
|    **50** | Medium     |
|    **75** | Long       |
|   **100** | Longer     |

---

## 📊 Text Analysis

Before generating text, the application displays:

* **Number of words**
* **Number of characters**

This provides a quick overview of the user's input.

---

## 🌍 Applications

This project can be useful for:

* ✍️ **Creative writing**
* 📝 **Content generation**
* 📖 **Story continuation**
* 💡 **Idea generation**
* 🎓 **Educational purposes**
* 📄 **Article drafting**
* 🤖 **Content creation**
* 🧪 **AI experimentation**

---

## ✅ Advantages

* **Simple and beginner-friendly**
* **Interactive user interface**
* **Uses a pre-trained language model**
* **No model training required**
* **Customizable text generation**
* **Easy to install and run**
* **Can be extended with additional AI features**

---

## 🔮 Future Enhancements

Future versions of this project can include:

* **Multiple AI model selection**
* **Text summarization**
* **Text translation**
* **Download generated text**
* **Voice input and output**
* **Advanced generation controls**
* **Chatbot functionality**
* **Conversation history**
* **Dark mode UI**
* **Cloud deployment**

---

## 🎓 Learning Outcomes

Through this project, I learned:

* **How to use Hugging Face Transformers**
* **How to load a pre-trained language model**
* **How Transformer pipelines work**
* **How to build an interactive application using Streamlit**
* **How to integrate AI models into Python applications**
* **How to control text generation parameters**
* **How to create and organize an AI project for GitHub**

---

## 👩‍💻 Author

### **Nikitha R**

**B.Sc. Computer Science with Artificial Intelligence**

---

