import os

from setuptools import find_packages, setup

here = os.path.abspath(os.path.dirname(__file__))

if __name__ == "__main__":
    setup(
        packages=find_packages(),
        install_requires=["xsdata"],
        extras_require={},
    )
