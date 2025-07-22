This project implements a semantic search system using a subset of Wikipedia as the knowledge base. Wikipedia articles are embedded using GTE or E5 sentence transformers, then indexed into a FAISS vector store for efficient similarity search. 
Users can input natural language queries and retrieve the most relevant Wikipedia passages based on semantic similarity, not just keyword matching. The code assumes that a Wikipedia dump has been downloaded at https://dumps.wikimedia.org/dawiki/latest/.

Features:
- Uses either GTE for general purpose embeddings or E5 for multilingual, high-quality sentence embeddings

- Fast and scalable FAISS vector index for similarity search

- Supports flexible retrieval from Wikipedia-based corpora

- Modular setup for swapping in different embedding models

Tech Stack
- FAISS for vector indexing

- GTE / E5 sentence transformers via Hugging Face

- Python for preprocessing and querying

- Subset of Wikipedia dump as the corpus (knowledge base)

Use Cases
- Semantic question answering

- Information retrieval research

- Multilingual or domain-specific RAG systems
