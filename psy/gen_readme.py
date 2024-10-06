import os
import urllib.parse

def generate_readme():
    # Get all .md files in the current directory (excluding the README.md)
    md_files = [f for f in os.listdir() if f.endswith(".md") and f != "README.md"]
    
    # Start the content of the README.md
    readme_content = "# Markdown Files\n\n"
    readme_content += "A list of all markdown files in this directory:\n\n"

    # Add each file to the list in markdown link format
    for md_file in md_files:
        # URL-encode the filename to be safe for links
        safe_file_name = urllib.parse.quote(md_file)
        # Append a bullet point for each file
        readme_content += f"- [{md_file}](./{safe_file_name})\n"

    # Write the README.md file with UTF-8 encoding
    with open("README.md", "w", encoding="utf-8") as readme_file:
        readme_file.write(readme_content)

if __name__ == "__main__":
    generate_readme()
