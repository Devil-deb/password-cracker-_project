# password-cracker-_project
✅ Step 1: Python Script – Brute Force Hash Cracker
We'll write a simple Python script that:

Takes a hashed password.

Tries to match it using a wordlist.

Supports MD5, SHA1, SHA256, etc.

hash_cracker.py
python
Copy
Edit
import hashlib
import sys

def crack_hash(hash_to_crack, wordlist_path, hash_type='md5'):
    try:
        with open(wordlist_path, 'r', encoding='utf-8') as file:
            for word in file:
                word = word.strip()
                hashed_word = hashlib.new(hash_type, word.encode()).hexdigest()
                if hashed_word == hash_to_crack:
                    print(f"[+] Password found: {word}")
                    return
        print("[-] Password not found in the wordlist.")
    except Exception as e:
        print(f"[!] Error: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Usage: python hash_cracker.py <hash> <wordlist.txt> <hash_type>")
        print("Example: python hash_cracker.py e99a18c428cb38d5f260853678922e03 wordlist.txt md5")
        sys.exit(1)
    
    hash_input = sys.argv[1]
    wordlist_file = sys.argv[2]
    hash_algo = sys.argv[3].lower()

    crack_hash(hash_input, wordlist_file, hash_algo)
✅ Step 2: Create README.md
README.md
markdown
Copy
Edit
# 🔐 Hash Cracker

A simple brute-force password hash cracker using a wordlist.

## ⚠️ Disclaimer
This tool is intended for **educational and authorized use only**.

## 🛠️ Features
- Supports multiple hash types: `md5`, `sha1`, `sha256`, etc.
- Easy to use with command-line arguments.

## 🚀 Usage
```bash
python hash_cracker.py <hash> <wordlist.txt> <hash_type>
Example
bash
Copy
Edit
python hash_cracker.py e99a18c428cb38d5f260853678922e03 wordlist.txt md5
📄 License
MIT License

yaml
Copy
Edit

---

## ✅ Step 3: Upload to GitHub

### 1. **Initialize Git Repo**
```bash
git init
git add .
git commit -m "Initial commit: Simple hash cracker"
2. Create GitHub Repo
Go to GitHub and create a new repository (e.g., hash-cracker).

3. Push to GitHub
bash
Copy
Edit
git remote add origin https://github.com/your-username/hash-cracker.git
git branch -M main
git push -u origin main

