import nbformat

files = ["System1.ipynb", "System2.ipynb", "System3.ipynb"]

for f in files:
    nb = nbformat.read(f, as_version=4)

    # Remove widget metadata if present
    if "widgets" in nb.get("metadata", {}):
        del nb["metadata"]["widgets"]

    nbformat.write(nb, f)

print("Fixed widget metadata in notebooks")