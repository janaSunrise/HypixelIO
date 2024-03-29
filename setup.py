import re
from itertools import chain
from pathlib import Path

import setuptools

# Constant variables
BASE_DIR = Path(__file__).resolve().parent

README = Path(BASE_DIR / "README.md").read_text()

URL = "https://github.com/janaSunrise/HypixelIO"

# Version locating and assignment
VERSION = re.search(
    r'^__version__\s*=\s*[\'"]([^\'"]*)[\'"]',
    Path(BASE_DIR / "hypixelio/__init__.py").read_text(),
    re.MULTILINE,
).group(  # type: ignore
    1
)

# Version error
if not VERSION:
    raise RuntimeError("VERSION is not set.")

# Dependencies configuration
extras_require = {"speedups": ["aiodns==3.0.0", "Brotli==1.0.9", "cchardet==2.1.7"]}
extras_require["all"] = list(chain.from_iterable(extras_require.values()))

# Main setup
setuptools.setup(
    name="HypixelIO",
    version=VERSION,
    author="Sunrit Jana",
    author_email="warriordefenderz@gmail.com",
    description="A modern, efficient and better way of interacting with the Hypixel API!",
    long_description=README,
    long_description_content_type="text/markdown",
    license="MIT",
    url=URL,
    project_urls={"Documentation": URL, "Issue tracker": f"{URL}/issues"},
    packages=setuptools.find_packages(exclude=["tests", "tests.*", "tools", "tools.*"]),
    package_data={"hypixelio": ["py.typed"]},
    install_requires=[
        "requests==2.28.2",
        "aiohttp==3.8.3",
    ],
    extras_require=extras_require,
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Typing :: Typed",
    ],
    python_requires=">=3.7",
)
