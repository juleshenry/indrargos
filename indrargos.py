from surrealdb import Surreal
from surreal_langchain import SurrealDBStore
from langchain.embeddings import HuggingFaceEmbeddings

async def delete_docs():
    async with Surreal("ws://localhost:8000/rpc") as db:
        await db.signin({"user": "root", "pass": "root"})
        await db.use("langchain", "database")
        await db.delete("documents")

await delete_docs()

embeddings = HuggingFaceEmbeddings()
sdb = SurrealDBStore(
    dburl="ws://localhost:8000/rpc",  # url for the hosted SurrealDB database
    embedding_function=embeddings,
    db_user="root",  # SurrealDB credentials if needed: db username
    db_pass="root",  # SurrealDB credentials if needed: db password
    # ns="langchain", # namespace to use for vectorstore
    # db="database",  # database to use for vectorstore
    # collection="documents", #collection to use for vectorstore
)
await sdb.initialize()
sdb = await SurrealDBStore.afrom_texts(
    dburl="ws://localhost:8000/rpc",
    texts=sentences,db_user="root",db_pass="root",
    embedding=embeddings,
)
await sdb.asimilarity_search("What is Langchain?")
embeddings = HuggingFaceEmbeddings().embed_query("What is Langchain?")
await sdb.asimilarity_search_by_vector(embeddings,k=4)

await sdb.asimilarity_search_with_score("What is Langchain?",k=10,score_threshold=0.6)
await sdb.asimilarity_search_with_relevance_scores("What is Langchain?",score_threshold=0.5)

class Indrargos:

    def __init__(self, url):
        self.url = url