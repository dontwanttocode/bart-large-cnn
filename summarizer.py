import streamlit as st
from transformers import pipeline

pipe = pipeline("summarization", model="ainize/bart-base-cnn")

def summarize_text(input_text):
    summary = pipe(input_text,do_sample = False)
    return summary[0]["summary_text"]

st.set_page_config(page_title = "✍️ Summarizer")
st.title("📚Text Summarization Tool")
input_text = st.text_area("Enter the text you want to summarize:", height = 200)

if st.button("📄Summarize"):
    if input_text:
        with st.spinner("Generating summary..."):
            summary = summarize_text(input_text)
        st.subheader("Summary: ")
        st.write(summary)
    else:
        st.warning("Please enter some text to summarize.")

st.sidebar.header("About")
st.sidebar.info(
    "This summarizer uses the BART model (facebook/bart-large-cnn) "
    "fine-tuned on the CNN Daily Mail dataset making it particularly "
    "effective for summarizing news articles and similar content."
)

sample_text = '''The Eiffel Tower is a wrought-iron lattice tower on the Champ de Mars in Paris, France. 
It is named after the engineer Gustave Eiffel, whose company designed and built the tower. 
Constructed from 1887 to 1889 as the entrance arch to the 1889 World's Fair, it was initially 
criticized by some of France's leading artists and intellectuals for its design, but it has 
become a global cultural icon of France and one of the most recognizable structures in the world. 
The Eiffel Tower is the most-visited paid monument in the world; 6.91 million people ascended it in 2015. 
The tower is 324 metres (1,063 ft) tall, about the same height as an 81-storey building, and the tallest 
structure in Paris. Its base is square, measuring 125 metres (410 ft) on each side.'''

if st.sidebar.button("Try Sample Text"):
    st.text_area("Summarized sample text:", value=sample_text, height=200)