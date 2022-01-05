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
).group(1)

# Version error
if not VERSION:
    raise RuntimeError("VERSION is not set!")

# Dependencies configuration
extras_require = {
    "speedups": ["aiodns>=1.1", "Brotli==1.0.9", "cchardet==2.1.7"],
    "cache": ["boto3==1.20.28", "pymongo==4.0.1", "redis==4.1.0"],
    "async-cache": ["aiosqlite==0.17.0", "motor==2.5.1", "aioredis==2.0.1"]
}
extras_require["all"] = list(chain.from_iterable(extras_require.values()))

# Main setup
setuptools.setup(
    # Project info
    name="HypixelIO",
    version=VERSION,

    # Author info
    author="Sunrit Jana",
    author_email="warriordefenderz@gmail.com",

    # Description
    description="A modern, efficient and better way of interacting with the Hypixel API!",
    long_description=README,
    long_description_content_type="text/markdown",

    # Licensing
    license="MIT",

    # Project repo info
    url=URL,
    project_urls={"Documentation": URL, "Issue tracker": f"{URL}/issues"},

    # Packages in the project
    packages=setuptools.find_packages(exclude=["tests", "tests.*", "tools", "tools.*"]),

    # Dependencies for the package
    install_requires=[
        "requests==2.25.1",
        "aiohttp==3.7.4.post0",
        "requests-cache==0.6.3",
        "aiohttp-client-cache==0.4.0",
    ],
    extras_require=extras_require,

    # Classifiers
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
        "Typing :: Typed"
    ],

    # Minimum python version
    python_requires=">=3.7",
)
