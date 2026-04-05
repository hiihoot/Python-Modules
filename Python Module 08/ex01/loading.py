import importlib
import sys

try:
    pandas = importlib.import_module("pandas")
    requests = importlib.import_module("requests")
    matplotlib = importlib.import_module("matplotlib")

    print(pandas)

except ModuleNotFoundError:
    pass