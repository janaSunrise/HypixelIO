import setuptools
from pathlib import Path

from hypixelio.utils.constants import VERSION

BASE_DIR = Path(__file__).resolve().parent

README = Path(BASE_DIR / "README.md").read_text()
REQUIREMENTS = Path(BASE_DIR / "requirements.txt").read_text().splitlines()

setuptools.setup(
    name="HypixelIO",
    version=VERSION,

    author="Sunrit Jana",
    author_email="warriordefenderz@gmail.com",

    description="A modern efficient and faster way of interacting with the Hypixel API!",
    long_description=README,
    long_description_content_type="text/markdown",
    license="GPL v3",

    url="https://github.com/janaSunrise/HypixelIO",

    packages=setuptools.find_packages(
        exclude=["tests", "tests.*", "tools", "tools.*"]
    ),

    install_requires=REQUIREMENTS,

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Programming Language :: Python :: Implementation :: CPython",

        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",

        "Operating System :: OS Independent",
    ],

    python_requires='>=3.6',
)
