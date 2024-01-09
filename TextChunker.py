from langchain import TextChunker

chunker = TextChunker()

# Split documents into paragraphs
paragraphs = chunker.chunk_into_paragraphs(documents)

# Split paragraphs into sentences
sentences = chunker.chunk_into_sentences(paragraphs)

# Split documents into fixed-size chunks
chunk_size = 1000  # Specify the desired chunk size in words
fixed_size_chunks = chunker.chunk_into_fixed_size(documents, chunk_size)
