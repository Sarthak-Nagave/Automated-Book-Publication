import os

def save_version(version_name, content):
    os.makedirs("versions", exist_ok=True)
    with open(f"versions/{version_name}.txt", "w", encoding="utf-8") as f:
        f.write(content)
