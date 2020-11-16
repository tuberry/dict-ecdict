VERSION=1.0.0
FILENAME=ecdict-ultimate-csv
CSVNAME=ultimate
PKGNAME=ecdict

all: build

build: $(PKGNAME).index $(PKGNAME).dict.dz

download: $(FILENAME).zip

$(FILENAME).zip:
	curl -kLO https://github.com/skywind3000/ECDICT-ultimate/releases/download/$(VERSION)/$(FILENAME).zip

$(PKGNAME).tmp: $(FILENAME).zip
	unzip $(FILENAME).zip && mv $(CSVNAME).csv $(PKGNAME).tmp

$(PKGNAME).txt: $(PKGNAME).tmp
ifdef FULL
	python ./$(PKGNAME).py ./$(PKGNAME).tmp $(PKGNAME).txt
else
	python ./$(PKGNAME)s.py ./$(PKGNAME).tmp $(PKGNAME).txt
endif

$(PKGNAME).index $(PKGNAME).dict.dz: $(PKGNAME).txt
	dictfmt --utf8 --allchars -s ECDICT -u https://github.com/skywind3000/ECDICT -j $(PKGNAME) < ./$(PKGNAME).txt
	dictzip $(PKGNAME).dict

install: $(PKGNAME).index $(PKGNAME).dict.dz
	install -Dm644 $(PKGNAME).index -t $(DESTDIR)/usr/share/dict/
	install -Dm644 $(PKGNAME).dict.dz -t $(DESTDIR)/usr/share/dict/

clean:
	-rm -f $(PKGNAME).{index,dict.dz,txt,tmp}
