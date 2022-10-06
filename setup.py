# -*- coding: utf-8 -*-
import os
import re
from codecs import open
from pathlib import Path

from setuptools import setup


def _get_requirements():
    root = Path(__file__).parent

    with open(root / "requirements.txt") as f:
        reqs = f.read().splitlines()

    reqs = [req for req in reqs if not req.startswith("-f")]

    return reqs


with open(os.path.join("mozcpy", "__init__.py"), "r", encoding="utf8") as f:
    version = re.compile(r".*__version__ = '(.*?)'", re.S).match(f.read()).group(1)

setup(
    name="mozcpy",
    packages=["mozcpy"],
    version=version,
    license="MIT License",
    platforms=["POSIX", "Windows", "Unix", "MacOS"],
    description="Mozc for Python: yet another Kana-Kanji converter",
    author="Yukino Ikegami",
    author_email="yknikgm@gmail.com",
    url="https://github.com/ikegami-yukino/mozcpy",
    keywords=["Kana-Kanji converter"],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Intended Audience :: Information Technology",
        "License :: OSI Approved :: MIT License",
        "Natural Language :: Japanese",
        "Programming Language :: Python :: 3.4",
        "Programming Language :: Python :: 3.5",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Topic :: Text Processing :: Linguistic",
    ],
    long_description="%s\n\n%s"
    % (open("README.rst", encoding="utf8").read(), open("CHANGES.rst", encoding="utf8").read()),
    package_data={"mozcpy": ["dic/*"]},
    install_requires=_get_requirements(),
    tests_require=["pytest"],
    test_suite="pytest",
)
