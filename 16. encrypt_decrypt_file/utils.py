import os


def create_path(path, filename):
    return os.path.join(os.path.dirname(path), filename)
