from langchain_huggingface import (
    HuggingFaceEmbeddings
)

from langchain_community.vectorstores import (
    FAISS
)


class VectorService:

    VECTOR_FOLDER = "vectorstore"

    embedding_model = (
        HuggingFaceEmbeddings(
            model_name=
            "sentence-transformers/all-MiniLM-L6-v2"
        )
    )

    @staticmethod
    def load_db():

        return FAISS.load_local(

            VectorService.VECTOR_FOLDER,

            VectorService.embedding_model,

            allow_dangerous_deserialization=True
        )