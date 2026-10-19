# -*- coding: utf-8 -*-
import os

import MeCab
from medie import Medie

DICT_DIR = os.path.join(os.path.dirname(__file__), 'dic')
DICT_VERSION_FILE = os.path.join(DICT_DIR, 'tag-version.txt')
SYS_DIC = os.path.join(DICT_DIR, 'sys.dic')
MECAB_ARGS = '-d %s' % DICT_DIR
MECAB_ARGS += ' -r /dev/null' if os.name == "posix" else ' -r nul'
if os.sep == '\\':
    MECAB_ARGS = MECAB_ARGS.replace('\\', '\\\\')


class Converter(object):
    _dict_version: str

    def __init__(self):
        self._trie = Medie(SYS_DIC)
        with open(DICT_VERSION_FILE, 'r', encoding='utf-8') as f:
            self._dict_version = f.read().strip()

    def dict_version(self):
        return self._dict_version

    @staticmethod
    def _convert(sentence, n_best, mecab_args):
        tagger = MeCab.Tagger(mecab_args)
        tagger.parse('')  # for avoiding a bug
        if n_best > 1:
            result_s = tagger.parseNBest(n_best, sentence).replace(" \n", "\n")
            result = result_s.splitlines()
            return list(sorted(set(result), key=result.index))
        return tagger.parse(sentence).rstrip()

    def convert(self, sentence, n_best=1):
        return self._convert(sentence, n_best, MECAB_ARGS)

    def convert_wakati(self, sentence, n_best=1):
        return self._convert(sentence, n_best, MECAB_ARGS + ' -Owakachi')

    def wakati(self, sentence, n_best=1):
        return self._convert(sentence, n_best, MECAB_ARGS + ' -Owakati')

    def search_prefix(self, sentence, n_best=5):
        result = []
        tokens = self._trie.search_prefix(sentence, n_best)
        if tokens:
            result = [x['feature'] for x in sorted(tokens, key=lambda x: [x['cost'], len(x['surface']), len(x['feature'])])]
            result = list(sorted(set(result), key=result.index))
        return result
