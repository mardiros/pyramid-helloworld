import importlib.metadata

__version__ = importlib.metadata.version("pyarmid-helloworld")


if __name__ == "__main__":
    print(__version__, end="")
