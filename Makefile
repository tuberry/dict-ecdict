VERSION=1.0.0
FILENAME=ecdict-ultimate-csv
CSVNAME=ultimate

all: build

build: ecdict.index ecdict.dict.dz

build_simp: ecdicts.index ecdicts.dict.dz

download: $(FILENAME).zip

$(FILENAME).zip:
	wget https://github.com/skywind3000/ECDICT-ultimate/releases/download/$(VERSION)/$(FILENAME).zip

ecdict.csv: $(FILENAME).zip
	unzip $(FILENAME).zip && mv $(CSVNAME).csv ecdict.csv

ecdict.txt ecdict.index ecdict.dict.dz: ecdict.csv
	python ./ecdict.py

ecdicts.txt ecdicts.index ecdicts.dict.dz: ecdict.csv
	python ./ecdicts.py

install: ecdict.index ecdict.dict.dz
	install -Dm644 ecdict.index -t $(DESTDIR)/usr/share/dict/
	install -Dm644 ecdict.dict.dz -t $(DESTDIR)/usr/share/dict/

install_simp: ecdicts.index ecdicts.dict.dz
	install -Dm644 ecdicts.index -t $(DESTDIR)/usr/share/dict/
	install -Dm644 ecdicts.dict.dz -t $(DESTDIR)/usr/share/dict/

clean:
	rm -f $(FILENAME).zip ecdict{,s}.{index,dict.dz,txt,csv}
