# DocuMind — AI-Powered Document Question Answering System

DocuMind is an AI-powered document question-answering application that enables users to upload PDF documents and ask questions about their content using natural language. It uses Retrieval-Augmented Generation (RAG) to retrieve relevant information from documents and generate context-aware answers with source references.

Built using Python, FastAPI, Streamlit, ChromaDB, Sentence Transformers, and Google's Gemini API, DocuMind combines semantic search with large language models to make document exploration more efficient and accessible.

## Table of Contents

* [Overview](#overview)
* [Key Features](#key-features)
* [How It Works](#how-it-works)
* [Technology Stack](#technology-stack)
* [Project Structure](#project-structure)
* [Getting Started](#getting-started)
* [Usage](#usage)
* [API Documentation](#api-documentation)
* [Example Use Cases](#example-use-cases)
* [AI-Assisted Development](#ai-assisted-development)
* [Limitations](#limitations)
* [Future Improvements](#future-improvements)
* [Security Considerations](#security-considerations)
* [Contributing](#contributing)
* [License](#license)
* [Author](#author)

## Overview

Finding specific information in lengthy PDF documents can be time-consuming. Traditional keyword-based searches may fail to identify relevant information when a user's question differs from the wording used in the original document.

DocuMind addresses this challenge through Retrieval-Augmented Generation.

The application processes uploaded PDF documents, divides their content into smaller text chunks, generates vector embeddings, and stores them in a vector database. When a user asks a question, the system retrieves relevant passages and supplies them as context to a large language model to generate an answer.

The application also uses document metadata to help users identify the sources associated with retrieved information.

## Key Features

* **PDF Document Processing:** Extract text from uploaded PDF documents.
* **Natural Language Question Answering:** Ask questions about document content using everyday language.
* **Retrieval-Augmented Generation:** Retrieve relevant document passages before generating answers.
* **Semantic Search:** Identify relevant content using vector embeddings rather than relying exclusively on exact keyword matches.
* **Vector Database Integration:** Store and retrieve document embeddings using ChromaDB.
* **Source References:** Use document filenames and page metadata to help users locate relevant information.
* **LLM Integration:** Generate context-aware responses using Google's Gemini API.
* **Interactive User Interface:** Upload documents and interact with the application through Streamlit.
* **REST API:** Expose backend functionality through FastAPI.
* **Modular Architecture:** Separate the frontend, backend, and RAG processing logic.

## How It Works

DocuMind follows a Retrieval-Augmented Generation pipeline.

```text
                 PDF Document
                       |
                       v
               Text Extraction
                       |
                       v
                 Text Chunking
                       |
                       v
              Embedding Generation
                       |
                       v
              Store in ChromaDB
                       |
                       v
                User's Question
                       |
                       v
             Semantic Retrieval
                       |
                       v
            Retrieve Relevant Chunks
                       |
                       v
           Context + Question to Gemini
                       |
                       v
              Generate an Answer
                       |
                       v
            Answer with Source References
```

### 1. Document Ingestion

The application accepts PDF documents and extracts their text using PyMuPDF.

### 2. Text Chunking

The extracted text is divided into smaller, overlapping chunks to support efficient retrieval while preserving relevant context.

### 3. Embedding Generation

Sentence Transformers converts text chunks into vector embeddings that represent their semantic meaning.

### 4. Vector Storage

The embeddings and associated metadata are stored in ChromaDB.

### 5. Semantic Retrieval

When a user submits a question, the system retrieves relevant document chunks using vector similarity search.

### 6. Answer Generation

The retrieved passages and the user's question are passed to Google's Gemini API to generate an answer based on the supplied context.

### 7. Source References

Document metadata, including filenames and page numbers, can be used to help users identify the source passages associated with retrieved information.

## Technology Stack

| Technology            | Purpose                              |
| --------------------- | ------------------------------------ |
| Python                | Core programming language            |
| FastAPI               | Backend REST API                     |
| Streamlit             | Interactive frontend                 |
| PyMuPDF               | PDF text extraction                  |
| Sentence Transformers | Text embedding generation            |
| ChromaDB              | Vector storage and similarity search |
| Google Gemini API     | Context-aware answer generation      |
| Uvicorn               | ASGI server for running FastAPI      |
| Git                   | Version control                      |
| GitHub                | Source code hosting                  |

## Project Structure

```text
DocuMind/
|
├── app.py                 # Streamlit frontend
├── main.py                # FastAPI backend
├── rag.py                 # RAG pipeline and document processing
├── requirements.txt       # Python dependencies
├── README.md              # Project documentation
└── .gitignore             # Files excluded from version control
```

This structure describes the primary application files. Additional files or directories may exist in the repository.

## Getting Started

Follow the steps below to set up DocuMind locally.

### Prerequisites

Before starting, ensure that you have:

* Python installed in a version compatible with the project dependencies.
* Git installed on your system.
* A Google Gemini API key.
* An internet connection for accessing the Gemini API and installing dependencies.

### 1. Clone the Repository

```bash
git clone https://github.com/adarshk-ops/DocuMind.git
```

Navigate to the project directory:

```bash
cd DocuMind
```

### 2. Create a Virtual Environment

On Windows:

```bash
python -m venv venv
```

Activate the environment using Command Prompt:

```cmd
venv\Scripts\activate
```

On macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

If `requirements.txt` is present in the repository, install the dependencies using:

```bash
pip install -r requirements.txt
```

If the file is missing, create it using the actual dependencies required by the application before proceeding.

### 4. Configure Environment Variables

Create a `.env` file in the project root if the application uses environment variables for configuration.

For example:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Replace the placeholder with your actual API key.

The variable name must match the name expected by your application code.

Keep API keys and other secrets out of your source code and public repositories. Ensure that `.env` is included in `.gitignore`.

### 5. Start the Backend

From the project root, run:

```bash
uvicorn main:app --reload
```

The backend should be available at:

```text
http://127.0.0.1:8000
```

FastAPI's interactive API documentation is generally available at:

```text
http://127.0.0.1:8000/docs
```

These commands assume that the FastAPI application instance is defined in `main.py` and uses the standard Uvicorn configuration.

### 6. Start the Frontend

Open a second terminal, activate the virtual environment, and run:

```bash
streamlit run app.py
```

Open the local URL displayed in the terminal to access the application.

If the frontend communicates with the FastAPI backend, ensure that its configured backend URL matches the address where the backend is running.

**Note:** Verify the dependency list, environment-variable names, and startup commands against the current source code before publishing the README.

## Usage

After starting the application:

1. Open the Streamlit interface in your browser.
2. Upload a PDF document.
3. Allow the application to extract and process the document.
4. Enter a question related to the uploaded content.
5. Review the generated answer.
6. Examine the available source references to locate relevant information in the original document.

For better results, ask clear and specific questions related to the uploaded document.

Answer quality depends on the document's content, retrieval effectiveness, and the language model's interpretation of the supplied context.

## API Documentation

DocuMind uses FastAPI to expose backend functionality.

The available endpoints are defined in `main.py`.

To explore the actual endpoints, request formats, and response schemas, start the backend and visit:

**API Documentation:** http://127.0.0.1:8000/docs

The interactive documentation is generated from the routes registered in the FastAPI application.

## Example Use Cases

### Academic Learning

Upload textbooks, lecture notes, and study materials to find explanations of specific concepts.

### Research Assistance

Retrieve relevant information from research papers and technical publications.

### Technical Documentation

Ask questions about software documentation, technical manuals, and engineering guides.

### Business Documents

Search reports, policies, and other text-based PDF documents for relevant information.

### Exam Preparation

Use academic materials to review definitions, concepts, and explanations before examinations.

These are potential use cases for the application, rather than claims that every specialized workflow has been implemented.

## AI-Assisted Development

AI tools were used during the development of DocuMind to assist with project structuring, code review, debugging, testing, and monitoring application behavior.

AI assistance helped identify potential issues, improve code organization, evaluate implementation approaches, and streamline the development workflow.

AI-generated suggestions were reviewed and incorporated where appropriate as part of the iterative development process.

The project combines AI-assisted development practices with the implementation of document processing, semantic retrieval, backend APIs, and LLM integration.

## Limitations

DocuMind is an AI-powered document question-answering application. Its responses should be checked against the original documents when accuracy is important.

Potential limitations include:

* Relevant information may not always be retrieved.
* Answers may be incomplete when the retrieved context is insufficient.
* Language models can generate inaccurate or unsupported statements.
* Source references must be verified to ensure they support the corresponding answers.
* Scanned PDFs may require OCR if their text cannot be extracted directly.
* Large documents may require additional processing time and computational resources.
* Gemini API access may be subject to usage limits, availability constraints, and pricing.
* Retrieval quality depends on document structure, chunking, embeddings, and search configuration.

Retrieval-Augmented Generation can help ground responses in document content, but it does not guarantee factual accuracy.

## Future Improvements

Potential enhancements include:

* Improved document indexing and replacement handling.
* Document deletion and lifecycle management.
* Better retrieval strategies and configurable similarity thresholds.
* Hybrid search combining semantic retrieval with keyword search.
* Reranking of retrieved passages.
* Clickable citations with PDF page navigation.
* Highlighting relevant passages in source documents.
* Improved handling of questions that cannot be answered from the available context.
* Persistent, session-specific conversation history.
* Automated tests for document processing, retrieval, and answer generation.
* Evaluation of retrieval quality, answer correctness, and citation accuracy.
* Improved error handling and application logging.
* Docker-based deployment.
* Enhanced interface design and document previews.

These items are proposed improvements and should not be interpreted as existing features unless they have been implemented.

## Security Considerations

When running or deploying DocuMind:

* Keep API keys and other secrets outside version control.
* Exclude environment files and sensitive local data using `.gitignore`.
* Validate uploaded files before processing them.
* Enforce appropriate file-size and resource limits.
* Handle malformed or corrupted documents safely.
* Avoid exposing internal file paths through public endpoints.
* Implement session isolation and access controls before supporting multiple users.
* Review the privacy implications of sending document content to an external language-model API.

Avoid uploading confidential or sensitive documents unless the application's data-handling and privacy requirements have been evaluated.

## Contributing

Contributions, suggestions, and bug reports are welcome.

To propose a change:

1. Fork the repository.
2. Create a separate branch for your changes.
3. Implement and test the improvement.
4. Submit a pull request explaining the changes.

For bug reports, include the steps to reproduce the issue, the expected behavior, and the observed behavior.

## License

The applicable license should be specified here.

If the repository does not already contain a license, select an appropriate open-source license before publishing one. Until a license is added, do not assume that the project is distributed under an open-source license.

## Author

**PARTHA**

GitHub: https://github.com/adarshk-ops

Project Repository: https://github.com/adarshk-ops/DocuMind
