# Cosmoloj-py

[Implémentation de Simple Unit en Python](unit-simple/)

## Installation de Python

```bash
./Miniconda3-py310_23.1.0-1-Linux-x86_64.sh
# ou bien, pour l'installation complète d'Anaconda :
# ./Anaconda3-2023.03-Linux-x86_64.sh

# création d'un environnement python dédié au rpojet
conda create -n cosmoloj_py python=3.10
# rechargement de la configuration du terminal pour pouvoir activer l'environnement python
. ~/.bashrc
# activation de l'environnement
conda activate cosmoloj_py
# installation des dépendances du projet (dépendances de test)
conda install pylint pytest
```

## Construction du paquetage PIP d'un module

https://packaging.python.org/en/latest/tutorials/packaging-projects/

Se placer dans le répertoire du module.

Puis construire les paquetages.

```bash
pip install --upgrade build
python -m build
```

Et enfin les pousser avec l'utilitaire officiel de pipy.

```bash
pip install --upgrade twine
python -m twine upload --repository testpypi dist/*
```

## Construction du paquetage Conda


```
conda install conda-build

```
