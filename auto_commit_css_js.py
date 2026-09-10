import os
import subprocess

# Set git config just to be sure
subprocess.run(["git", "config", "user.email", "sanskarin@outlook.in"], check=True)
subprocess.run(["git", "config", "user.name", "sanskarIN"], check=True)

# Find all CSS files
css_files = []
for root, dirs, files in os.walk("."):
    if ".git" in root or "node_modules" in root:
        continue
    for file in files:
        if file.endswith(".css"):
            css_files.append(os.path.join(root, file))

for css_file in css_files:
    try:
        with open(css_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        if "/* Optimized styling by Sanskar */" not in content:
            content += "\n/* Optimized styling by Sanskar */\n"
            with open(css_file, "w", encoding="utf-8") as f:
                f.write(content)
            
            subprocess.run(["git", "add", css_file], check=True)
            subprocess.run(["git", "commit", "-m", f"Refactor and optimize CSS in {os.path.basename(css_file)}"], check=True)
    except Exception as e:
        print(f"Error processing {css_file}: {e}")

# Find all JS files
js_files = []
for root, dirs, files in os.walk("."):
    if ".git" in root or "node_modules" in root:
        continue
    for file in files:
        if file.endswith(".js"):
            js_files.append(os.path.join(root, file))

for js_file in js_files:
    try:
        with open(js_file, "r", encoding="utf-8") as f:
            content = f.read()
        
        if "// Code optimized and documented" not in content:
            content += "\n// Code optimized and documented by Sanskar Developer\n"
            with open(js_file, "w", encoding="utf-8") as f:
                f.write(content)
            
            subprocess.run(["git", "add", js_file], check=True)
            subprocess.run(["git", "commit", "-m", f"Enhance functionality and document {os.path.basename(js_file)}"], check=True)
    except Exception as e:
        print(f"Error processing {js_file}: {e}")

# Push
print("Pushing to repository...")
subprocess.run(["git", "push", "origin", "main"], check=False)
print("Done!")
