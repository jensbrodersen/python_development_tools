import os
import ast
from collections import defaultdict

# Wurzelverzeichnis
wurzelpfad = "D:\\documents\\MyTrading\\Tools_alles\\python\\SimuQuant"

# Alle .py-Dateien sammeln, außer die mit "test_" im Namen
python_files = []
for root, dirs, files in os.walk(wurzelpfad):
    for file in files:
        if file.endswith(".py") and not file.startswith("test_"):
            python_files.append(os.path.join(root, file))

# Alle Funktionsdefinitionen sammeln: {funktion: [pfade]}
definierte_funktionen = defaultdict(list)

# Alle Funktionsverwendungen sammeln: set(funktionsnamen)
verwendete_funktionen = set()

# AST-Analyse
for file_path in python_files:
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            code = f.read()
            tree = ast.parse(code)
    except SyntaxError:
        continue  # Datei überspringen bei Fehler

    # Definitionen sammeln
    for node in ast.walk(tree):
        if isinstance(node, ast.FunctionDef):
            definierte_funktionen[node.name].append(file_path)

    # Verwendungen sammeln
    for node in ast.walk(tree):
        if isinstance(node, ast.Call) and isinstance(node.func, ast.Name):
            verwendete_funktionen.add(node.func.id)

# Unbenutzte Funktionen ermitteln
unbenutzt = []
for func_name, pfade in definierte_funktionen.items():
    if func_name not in verwendete_funktionen:
        for pfad in pfade:
            unbenutzt.append((func_name, pfad))

# Formatierte Ausgabe
if unbenutzt:
    print("\n📦 Unbenutzte Funktionen im Projekt (ohne test_*.py):\n")
    max_len = max(len(name) for name, _ in unbenutzt)
    for name, pfad in sorted(unbenutzt):
        print(f"{name.ljust(max_len)}   →   {pfad}")
else:
    print("✅ Keine unbenutzten Funktionen gefunden.")
