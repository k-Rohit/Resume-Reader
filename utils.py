import fitz  # PyMuPDF
import docx
import io
from spacy import displacy
from bs4 import BeautifulSoup
from IPython.display import display
import plotly.express as px
import pandas as pd
import spacy
import plotly.graph_objects as go

# Function to parse PDF
def parse_pdf(pdf_content):
    text = ""
    pdf_document = fitz.open(stream=pdf_content, filetype="pdf")
    for page_num in range(len(pdf_document)):
        page = pdf_document.load_page(page_num)
        text += page.get_text()
    return text

# Functions to parse HTML
def preprocess_text(text):
    # Remove extra whitespaces
    text = ' '.join(text.split())
    return text

def extract_text_from_resume(html_content):
    # Parse HTML content
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Extract text from all elements
    text = soup.get_text(separator='\n')
    
    return preprocess_text(text)


def process_text(text):
    # Split the text into sentences based on full stops
    sentences = text.split('. ')
    
    # Concatenate the sentences with a newline after each
    processed_text = '\n'.join(sentences)
    
    return processed_text

# Function to parse DOCX
def parse_docx(docx_content):
    doc = docx.Document(io.BytesIO(docx_content))
    text = ""
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text


colors = {
    "SKILL": "linear-gradient(90deg, #aa9cfc, #fc9ce7)",
    "EDUC": "linear-gradient(90deg, #9BE15D, #00E3AE)",
    "ORG": "#ffd966",
    "EXPERIENCE": "#9fc5e8",

}
options = {
    "ents": [
        "SKILL",
        "ORG",
        "EDUC",
        "EXPERIENCE"
    ],
    "colors": colors,
}