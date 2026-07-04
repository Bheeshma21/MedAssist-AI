import os

from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings

DB_PATH = "database/chroma_db"

_embedding = None


def get_embedding():
    global _embedding

    if _embedding is None:
        print("Loading embedding model...")
        _embedding = HuggingFaceEmbeddings(
            model_name="sentence-transformers/all-MiniLM-L6-v2"
        )

    return _embedding


# =====================================================
# Build / Rebuild Vector Database
# =====================================================

def create_vector_db():

    docs = []

    for root, _, files in os.walk("data/medical_docs"):

        for file in files:

            if not file.endswith(".txt"):
                continue

            path = os.path.join(root, file)

            loaded = TextLoader(path, encoding="utf-8").load()

            for doc in loaded:
                doc.metadata["source"] = os.path.relpath(
                    path,
                    "data/medical_docs"
                )

            docs.extend(loaded)

    if not docs:
        print("No medical documents found.")
        return

    Chroma.from_documents(
        documents=docs,
        embedding=get_embedding(),
        persist_directory=DB_PATH
    )

    print(f"Indexed {len(docs)} documents.")


# =====================================================
# Retrieve Medical Context
# =====================================================

def retrieve_medical_context(
    query,
    k=4,
    min_score=0.45
):

    db = Chroma(
        persist_directory=DB_PATH,
        embedding_function=get_embedding()
    )

    results = db.similarity_search_with_relevance_scores(
        query,
        k=k
    )

    context = []
    sources = []

    for doc, score in results:

        # Ignore low relevance documents
        if score < min_score:
            continue

        context.append(doc.page_content)

        source = doc.metadata.get("source", "Unknown")

        if source not in sources:
            sources.append(source)

    medical_context = "\n\n".join(context)

    return {

        "medical_context": medical_context,

        "sources": sources,

        "has_context": len(context) > 0,

        "document_count": len(context)

    }