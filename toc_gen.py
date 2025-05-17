import os

# Directorio raíz (el mismo donde está este script)
ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(ROOT_DIR, "table-of-content.md")
EXCLUDE = ["__pycache__", ".git", ".DS_Store", "node_modules"]
INDENT = "  "

def is_valid_file(filename):
    return not filename.startswith(".") and filename.endswith(".md")

def build_markdown_toc(path, depth=0):
    toc = ""
    entries = sorted(os.listdir(path))
    for entry in entries:
        full_path = os.path.join(path, entry)
        if entry in EXCLUDE:
            continue
        if os.path.isdir(full_path):
            toc += f"{INDENT * depth}- **{entry}/**\n"
            toc += build_markdown_toc(full_path, depth + 1)
        elif is_valid_file(entry):
            rel_path = os.path.relpath(full_path, ROOT_DIR).replace("\\", "/")
            toc += f"{INDENT * depth}- [{entry}]({rel_path})\n"
    return toc

def generate_toc():
    toc = "# 🗂 Tabla de Contenidos\n\n"
    toc += build_markdown_toc(ROOT_DIR)
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write(toc)
    print(f"✅ Tabla de contenido generada en: {OUTPUT_FILE}")

if __name__ == "__main__":
    generate_toc()
