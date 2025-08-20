import os
import ast
from collections import defaultdict

# Wurzelverzeichnis, das durchsucht werden soll
wurzelpfad = "D:\\documents\\MyTrading\\Tools_alles\\python\\SimuQuant"

# Alle .py-Dateien rekursiv sammeln
python_files = []
for root, dirs, files in os.walk(wurzelpfad):
    for file in files:
        if file.endswith(".py"):
            python_files.append(os.path.join(root, file))

# Funktion: AST-Dump für Vergleich
def get_function_dump(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        try:
            tree = ast.parse(f.read())
        except SyntaxError:
            return []  # Datei überspringen bei Syntaxfehler
    return [node for node in tree.body if isinstance(node, ast.FunctionDef)]

# Alle Funktionen sammeln
duplikate = defaultdict(lambda: defaultdict(list))  # {filename: {func_name: [dump]}}

for file in python_files:
    functions = get_function_dump(file)
    for func in functions:
        dump = ast.dump(func)
        duplikate[file][func.name].append(dump)

# Ausgabe: Doppelte Funktionen mit identischem Inhalt
for file, func_dict in duplikate.items():
    for name, dumps in func_dict.items():
        if len(dumps) > 1 and len(set(dumps)) == 1:
            print(f"\n🔁 Datei: {file}")
            print(f"→ Doppelte Funktion: {name} (identisch definiert)")

