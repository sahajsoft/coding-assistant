import weaviate
import weaviate.classes.config as wc
import weaviate.classes as wvc
import sys


def local_client():
    return weaviate.connect_to_local()


def create_or_get_collection(collection_name: str = "test"):
    client = local_client()
    if not client.collections.exists(name = 'test'):
        client.collections.create(name = 'test')
    collection = client.collections.get('test')
    return collection

def apply_embeddings(embedding_function: callable, embedding_model: str, nodes: list[str]):
    embeddings = []
    for i, value in enumerate(nodes):
        res = embedding_function(value, embedding_model)
        if res is not None:
            embedding_i = wvc.data.DataObject(
                properties={
                    'message': value,
                },
                vector=list(res)
            )
            embeddings.append(embedding_i)
        # Print the loading percentage
        print(f"\rLoading... {(i+1)*100/len(nodes)}%", end="")
        # Flush the output buffer to ensure the text is printed immediately
        sys.stdout.flush()
    return embeddings