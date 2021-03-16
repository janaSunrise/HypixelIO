import re
from pathlib import Path

import setuptools

# -- Constants --
BASE_DIR = Path(__file__).resolve().parent
README = Path(BASE_DIR / "README.md").read_text()
URL = "https://github.com/janaSunrise/HypixelIO"

# -- Version config --
VERSION = re.search(
    r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    Path(BASE_DIR / "hypixelio/__init__.py").read_text(),
    re.MULTILINE
).group(1)

if not VERSION:
    raise RuntimeError("VERSION is not set!")

setuptools.setup(
    name="HypixelIO",
    version=VERSION,

    author="Sunrit Jana",
    author_email="warriordefenderz@gmail.com",

    description="A modern, efficient and faster way of interacting with the Hypixel API!",
    long_description=README,
    long_description_content_type="text/markdown",
    license="GPL v3",

    url=URL,

    project_urls={
        "Documentation": URL,
        "Issue tracker": f"{URL}/issues",
    },

    packages=setuptools.find_packages(
        exclude=["tests", "tests.*", "tools", "tools.*"]
    ),

    install_requires=[
        "requests==2.25.1",
        "requests-cache==0.5.2",
        "aiohttp==3.7.4.post0"
    ],
    extras_require={
        "speedups": [
            "aiodns>=1.1",
            "Brotli",
            "cchardet",
        ],
    },

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
