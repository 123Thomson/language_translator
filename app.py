import streamlit as st
from googletrans import Translator, LANGUAGES

# Initialize Google Translator
translator = Translator()

# Function to get language code from language name
def get_language_code(language_name):
    language_name = language_name.lower().capitalize()  # Capitalize the first letter
    for lang_code, lang_name in LANGUAGES.items():
        if lang_name.lower() == language_name.lower():
            return lang_code
    return None

# Supported languages (including Malayalam, Hindi, Tamil, etc.)
SUPPORTED_LANGUAGES = {
    "English": "en",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Italian": "it",
    "Hindi": "hi",
    "Malayalam": "ml",
    "Tamil": "ta"
}

# Custom CSS for new styling
st.markdown("""
    <style>
    body {
        background-color: #E8F4F8;
        font-family: 'Arial', sans-serif;
    }
    .stTextInput, .stTextArea, .stButton {
        font-size: 14px !important;
    }
    h1, h2, h3, p {
        text-align: left;
        color: #005A9C;
    }
    .stButton > button {
        background-color: #FF5733;
        color: white;
        font-size: 16px;
        padding: 8px 20px;
        border: none;
        border-radius: 4px;
        transition: background-color 0.3s;
    }
    .stButton > button:hover {
        background-color: #FF4519;
    }
    .stTextInput input, .stTextArea textarea {
        border-radius: 8px;
        border: 1.5px solid #FF5733;
    }
    .stTextArea textarea {
        height: 100px;
    }
    </style>
    """, unsafe_allow_html=True)

# Streamlit UI with updated formatting
st.title("🌍 Multi-language Translator")
st.subheader("Translate between different languages effortlessly.")

# Input text
source_text = st.text_area("Enter the text to be translated:", "", height=150)

# Automatically identify the source language
detected_lang = ""
if source_text:
    detected_lang = translator.detect(source_text).lang
    source_lang_name = LANGUAGES[detected_lang].capitalize()
    st.write(f"Detected Source Language: **{source_lang_name}**")

# Target language selection (dropdown)
target_language = st.selectbox("Select target language:", list(SUPPORTED_LANGUAGES.keys()))

# Translate button
if st.button("Translate"):
    target_lang_code = SUPPORTED_LANGUAGES[target_language]

    try:
        # Using googletrans for translation
        translated_text = translator.translate(source_text, src=detected_lang, dest=target_lang_code).text
        st.success(f"**Translated Text**: {translated_text}")
    except Exception as e:
        st.error(f"⚠ Error during translation: {str(e)}")

# Display supported languages with alternate layout
if st.checkbox("View supported languages"):
    st.write("Available languages for translation:")
    st.write(", ".join(SUPPORTED_LANGUAGES.keys()))

# Footer with alternate styling
st.markdown("""
    <div style="text-align: center; padding-top: 20px; font-size: 12px; color: #606060;">
        Language translation app powered by Streamlit & Google Translate API.
    </div>
    """, unsafe_allow_html=True)
