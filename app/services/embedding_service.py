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























# import hashlib
# import random


# class EmbeddingService:

#     @staticmethod
#     def generate_embedding(text: str) -> list[float]:
#         seed = int(
#             hashlib.md5(text.encode()).hexdigest(),
#             16
#         )

#         random.seed(seed)

#         return [
#             random.random()
#             for _ in range(384)
#         ]


# embedding_service = EmbeddingService()