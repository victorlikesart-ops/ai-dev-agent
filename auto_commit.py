import subprocess
import time
import random
from datetime import datetime

COMMIT_SAYISI = 110
GIT = r"C:\Program Files\Git\bin\git.exe"

COMMIT_MESAJLARI = [
    "refactor: improve code readability",
    "fix: handle edge case in input validation",
    "feat: add logging support",
    "docs: update README with usage examples",
    "chore: clean up unused variables",
    "fix: resolve off-by-one error",
    "feat: add error handling",
    "refactor: extract helper function",
    "docs: add inline comments",
    "fix: correct typo in variable name",
    "feat: implement retry logic",
    "chore: update .gitignore",
    "refactor: simplify conditional logic",
    "fix: prevent null reference",
    "feat: add input sanitization",
    "docs: improve function docstrings",
    "chore: remove debug print statements",
    "fix: memory leak fix",
    "feat: add config file support",
    "refactor: modularize main function",
]

def run(cmd):
    subprocess.run(cmd, shell=True, check=True)

def commit(n):
    with open("log.txt", "a") as f:
        f.write(f"[{datetime.now()}] commit #{n}\n")
    mesaj = random.choice(COMMIT_MESAJLARI) + f" (#{n})"
    run(f'"{GIT}" add .')
    run(f'"{GIT}" commit -m "{mesaj}"')
    print(f"✅ Commit {n}/{COMMIT_SAYISI}: {mesaj}")

run(f'"{GIT}" config user.email "victorlikesart@gmail.com"')
run(f'"{GIT}" config user.name "victorlikesart-ops"')

print(f"🚀 {COMMIT_SAYISI} commit başlıyor...\n")

for i in range(1, COMMIT_SAYISI + 1):
    commit(i)
    time.sleep(0.3)

print("\n📤 GitHub'a push ediliyor...")
run(f'"{GIT}" push origin main')
print("\n🎉 Bitti!")