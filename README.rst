mozcpy
==========
|circleci| |pyversion| |version| |license|

Mozc for Python: yet another Kana-Kanji converter

INSTALLATION
==============

::

 $ pip install mozcpy


USAGE
============

.. code:: python

  import mozcpy

  converter = mozcpy.Converter()
  converter.convert('まほうしょうじょ')
  # => '魔法少女'
  converter.convert('まほうしょうじょ', n_best=10)
  # => ['魔法少女', '魔法消除', '魔法省所', '魔法小所', '魔法昇叙', '魔砲少女', 'マホウ少女', '魔法証所', '魔法賞所']

  converter.convert_wakati('もうなにもこわくない')
  # => 'もう 何 も 怖く ない'
  converter.convert_wakati('もうなにもこわくない', n_best=3)
  # => ['もう 何 も 怖く ない', 'もう 何 も こわく ない', 'もう 何 も 恐く ない']

  converter.wakati("もうなにもこわくない")
  # => 'もう なに も こわく ない'
  converter.wakati("もうなにもこわくない", n_best=10)  # duplicatetions are ignored
  # => ['もう なに も こわく ない']

FOR DEVELOPER
===============

This module uses Git LFS to pull dictionary files.

ACKNOWLEDGEMENT
=================

This module relies on Mozc and MeCab.

- . T. Kudo, T. Hanaoka, J. Mukai, Y. Tabata, H. Komatsu. 2011. Efficient dictionary and language model compression for input method editors. In Proceedings of the Workshop on Advances in Text Input Methods (WTIM 2011), pp 19-25.

- . T. Kudo, H. Komatsu, T. Hanaoka, A. Mukai, Y. Tabata, K. Yamamoto, Y. Matsumoto. 2004. Applying Conditional Random Fields to Japanese Morphological Analysis. In Proceedings of the EMNLP 2004, pp 230-237.


.. |circleci| image:: https://dl.circleci.com/status-badge/img/gh/ikegami-yukino/mozcpy/tree/master.svg?style=svg
        :target: https://dl.circleci.com/status-badge/redirect/gh/ikegami-yukino/mozcpy/tree/master

.. |pyversion| image:: https://img.shields.io/pypi/pyversions/mozcpy.svg

.. |version| image:: https://img.shields.io/pypi/v/mozcpy.svg
    :target: http://pypi.python.org/pypi/mozcpy/
    :alt: latest version

.. |license| image:: https://img.shields.io/pypi/l/mozcpy.svg
    :target: http://pypi.python.org/pypi/mozcpy/
    :alt: license
