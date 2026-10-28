import os
from pypdf import PdfReader
from app.services.chunk_service import chunk_text
from app.services.embedding_service import generate_embeddings
from app.services.chroma_service import store_chunks

def extract_pdf_info(pdf_path):

    reader = PdfReader(pdf_path)

    text = ""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text

    chunks = chunk_text(text)
    embeddings = generate_embeddings(chunks)
    store_chunks(chunks, embeddings, os.path.basename(pdf_path))
    return {
        "pages": len(reader.pages),
        "characters": len(text),
        "chunks": len(chunks),
        "embedding_count": len(embeddings),
        "embedding_dimension": len(embeddings[0]),
        "stored_in_chromadb": True
    }