import os
import subprocess
import re

def main():
    target_dir = r"E:\All_the_Projects_of_the-Sanskar\SANSKAR Folder\Web-Development-Mastery"
    
    html_files = []
    for root, dirs, files in os.walk(target_dir):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if '.git' in dirs:
            dirs.remove('.git')
        
        for file in files:
            if file.endswith(".html"):
                html_files.append(os.path.join(root, file))

    twitter_tags = """<meta name="twitter:card" content="summary_large_image">\n    <meta name="twitter:site" content="@Sanskar_in">\n    <meta name="twitter:creator" content="@Sanskar_in">"""

    for file_path in html_files:
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            if '<meta name="twitter:card"' in content:
                continue

            og_matches = list(re.finditer(r'<meta property="og:.*?>', content, re.IGNORECASE | re.DOTALL))
            if og_matches:
                last_match = og_matches[-1]
                insert_pos = last_match.end()
            else:
                desc_match = re.search(r'<meta name="description".*?>', content, re.IGNORECASE | re.DOTALL)
                if desc_match:
                    insert_pos = desc_match.end()
                else:
                    head_match = re.search(r'<head.*?>', content, re.IGNORECASE | re.DOTALL)
                    if head_match:
                        insert_pos = head_match.end()
                    else:
                        insert_pos = -1

            if insert_pos != -1:
                new_content = content[:insert_pos] + "\n    " + twitter_tags + content[insert_pos:]
                
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(new_content)
                    
                subprocess.run(["git", "add", file_path], cwd=target_dir)
                filename = os.path.basename(file_path)
                subprocess.run(["git", "commit", "-m", f"seo: add Twitter Card meta tags to {filename}"], cwd=target_dir)
                print(f"Processed {filename}")
        except Exception as e:
            print(f"Error processing {file_path}: {e}")

if __name__ == "__main__":
    main()
