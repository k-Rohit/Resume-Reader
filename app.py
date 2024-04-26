
import streamlit as st
import spacy
from spacy import displacy
import plotly.express as px
from utils import parse_pdf, parse_docx, extract_text_from_resume, process_text, options
import pandas as pd
import logging
import time

# Configure logger
logging.basicConfig(filename='resume_parser.log', level=logging.INFO, 
                    format='%(asctime)s - %(levelname)s - %(message)s')

# Load English language model for Spacy
start_time_load = time.time()  # Start time for model loading
nlp = spacy.load("model-best-with-job-titles")
end_time_load = time.time()    # End time for model loading
logging.info(f"Model loaded in {end_time_load - start_time_load:.2f} seconds.")

# Define function for the introduction page
def intro():
    st.title("Resume Parser Application")
    st.write("Welcome to the Resume Parser App!")
    st.sidebar.title("About")
    st.sidebar.info(
        '''
        This is a resume parser application that identifies the Job Title, Skills, 
        Experience of the candidates.
        "Upload your resume in PDF, DOCX, or HTML format, and explore the extracted information
        '''
    )

    # File uploader
    uploaded_file = st.file_uploader("Upload your resume", type=['pdf', 'docx', 'html'])

    # Log file upload event
    logging.info("Resume uploaded successfully.")

    # Process the uploaded file
    if uploaded_file is not None:
        st.success("File uploaded successfully!")
        entities = process_uploaded_file(uploaded_file)
        visualization(entities)
    else:
        st.warning("No file uploaded")

# Function to process the uploaded file
def process_uploaded_file(uploaded_file):
    entities = []
    if uploaded_file is not None:
        file_content = uploaded_file.read()
        filename = uploaded_file.name

        if filename.endswith('.pdf'):
            text = parse_pdf(file_content)
        elif filename.endswith('.html'):
            text = extract_text_from_resume(file_content)
            text = process_text(text)
        elif filename.endswith('.docx'):
            text = parse_docx(file_content)
        else:
            st.error("Unsupported file format")
            return entities

        # Process text using Spacy
        start_time_inference = time.time()  # Start time for inference
        doc = nlp(text)
        end_time_inference = time.time()    # End time for inference
        logging.info(f"Inference completed in {end_time_inference - start_time_inference:.2f} seconds.")

        for ent in doc.ents:
            entities.append((ent.text, ent.label_))

        st.subheader("Resume Text")
        st.write(doc.text)  # Print the parsed text
        
        # Render entities using displacy
        st.subheader("Named Entity Recognition")
        html = displacy.render(doc, style="ent", page=True, options=options)
        st.write(html, unsafe_allow_html=True)

        # Log entity extraction event
        logging.info("Entities extracted successfully.")
    else:
        st.warning("No file uploaded")
    return entities

# Define function for visualization page
def visualization(entities):
    st.title("Resume Visualization")
    st.subheader("Resume Sunburst")
    data = [{'Category': entity[1], 'Value': entity[0]} for entity in entities]
    df = pd.DataFrame(data)
    fig = px.sunburst(df, path=['Category', 'Value'])
    
    # Change the color of the sunburst
    fig.update_traces(marker=dict(colors=px.colors.qualitative.Light24))
    
    # Change the size of the sunburst
    fig.update_layout(margin=dict(t=0, l=0, r=0, b=0))
    
    fig.update_layout(title="Resume Sunburst")
    st.plotly_chart(fig)

    # Log visualization event
    logging.info("Resume visualization generated successfully.")

# Define main function to manage page navigation
def main():
    # Add a selectbox to choose the page
    page = st.sidebar.selectbox("Select a page", ["Introduction"])

    # Render the selected page
    if page == "Introduction":
        intro()

if __name__ == "__main__":
    main()
