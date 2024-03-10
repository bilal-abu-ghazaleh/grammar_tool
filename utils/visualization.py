import streamlit as st


# ---------------------------
def display_fixed_output(modified, editType):
    st.subheader(f"Output Text: {editType}")
    with st.container(border=True):
        # Directly display the differences using Markdown
        st.markdown(modified, unsafe_allow_html=True)
