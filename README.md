# PDF Highlighter with Text Layer

A web application that allows users to upload PDF documents, ask questions about their content, and receive highlighted versions with relevant text sections. The application uses AI to identify relevant paragraphs and provides an interactive PDF viewer with text layer support.

## Features

- PDF upload and processing
- AI-powered text relevance analysis using Claude 3.7 Sonnet
- Interactive PDF viewer with text layer support
- Real-time text highlighting
- Cross-origin resource sharing (CORS) enabled
- Temporary file management for secure processing

## Prerequisites

- Python 3.x
- Anthropic API key (for Claude AI integration)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/bigbrainw/pdf_tools.git
cd pdf_tool
```

2. Install the required dependencies:
```bash
pip install flask flask-cors PyMuPDF anthropic python-dotenv
```

3. Create a `.env` file in the project root and add your Anthropic API key:
```
ANTHROPIC_API_KEY=your_api_key_here
```

## Usage

1. Start the Flask server:
```bash
python app.py
```

2. Open your web browser and navigate to `http://localhost:5000`

3. Upload a PDF file and enter your question about its content

4. The application will:
   - Process the PDF
   - Analyze the content using AI
   - Return a highlighted version with relevant text sections
   - Display the PDF in an interactive viewer

## Technical Details

- **Backend**: Flask server with CORS support
- **Frontend**: HTML/JavaScript with PDF.js for rendering
- **PDF Processing**: PyMuPDF (fitz) for PDF manipulation
- **AI Integration**: Anthropic's Claude 3.7 Sonnet for text analysis
- **File Handling**: Secure temporary file storage

## Security Notes

- The application uses secure filename handling
- Files are stored in a temporary directory
- CORS is enabled for development purposes (configure appropriately for production)

## License

[Add your license information here]

## Contributing

[Add contribution guidelines here] 