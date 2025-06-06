import nbformat
import os

# Replace with your actual filename
NOTEBOOK_FILE = "SpaceHACK_Team_7_Maps.ipynb"

with open(NOTEBOOK_FILE, "r", encoding="utf-8") as f:
    nb = nbformat.read(f, as_version=4)

# Remove broken widget metadata if present
if "widgets" in nb.metadata:
    del nb.metadata["widgets"]
    print("✅ Removed metadata.widgets from notebook.")

# Save the cleaned notebook (overwrite or create new)
with open(NOTEBOOK_FILE, "w", encoding="utf-8") as f:
    nbformat.write(nb, f)
print(f"🧽 Notebook cleaned and saved: {NOTEBOOK_FILE}")
