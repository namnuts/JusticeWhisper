import faiss
import pickle
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity
import argparse

parser = argparse.ArgumentParser(description="Search FAISS index for relevant transcript chunks.")
parser.add_argument("query", type=str, help="The question to query the transcript.")
args = parser.parse_args()
query = args.query

VECTORSTORE_FOLDER = "vectorstore"

index = faiss.read_index(f"{VECTORSTORE_FOLDER}/index.faiss")

with open(f"{VECTORSTORE_FOLDER}/metadata.pkl", "rb") as f:
    chunks, metadatas = pickle.load(f)

embed_model = SentenceTransformer("all-MiniLM-L6-v2")

query_embedding = embed_model.encode([query])

k = 6
D, I = index.search(query_embedding, k)

print(f"\n🔎 Query: {query}\n")

retrieved_docs = []

for rank, idx in enumerate(I[0]):
    chunk_text = chunks[idx]
    print(f"🔹 Result {rank + 1} (Source: {metadatas[idx]['source']})\n")
    print(chunk_text[:500], "...\n")
    retrieved_docs.append(chunk_text)

with open("retrieved_chunks.txt", "w", encoding="utf-8") as f:
    f.write("\n\n---\n\n".join(retrieved_docs))

print("\n✅ Retrieved chunks saved to 'retrieved_chunks.txt'")
