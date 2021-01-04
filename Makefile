PKGNAME=ecdict
CSVNAME=ultimate
FILENAME=ecdict-ultimate-csv
URL=https://github.com/skywind3000/ECDICT-ultimate

ifndef VERSION
	VERSION=1.0.0
endif

all: $(PKGNAME).index $(PKGNAME).dict.dz

$(PKGNAME).csv:
	curl -kLO $(URL)/releases/download/$(VERSION)/$(FILENAME).zip
	unzip $(FILENAME).zip && mv $(CSVNAME).csv $(PKGNAME).csv

$(PKGNAME).txt: $(PKGNAME).csv
ifdef FULL
	python ./$(PKGNAME).py ./$(PKGNAME).csv $(PKGNAME).txt
else
	python ./$(PKGNAME)s.py ./$(PKGNAME).csv $(PKGNAME).txt
endif

$(PKGNAME).index $(PKGNAME).dict.dz: $(PKGNAME).txt
	dictfmt --utf8 --allchars -s ECDICT -u $(URL) -j $(PKGNAME) < ./$(PKGNAME).txt && dictzip $(PKGNAME).dict

install: $(PKGNAME).index $(PKGNAME).dict.dz
	install -Dm644 $(PKGNAME).index -t $(DESTDIR)/usr/share/dict/
	install -Dm644 $(PKGNAME).dict.dz -t $(DESTDIR)/usr/share/dict/

clean:
	-rm -f $(PKGNAME).{index,dict.dz,txt,csv}
