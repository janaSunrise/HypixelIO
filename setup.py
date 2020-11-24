import re
from pathlib import Path

import setuptools

BASE_DIR = Path(__file__).resolve().parent

README = Path(BASE_DIR / "README.md").read_text()

VERSION = re.search(
    r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    Path(BASE_DIR / "hypixelio/__init__.py").read_text(),
    re.MULTILINE
).group(1)

if not VERSION:
    raise RuntimeError('version is not set')

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

    project_urls={
        "Documentation": "https://github.com/janaSunrise/HypixelIO",
        "Issue tracker": "https://github.com/janaSunrise/HypixelIO/issues",
    },

    packages=setuptools.find_packages(
        exclude=["tests", "tests.*", "tools", "tools.*"]
    ),

    install_requires=[
        'requests==2.25.0',
        'requests-cache==0.5.2'
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Programming Language :: Python :: Implementation :: CPython",

        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",

        "Operating System :: OS Independent",

        "Intended Audience :: Developers",

        "Natural Language :: English",
    ],

    python_requires='>=3.6',
)
