import re
from itertools import chain
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
    re.MULTILINE,
).group(1)

if not VERSION:
    raise RuntimeError("VERSION is not set!")

extras_require = {
    "speedups": ["aiodns>=1.1", "Brotli==1.0.9", "cchardet==2.1.7"],
    "cache": ["boto3==1.17.82", "pymongo==3.11.4", "redis==3.5.3"],
    "async-cache": ["aiosqlite==0.17.0", "motor==2.4.0", "aioredis==1.3.1"],
}
extras_require["all"] = list(chain.from_iterable(extras_require.values()))

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
    project_urls={"Documentation": URL, "Issue tracker": f"{URL}/issues"},

    packages=setuptools.find_packages(exclude=["tests", "tests.*", "tools", "tools.*"]),

    install_requires=[
        "requests==2.25.1",
        "aiohttp==3.7.4.post0",
        "requests-cache==0.6.3",
        "aiohttp-client-cache==0.4.0",
    ],
    extras_require=extras_require,

    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: Implementation :: CPython",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Intended Audience :: Developers",
        "Natural Language :: English",
    ],
    python_requires=">=3.6",
)
