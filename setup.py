import setuptools
from pathlib import Path

setuptools.setup(
    name="HypixelIO",
    version="0.0.3",

    author="Sunrit Jana",
    author_email="warriordefenderz@gmail.com",

    description="A modern efficient and faster way of interacting with the Hypixel API!",
    long_description=Path("README.md").read_text(),
    long_description_content_type="text/markdown",
    license="MIT",

    url="https://github.com/janaSunrise/HypixelIO",
    packages=setuptools.find_packages(
        exclude=["tests", "tests.*", "tools", "tools.*"]
    ),

    install_requires=[
        'requests',
        'requests-cache',
    ],

    classifiers=[
        "Programming Language :: Python :: 3",
        "LICENSE :: OSI APPROVED :: GNU GENERAL PUBLIC LICENSE V3 (GPLV3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
