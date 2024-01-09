import spacy

nlp = spacy.load("en_core_web_md")  # Load pre-trained word embeddings

# Generate word embeddings for individual words
def generate_word_embeddings(text_chunks):
    embeddings = []
    for chunk in text_chunks:
        doc = nlp(chunk)
        chunk_embeddings = [token.vector for token in doc]
        embeddings.append(chunk_embeddings)
    return embeddings

# Generate sentence embeddings for text chunks
def generate_sentence_embeddings(text_chunks):
    embeddings = []
    for chunk in text_chunks:
        doc = nlp(chunk)
        chunk_embedding = doc.vector
        embeddings.append(chunk_embedding)
    return embeddings

# Generate word embeddings for text chunks
word_embeddings = generate_word_embeddings(text_chunks)

# Generate sentence embeddings for text chunks
sentence_embeddings = generate_sentence_embeddings(text_chunks)
