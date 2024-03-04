# Cosmoloj-py

[Implémentation de Simple Unit en Python](unit-simple/)

## Installation de Python

```bash
./Miniconda3-py310_23.1.0-1-Linux-x86_64.sh
# ou bien, pour l'installation complète d'Anaconda :
# ./Anaconda3-2023.03-Linux-x86_64.sh

# création d'un environnement python dédié au projet
conda create -n cosmoloj_py python=3.12
# rechargement de la configuration du terminal pour pouvoir activer l'environnement python
. ~/.bashrc
# activation de l'environnement
conda activate cosmoloj_py
# installation des dépendances du projet (dépendances de test)
conda install pylint pytest-cov
```


## Mettre à jour unenvironnement

```commandline
conda env update --file environment.yml
# ou bien simplement sans faire mention du fichier de conf Conda environment.yml implicite :
conda env update
# ou bien encore, pour supprimer les dépendances absentes du fichier d'environnement :
conda env update --prune --file environement.yml
# ou bien plus implement :
conda env update --prune
# ou bien pour forcer la suppression des dépendances :
conda env create --force
```

## Construction du paquetage PIP d'un module (exemple avec unit-simple)

https://packaging.python.org/en/latest/tutorials/packaging-projects/

Se placer dans le répertoire du module.

```commandline
cd unit-simple
```

Puis, après avoir configuré le fichier pyproject.toml, construire les paquetages:

```bash
pip install --upgrade build
python -m build
```

Et enfin les pousser avec l'utilitaire officiel de pipy.

```bash
pip install --upgrade twine
python -m twine upload --repository pypi dist/*
```

## Construction du paquetage Conda d'un module (exemple avec unit-simple)

Après avoir publié le paquet PyPI, se placer dans le répertoire du module.

```commandline
cd unit-simple
```

Puis construire la recette de build conda :

```commandline
conda skeleton pypi --pypi-url https://pypi.io/pypi/ --output-dir conda_dist unit_simple
```

On peut ensuite construire la paquet Conda :

```commandline
conda build conda_dist/unit_simple
```

Puis se connecter au dépôt Conda pour l'y publier (remplacer `<CONDA_HOME>`, `<PACKAGE>` et `<VERSION>`) :

```commandline
anaconda login
anaconda upload <CONDA_HOME>/conda-bld/linux-64/<PACKAGE>-<VERSION>-py310_0.tar.bz2
anaconda logout
```
