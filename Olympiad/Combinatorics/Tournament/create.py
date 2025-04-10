from pathlib import Path


*a, = map(int, input().split())


for i in a:
    file = Path(f"./questions/{i}.tex")
    file2 = Path(f"./answers/{i}.tex")
    if not file.exists() and not file2.exists():
        with open(f"./questions/{i}.tex", 'w') as f:
            f.write("")
        with open(f"./answers/{i}.tex", 'w') as f:
            f.write("")
    else:
        print(f"file {i} exists.")
        