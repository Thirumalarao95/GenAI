import os

readme_content = "#  Python Assignment (Auto-Generated)\n\n"
readme_content += "##  Overview\nThis README is automatically generated from Python files in this folder.\n\n"
readme_content += "##  Files\n\n"

# Loop through all files
for file in os.listdir():
    if file.endswith(".ipynb") and file != "generate_readme.py":
        readme_content += f"### {file}\n"

        with open(file, "r") as f:
            lines = f.readlines()

            # Get first few lines as preview
            preview = "".join(lines[:5])
            readme_content += "python\n"
            readme_content += preview
            readme_content += "\n\n\n"

readme_content += "---\n"
readme_content += "##  How to Run\nbash\npython filename.ipynb\n\n"

# Write README
with open("README.md", "w") as f:
    f.write(readme_content)

print("README.md generated automatically!")
