from fastembed import TextEmbedding

class EmbeddingService:

    def __init__(self):
        self.model = TextEmbedding()

    def generate_embedding(self, text: str) -> list[float]:

        embedding = next(
            self.model.embed([text])
        )

        return embedding.tolist()

embedding_service = EmbeddingService()
