import os

os.system(f'python3 -m venv .venv')

with open('requirments.txt', 'r', encoding='utf-16') as file:
    requirements = file.read()

requirements = requirements.split()

for req in requirements:
    os.system(f'.venv/bin/pip install {req}')
