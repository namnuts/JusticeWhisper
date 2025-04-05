import os
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from langchain.text_splitter import RecursiveCharacterTextSplitter

TRANSCRIPTS_FOLDER = "transcripts"
VECTORSTORE_FOLDER = "vectorstore"
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

embed_model = SentenceTransformer("all-MiniLM-L6-v2")
splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)

all_chunks = []
metadata_list = []

for fname in os.listdir(TRANSCRIPTS_FOLDER):
    if fname.endswith(".txt"):
        file_path = os.path.join(TRANSCRIPTS_FOLDER, fname)
        with open(file_path, "r", encoding="utf-8") as f:
            full_text = f.read()
            chunks = splitter.split_text(full_text)
            all_chunks.extend(chunks)
            metadata_list.extend([{"source": fname}] * len(chunks))

print(f"🔍 Total chunks: {len(all_chunks)}")

embeddings = embed_model.encode(all_chunks)

dimension = embeddings[0].shape[0]
faiss_index = faiss.IndexFlatL2(dimension)
faiss_index.add(embeddings)

os.makedirs(VECTORSTORE_FOLDER, exist_ok=True)
faiss.write_index(faiss_index, os.path.join(VECTORSTORE_FOLDER, "index.faiss"))

with open(os.path.join(VECTORSTORE_FOLDER, "metadata.pkl"), "wb") as f:
    pickle.dump((all_chunks, metadata_list), f)

print("✅ Embeddings saved in FAISS vectorstore!")
