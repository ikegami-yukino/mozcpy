MECAB_LIBEXEC_DIR = $(shell mecab-config --libexecdir)

MATRIX_DEF = mozcpy/dic/matrix.def
LEX_CSV = mozcpy/dic/lex.csv
MOZC_TAG_FILE = mozcpy/dic/tag-version.txt
LATEST_MOZC_TAG = $(shell git -C mozc describe --tags --abbrev=0)

.PHONY: all update_mozc build install check-version clean

all: install

update_mozc:
	git submodule update --remote
	cd mozc; git checkout `git describe --tags --abbrev=0`

$(MATRIX_DEF):
	./script/generate_matrix_def.py

$(LEX_CSV):
	cat mozc/src/data/dictionary_oss/dictionary*.txt | tr "\\t" "," | grep -v "^," > $@
	cat mozc/src/data/dictionary_oss/suffix.txt | tr "\\t" "," | grep -v "^," >> $@

build: update_mozc $(MOZC_TAG_FILE) mozcpy/dic/sys.dic

mozcpy/dic/sys.dic: $(MOZC_TAG_FILE)
	$(MAKE) $(MATRIX_DEF) $(LEX_CSV)
	$(MECAB_LIBEXEC_DIR)/mecab-dict-index -d mozcpy/dic -o mozcpy/dic -f utf-8 -t utf-8
	$(RM) $(LEX_CSV)
	$(RM) $(MATRIX_DEF)

$(MOZC_TAG_FILE): check-version
	@# ファイルが存在しないか、中身が現在のタグと異なる場合のみ書き込む
	@if [ ! -f $@ ] || [ "$$(cat $@)" != "$(LATEST_MOZC_TAG)" ]; then \
		echo "Update is available: The latest Mozc tag is $(LATEST_MOZC_TAG)"; \
		echo $(LATEST_MOZC_TAG) > $@; \
	else \
		echo "No update: The latest Mozc tag remains $(LATEST_MOZC_TAG)"; \
	fi

# 強制的にルールを実行させるためのダミーターゲット
check-version:
	@:

init:
	git lfs install
	git lfs pull
	git lfs fetch --all
	git lfs checkout

install: build
	pip install .

test:
	tox -p

clean:
	$(RM) mozcpy/dic/*.bin
	$(RM) mozcpy/dic/*.dic
	$(RM) $(LEX_CSV)
	$(RM) $(MATRIX_DEF)
	$(RM) $(MOZC_TAG_FILE)
