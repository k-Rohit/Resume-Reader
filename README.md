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

### Training statistics - 
We have fine-tuned two models namely roberta-base for Named Entity Extraction and bert-base for generation of job title after getting the skills as keywords in input.
| Model Name    | Training Time | GPU used          | Inference Speed |
|---------------|---------------|-------------------|-----------------|
| roberta-base  | 1 hour        | Tesla-T4 (Colab) | 9.4 seconds     |
| bert-base     | 1 hour        | P-100 (Kaggle)    | 3.2 seconds     |



## utils.py
This files defines a set of functions and configurations for parsing and processing text data from various formats such as PDF, DOCX, and HTML. Below is an explanation of each component:

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

## app.py

This code defines a Streamlit application for parsing and visualizing resume data, as well as performing job searches based on extracted information. Below is an explanation of each component:

### Libraries Used:

- **streamlit:** Framework for building interactive web applications.
- **spacy:** For named entity recognition and visualization.
- **plotly:** For generating interactive visualizations like graphs and charts.
- **pandas:** For data manipulation and analysis.

### Components:

1. **Introduction Page:**
   - Displays a welcome message and an about section in the sidebar.
   - Provides a file uploader to upload resumes in PDF, DOCX, or HTML format.
   - Processes the uploaded file to extract entities (Job Title, Skills, etc.).
   - Visualizes the extracted entities using spaCy's displacy module.

2. **Process Uploaded File:**
   - Parses the uploaded file based on its format (PDF, DOCX, HTML).
   - Utilizes spaCy for named entity recognition on the parsed text.
   - Renders the parsed text and named entities using Streamlit components.

3. **Visualization Page:**
   - Displays visualizations of extracted entities from the resume.
   - Generates a sunburst chart using Plotly Express to visualize entity categories and values.

4. **Search Jobs Page:**
   - Allows users to search for job opportunities based on extracted skills or job titles.
   - Users can enter a query (job title or keyword) and location for the job search.
   - Performs a job search using predefined functions from the 'jobs' module.
   - Logs the job search event.

### Logging:

- **File Logging:** Logs events such as resume upload, entity extraction, visualization, and job searches to a log file named 'resume_parser.log'.
- Provides information about the time taken for model loading and inference.

## Video Demonstration

[Watch the Video](https://github.com/k-Rohit/Resume-Reader/assets/93335681/d9747b68-4030-4757-9083-33b2a1a61383.mp4)









