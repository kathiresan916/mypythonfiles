"""Path Concepts"""

from pathlib import Path

path = Path("Exercises")
for file in path.glob('*.py'):
    print(file)
