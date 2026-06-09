from services.vector_service import (
    VectorService
)

from services.rag_service import (
    RAGService
)


class RAGLayer:

    @staticmethod
    def ask(question):

        try:

            db = VectorService.load_db()

            docs = db.similarity_search_with_score(
                question,
                k=4
            )

            print("DOC COUNT:", len(docs))

            context = "\n\n".join(
                doc.page_content
                for doc, score in docs
            )

            answer = RAGService.generate_answer(
                question,
                context
            )

            similarities = []

            for doc, score in docs:

                similarity = max(
                    0,
                    round(
                        1 / (1 + float(score)),
                        2
                    )
                )

                similarities.append(similarity)
            print(similarities)

            if len(similarities) == 0:
                avg_similarity = 0
            else:
                avg_similarity = round(
                    sum(similarities) /
                    len(similarities),
                    2
                )
            print(avg_similarity)
            sources = []

            for doc, score in docs:

                sources.append({
                    "page": doc.metadata.get(
                        "page",
                        "unknown"
                    )
                })
            evidence = []

            for doc, score in docs:

                evidence.append({

                    "page":
                        doc.metadata.get(
                            "page",
                            "unknown"
                        ),

                    "snippet":
                        doc.page_content[:200]
                })

            return {
                "answer": answer,
                "confidence": avg_similarity,
                "sources": sources,
                "evidence": evidence,
                "confidence_reason":
                    f"Average retrieval similarity: {avg_similarity}"
            }

        except Exception as e:

            import traceback

            print("\nRAG ERROR:")
            traceback.print_exc()

            raise e