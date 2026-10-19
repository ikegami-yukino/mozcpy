# -*- coding: utf-8 -*-
import importlib.util

from setuptools import setup

dependencies = [] if importlib.util.find_spec('MeCab') else ['mecab']
dependencies.append('medie')

setup(
    install_requires=dependencies,
)
