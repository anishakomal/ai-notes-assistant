# import chromadb

# client = chromadb.Client()

# collection = client.create_collection(
#     name="notes_collection"
# )

import chromadb

client = chromadb.PersistentClient(path="./chroma_db")

collection = client.get_or_create_collection(
    name="notes_collection"
)