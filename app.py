import streamlit as st
from transformers import pipeline

st.set_page_config(
    page_title="Text Generation",
    page_icon="✍️",
    layout="centered"
)

st.title("✍️ Text Generation")
st.write("Enter your idea and let AI continue the text.")

st.divider()

@st.cache_resource
def get_model():
    return pipeline(
        "text-generation",
        model="Qwen/Qwen2.5-0.5B-Instruct"
    )

generator = get_model()

st.subheader("💡 Enter Your Idea")

user_text = st.text_area(
    "Starting Text",
    height=150,
    placeholder="Example: Artificial Intelligence is changing..."
)

if user_text.strip():
    words = len(user_text.split())
    characters = len(user_text)

    col1, col2 = st.columns(2)

    with col1:
        st.metric("📝 Words", words)

    with col2:
        st.metric("🔤 Characters", characters)

st.divider()

st.subheader("⚙️ Generation Settings")

col1, col2 = st.columns(2)

with col1:
    creativity = st.slider(
        "🎨 Creativity",
        0.2,
        1.2,
        0.7,
        0.1
    )

with col2:
    max_words = st.selectbox(
        "📏 Text Length",
        [30, 50, 75, 100],
        index=1
    )

if st.button("🚀 Generate", use_container_width=True):

    if not user_text.strip():
        st.warning("⚠️ Please enter some text first.")

    else:
        with st.spinner("🤖 Generating text..."):

            response = generator(
                user_text,
                max_new_tokens=max_words,
                temperature=creativity,
                top_p=0.9,
                do_sample=True,
                num_return_sequences=1
            )

        complete_text = response[0]["generated_text"]

        st.divider()

        st.subheader("📝 Generated Result")

        st.write(complete_text)

st.divider()

st.caption(
    "Powered by Hugging Face Transformers • Built with Streamlit"
)