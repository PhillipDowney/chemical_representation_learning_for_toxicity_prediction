"""Install package."""
from setuptools import setup, find_packages
import os
import codecs


def read(rel_path):
    here = os.path.abspath(os.path.dirname(__file__))
    with codecs.open(os.path.join(here, rel_path), "r") as fp:
        return fp.read()


def get_version(rel_path):
    for line in read(rel_path).splitlines():
        if line.startswith("__version__"):
            delim = '"' if '"' in line else "'"
            return line.split(delim)[1]
    else:
        raise RuntimeError("Unable to find version string.")


setup(
    name="toxsmi",
    version=get_version("toxsmi/__init__.py"),
    description=("PyTorch implementation of toxicity prediction models from SMILES."),
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/PhillipDowney/toxsmi",
    author="Jannis Born, Greta Markert, Matteo Manica",
    author_email=("jab@zurich.ibm.com, greta.markert@gmail.com, drugilsberg@gmail.com"),
    install_requires=[
        "paccmann_predictor @ git+https://github.com/PhillipDowney/paccmann_predictor@"0.0.2",
        "torch",
        "deepchem",
        "tensorflow>=2.0",
        "Pillow",
        "six",
        "brc_pytorch>=0.1.3",
        "pytoda>=1.1.2",
    ],
    packages=find_packages("."),
    zip_safe=False,
)
