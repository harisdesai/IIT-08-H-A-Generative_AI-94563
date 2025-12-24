from langchain_openai import OpenAIEmbeddings
import numpy as np

def cosine_similarity(a,b):
    return np.dot(a,b) / (np.linalg.norm(a) * np.linalg.norm(b))

embed_model = OpenAIEmbeddings(
                model="text-embedding-nomic-embed-text-v1.5",
                base_url="http://127.0.0.1:1234/v1",
                api_key="dummy-token",
                check_embedding_ctx_length=False
            )
sentences = [
    "I love Football",
    "Soccer is my favorite sport",
    "Messi is the GOAT"
]

emebeddings  = embed_model.embed_documents(sentences)

for embed_vect in emebeddings :
    print("len",len(embed_vect),"-->", embed_vect[:4])

print("Sentence 1 and 2 similarity",cosine_similarity(emebeddings [0],emebeddings [1]))
print("Sentence 2 and 3 similarity",cosine_similarity(emebeddings [1],emebeddings [2]))