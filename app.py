#import library for our app 
import streamlit as st
import requests
import time



# Constants for the app
API_KEY = "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"
API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-large" # Replace with your model if using a different one

# CSS for custom styling and animations
st.markdown("""
    <style>
    
    
    /* Button styling and animation */
    .stButton button {
       
        color: white;
        border-radius: 8px;
        border: none;
        padding: 10px 20px;
        font-size: 16px;
        transition: 0.3s;
    }
    .stButton button:hover {
        background-color: #4a4e69;
        transform: scale(1.05);
    }
    
 /* Sidebar styling */
    .css-18e3th9 {
        background-color: #22223b;
        color: white;
    }
    
    /* Add animation to headers */
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    h1, h2 {
        animation: fadeIn 2s ease;
    }
    
    </style>
""", unsafe_allow_html=True)





# Function to generate text using Hugging Face model
def generate_text(prompt, temperature=0.7, max_length=150):
    headers = {"Authorization": f"Bearer {API_KEY}"}
    payload = {
        "inputs": prompt,
        "parameters": {
            "temperature": temperature,
            "max_length": max_length
        },
        "options": {"wait_for_model": True}
    }
    response = requests.post(API_URL, headers=headers, json=payload)
    
    if response.status_code == 200:
        data = response.json()
        if data and isinstance(data, list):
            return data[0]["generated_text"]
        else:
            return "Error: No text generated."
    else:
        return f"Error {response.status_code}: {response.text}"

# Sidebar navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Home", "About", "Contact"])


st.sidebar.subheader("Generation Parameters")
temperature = st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, value=0.7)
max_length = st.sidebar.slider("Max Length", min_value=50, max_value=300, value=150)

# Home Page
if page == "Home":
    st.title("AI-Powered Text Generator")
    
    st.write("Welcome to the AI-powered Text Gernater  Enter a prompt below to get started.")
    
    user_input = st.text_input("Enter your Questions ? :", placeholder="Type something to get started...")
    
    if st.button("Get Answer"):
        if user_input.strip():
            with st.spinner("Generating text..."):
                generated_text = generate_text(user_input)
                time.sleep(1)  # Add slight delay for smooth animation
                st.write("### See 👀The Magic Here:")
                st.write(generated_text)
        else:
            st.write("Please enter a prompt to generate text.")
    
    # Animation for the prompt box
    st.markdown("""
        <style>
        input {
            animation: fadeIn 1s ease-in-out;
        }
        </style>
    """, unsafe_allow_html=True)

# About Page
elif page == "About":
    st.title("About This App")
    st.write("""
        This app is powered by Hugging Face's text generation models to showcase
        the capabilities of AI in generating creative, coherent, and useful content.
        The purpose of this app is to help students and educators generate AI-driven
        content and explore personalized learning applications.
        
        - **Model**: GPT-2 or other Hugging Face models.
        - **Technology Stack**: Python, Streamlit, Hugging Face API.
        - **Features**: Multi-page app, custom styling, text generation, contact form.
    """)
    st.image("https://huggingface.co/front/assets/huggingface_logo.svg", width=200)

# Contact Page
elif page == "Contact":
    st.title("Contact Us")
    st.write("Feel free to reach out with any questions, feedback, or suggestions!")

    # Simple contact form
    with st.form("contact_form"):
        name = st.text_input("Your Name")
        email = st.text_input("Your Email")
        message = st.text_area("Your Message")
        
        submit_button = st.form_submit_button("Submit")
        
        if submit_button:
            if name and email and message:
                st.success("Thank you for reaching out! We’ll get back to you shortly.")
            else:
                st.error("Please fill out all fields in the form.")

# Footer
st.markdown("""
    <hr style="margin-top: 2em; margin-bottom: 2em;">
    <p style="text-align: center;">
        Built with ❤️ by the Streamlit Team | Powered by Hugging Face API
    </p>
    <p style="text-align: center;">
        This AI app is created by <strong>Pro Coder Jii</strong>
    </p>
    
   
""", unsafe_allow_html=True)
