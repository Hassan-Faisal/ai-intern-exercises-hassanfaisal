import numpy as np
from sentence_transformers import SentenceTransformer
from sklearn.metrics.pairwise import cosine_similarity

def run_semantic_search():
    # 1. Load the recommended model [cite: 906, 912]
    model = SentenceTransformer('all-MiniLM-L6-v2')

    # 2. Load documents from documents.txt [cite: 896, 950]
    with open('documents.txt', 'r') as f:
        documents = [line.strip() for line in f.readlines() if line.strip()]

    # 3. Generate embeddings for all documents [cite: 902, 913]
    doc_embeddings = model.encode(documents)

    # 4. Load the 3 test queries [cite: 952]
    with open('queries.txt', 'r') as f:
        queries = [line.strip() for line in f.readlines() if line.strip()]

    # 5. Process each query and find the most relevant document [cite: 914, 922, 932]
    print("--- Semantic Search Results ---")
    with open('results.txt', 'w') as out_file:
        for query in queries:
            query_embedding = model.encode([query])
            
            # Compute cosine similarity between query and all docs [cite: 925, 930]
            similarities = cosine_similarity(query_embedding, doc_embeddings)
            
            # Find the index of the highest score [cite: 934, 937]
            best_idx = np.argmax(similarities)
            best_doc = documents[best_idx]
            
            # Formatting output for results.txt [cite: 939, 954]
            result_str = f"Query: {query}\nRetrieved Document:\n{best_doc}\n\n"
            print(result_str.strip())
            out_file.write(result_str)

if __name__ == "__main__":
    run_semantic_search()