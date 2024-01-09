from langchain import DocumentLoader

# Load documents from a local directory
documents = DocumentLoader.load_documents("path/to/documents")

# Load documents from a remote URL
documents = DocumentLoader.load_documents("https://example.com/documents")

# Load documents from a database or API
documents = DocumentLoader.load_documents_from_database(database_connection)
