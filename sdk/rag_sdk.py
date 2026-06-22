from layers.rag_layer import (
    RAGLayer
)


class RAGSDK:

    def upload_document(

        self,

        file_path

    ):

        return (

            RAGLayer
            .upload_document(
                file_path
            )
        )

    def ask(

        self,

        question

    ):

        return (

            RAGLayer
            .ask_question(
                question
            )
        )