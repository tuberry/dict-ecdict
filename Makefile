PKGNAME=ecdict
CSVNAME=ultimate.csv
FILENAME=ecdict-ultimate-csv.zip
URL=https://github.com/skywind3000/ECDICT-ultimate

ifndef VERSION
	VERSION=1.0.0
endif

ifndef MINI
	MINI=true
endif

all: $(PKGNAME).index $(PKGNAME).dict.dz

$(FILENAME):
	curl -kLO $(URL)/releases/download/$(VERSION)/$(FILENAME)

$(PKGNAME).csv: $(FILENAME)
	unzip $(FILENAME) && cp $(CSVNAME) $(PKGNAME).csv

$(PKGNAME).txt: $(PKGNAME).csv
ifeq ($(MINI),true)
	python ./$(PKGNAME).py -i ./$(PKGNAME).csv -o $(PKGNAME).txt
else
	python ./$(PKGNAME).py -i ./$(PKGNAME).csv -o $(PKGNAME).txt --no-mini
endif

$(PKGNAME).index $(PKGNAME).dict.dz &: $(PKGNAME).txt
	dictfmt --utf8 --allchars -s ECDICT -u $(URL) -j $(PKGNAME) < ./$(PKGNAME).txt && dictzip $(PKGNAME).dict

install: $(PKGNAME).index $(PKGNAME).dict.dz
	install -Dm644 $(PKGNAME).index -t $(DESTDIR)/usr/share/dictd/
	install -Dm644 $(PKGNAME).dict.dz -t $(DESTDIR)/usr/share/dictd/

_clean:
	rm -f $(PKGNAME).{index,dict.dz,txt,csv}

clean: _clean
	rm -f $(CSVNAME)
	rm -f $(FILENAME)
