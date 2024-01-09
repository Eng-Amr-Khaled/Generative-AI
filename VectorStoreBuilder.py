from langchain import VectorStoreBuilder

vector_store_builder = VectorStoreBuilder()

# Build a vector store from word embeddings
word_vector_store = vector_store_builder.build_vector_store(word_embeddings)

# Build a vector store from sentence embeddings
sentence_vector_store = vector_store_builder.build_vector_store(sentence_embeddings)
