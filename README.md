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

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the Repository**
   - Click the 'Fork' button on the repository page
   - Clone your fork locally

2. **Create a Feature Branch**
   ```bash
   git checkout -b feature/your-feature-name
   ```

3. **Make Your Changes**
   - Write clear, descriptive commit messages
   - Follow the existing code style
   - Add tests if applicable
   - Update documentation as needed

4. **Submit a Pull Request**
   - Push your changes to your fork
   - Create a pull request against the main branch
   - Describe your changes and their purpose
   - Reference any related issues

### Development Setup

1. Install development dependencies:
   ```bash
   pip install -r requirements.txt
   ```

2. Set up your environment:
   ```bash
   cp .env.example .env
   # Edit .env with your API keys
   ```

3. Run tests (if available):
   ```bash
   python -m pytest
   ```

### Code Style

- Follow PEP 8 guidelines for Python code
- Use meaningful variable and function names
- Add comments for complex logic
- Keep functions focused and single-purpose

### Reporting Issues

When reporting issues, please include:
- A clear description of the problem
- Steps to reproduce the issue
- Expected vs actual behavior
- Any relevant error messages
- Your environment details (OS, Python version, etc.)

### Feature Requests

We welcome feature requests! When suggesting new features:
- Explain the problem you're trying to solve
- Describe your proposed solution
- Consider potential impacts on existing functionality 