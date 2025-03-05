# Load the document to read it in its entirety for a comprehensive summary.
file_path = "/mnt/data/Microsoft_Activision_-_Provisional_Findings_Report_3.pdf"
import PyPDF2

# Read the PDF file
pdf_reader = PyPDF2.PdfFileReader(file_path)

# Extract text from each page
text = ""
for page_num in range(pdf_reader.getNumPages()):
    page = pdf_reader.getPage(page_num)
    text += page.extract_text()

# Display the total length of the extracted text to understand the document's size
len(text)
