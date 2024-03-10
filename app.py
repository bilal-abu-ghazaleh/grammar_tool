import streamlit as st
from utils.gpt import run_gpt4_prompt
from utils.visualization import display_fixed_output

# Streamlit UI
st.set_page_config(layout="wide")
st.title('Quality Checker & Editor')

user_input = st.text_area("Enter your text here:", height=300)

# ---------------------------
if st.button('Slightly Correct Text'):
    if user_input:
        # Run GPT grammar
        modified_text = run_gpt4_prompt(f"{user_input}", 'minimal')
        display_fixed_output(modified_text, "Slightly Corrected")
    else:
        st.warning("Please enter some text to analyze.")

if st.button('More Aggressively Correct Text'):
    if user_input:
        # Run GPT grammar
        modified_text = run_gpt4_prompt(f"{user_input}", 'medium')
        display_fixed_output(modified_text, "More Aggressively Corrected")
    else:
        st.warning("Please enter some text to analyze.")