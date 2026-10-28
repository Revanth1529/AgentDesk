import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="knowledge_base"
)


def store_chunks(chunks, embeddings):

    ids = []

    for i in range(len(chunks)):
        ids.append(f"chunk_{i}")

    collection.add(
        ids=ids,
        documents=chunks,
        embeddings=embeddings
    )