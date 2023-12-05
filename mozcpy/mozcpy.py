# -*- coding: utf-8 -*-
import os

import MeCab

DICT_DIR = os.path.join(os.path.dirname(__file__), 'dic')
MECAB_ARGS = '-d %s' % DICT_DIR
MECAB_ARGS += ' -r /dev/null' if os.name == "posix" else ' -r nul'
if os.sep == '\\':
    MECAB_ARGS = MECAB_ARGS.replace('\\', '\\\\')


class Converter(object):
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
