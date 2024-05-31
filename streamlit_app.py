import streamlit as st

# Initialize session state for the list of phrases
if 'phrases' not in st.session_state:
    st.session_state.phrases = ["apple", "banana", "cherry"]

def sort_phrases():
    st.session_state.phrases.sort()

st.title("Phrase Editor")

st.write("Edit the list of phrases below (separate phrases with commas):")

# Input field to edit the phrases
phrases_input = st.text_area("Phrases", value=", ".join(st.session_state.phrases))
st.session_state.phrases = [phrase.strip() for phrase in phrases_input.split(",")]

# Sort button
if st.button("Sort Phrases"):
    sort_phrases()

st.write("Updated list of phrases:")
st.write(st.session_state.phrases)
