import importlib.metadata

__version__ = importlib.metadata.version("pyramid-helloworld")


if __name__ == "__main__":
    print(__version__, end="")
