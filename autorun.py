from sentence_transformers import SentenceTransformer
sentences = ["Could you assist me in finding my lost card?",]

model = SentenceTransformer('./')
embeddings = model.encode(sentences)
print(embeddings)