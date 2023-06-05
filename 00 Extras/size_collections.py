import sys


def size_collections():
    collections = {
        "list": list(),
        "tuple": tuple(),
        "dict": dict(),
        "set": set(),
    }
    for name, value in collections.items():
        print(f"{name} = {sys.getsizeof(value)} bytes")


if __name__ == "__main__":
    size_collections()
