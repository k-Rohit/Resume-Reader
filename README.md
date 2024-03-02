# Resume Parser Application

This is a resume parser application built using Streamlit, Spacy, Plotly, and Google Serp API. It helps in identifying the job title, skills, and experience of candidates from their resumes. Additionally, it provides a job search feature based on the job title and location using Google Serp API.

## How to Start

Follow the steps below to set up and run the application:

### 1. Clone the Repository

Clone this repository to your local machine using the following command:

```bash
git clone <repository-url>
```

### 2. Install the dependencies
switch to the main directory
```bash
cd Resume-Reader
pip install -r requirements.txt
```

### 3. Run the application
```bash
streamlit run main.py
```
This code defines a set of functions and configurations for parsing and processing text data from various formats such as PDF, DOCX, and HTML. Below is an explanation of each component:

### Parsing Functions:

1. **parse_pdf(pdf_content):**
   - Uses PyMuPDF (fitz) library to parse text content from a PDF file.
   - It iterates through each page of the PDF document, extracts text, and concatenates it.

2. **extract_text_from_resume(html_content):**
   - Parses HTML content using BeautifulSoup.
   - Extracts text from HTML elements and preprocesses it by removing extra whitespaces.

3. **parse_docx(docx_content):**
   - Utilizes the python-docx library to extract text content from a DOCX file.
   - It reads each paragraph from the document and concatenates them into a single text string.

### Text Processing Functions:

1. **preprocess_text(text):**
   - Removes extra whitespaces from the input text.

2. **process_text(text):**
   - Splits the text into sentences based on full stops.
   - Concatenates the sentences with a newline after each.

### Additional Functionality:

- **extract_sections_with_dates(resume_text):**
  - Identifies sections within the resume text that contain dates.
  - It uses regular expressions to match dates in the format "Month Year" or just "Year".
  - Sections with dates are extracted along with the corresponding date range.

### Visualizations and Configuration:

- **colors:** Defines a dictionary containing colors for different named entities.
- **options:** Configuration for entity visualization using spaCy's `displacy` module.
  - Specifies named entities (e.g., "JOB TITLE", "SKILLS") and their associated colors.

### Libraries Used:

- **PyMuPDF (fitz):** For PDF parsing.
- **BeautifulSoup (bs4):** For HTML parsing.
- **python-docx:** For parsing DOCX files.
- **spacy:** For named entity recognition and visualization.
- **plotly:** For generating interactive visualizations like graphs and charts.

Overall, this code provides a comprehensive set of functions to parse, preprocess, and visualize text data from various document formats, especially tailored for processing resumes or similar documents. It leverages popular libraries in the Python ecosystem to accomplish these tasks efficiently.
