.PHONY: update_mozc build install clean

MECAB_LIBEXEC_DIR = $(shell mecab-config --libexecdir)
MECAB_DIC_DIR = $(shell mecab-config --dicdir)

MATRIX_DEF = matrix.def
LEX_CSV = lex.csv

all: install

update_mozc:
	git submodule init
	git submodule update

$(MATRIX_DEF):
	./script/generate_matrix_def.py

$(LEX_CSV):
	cat mozc/src/data/dictionary_oss/dictionary*.txt | tr "\\t" "," | grep -v "^," > mozcpy/dic/lex.csv

build: update_mozc $(MATRIX_DEF) $(LEX_CSV)
	$(MECAB_LIBEXEC_DIR)/mecab-dict-index -d mozcpy/dic -o mozcpy/dic
	$(RM) mozcpy/dic/lex.csv
	$(RM) mozcpy/dic/matrix.def

install: build
	pip install .

clean:
	$(RM) mozcpy/dic/*.bin
	$(RM) mozcpy/dic/*.dic
	$(RM) mozcpy/dic/lex.csv
	$(RM) mozcpy/dic/matrix.def
