# -*- coding: utf-8 -*-
import os

import mozcpy

DICT_DIR = os.path.join(os.path.dirname(__file__), 'mozcpy', 'dic')
MECAB_ARGS = '-d %s' % DICT_DIR


def test__convert():
    converter = mozcpy.Converter()
    actual = converter._convert('いけがみです', 1, MECAB_ARGS)
    assert isinstance(actual, str)
    assert actual == '池上です'

    actual = converter._convert('いけがみです', 2, MECAB_ARGS)
    assert isinstance(actual, list)
    assert len(actual) == 1
    assert actual[0] == '池上です'


def test_convert():
    converter = mozcpy.Converter()
    actual = converter.convert('いけがみです')
    assert isinstance(actual, str)
    assert actual == '池上です'

    actual = converter.convert('いけがみです', n_best=2)
    assert isinstance(actual, list)
    assert len(actual) == 1
    assert actual[0] == '池上です'


def test_convert_wakati():
    converter = mozcpy.Converter()
    actual = converter.convert_wakati('いけがみです')
    assert isinstance(actual, str)
    assert actual == '池上 です'

    actual = converter.convert_wakati('いけがみです', n_best=2)
    assert isinstance(actual, list)
    assert len(actual) == 1
    assert actual[0] == '池上 です'


def test_wakati():
    converter = mozcpy.Converter()
    actual = converter.wakati('いけがみです')
    assert isinstance(actual, str)
    assert actual == 'いけがみ です'

    actual = converter.wakati('いけがみです', n_best=2)
    assert isinstance(actual, list)
    assert len(actual) == 1
    assert actual[0] == 'いけがみ です'
