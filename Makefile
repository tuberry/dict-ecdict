pkg := ecdict
ver := 1.0.0
csv := ultimate.csv
zip := ecdict-ultimate-csv.zip
url := https://github.com/skywind3000/ECDICT-ultimate
aim := $(pkg).index $(pkg).dict.dz

# as brief as possible or not
MINI ?= true

.PHONY: all clean _clean

all: $(aim)

$(zip):
	curl -kLO $(url)/releases/download/$(ver)/$(zip)

$(pkg).csv: $(zip)
	unzip $(zip) && mv $(csv) $(pkg).csv && touch $(pkg).csv

$(pkg).txt: $(pkg).csv
ifeq ($(MINI),true)
	python ./$(pkg).py -i ./$(pkg).csv -o $(pkg).txt
else
	python ./$(pkg).py -i ./$(pkg).csv -o $(pkg).txt --no-mini
endif

$(aim) &: $(pkg).txt
	dictfmt --utf8 --allchars -s ECDICT -u $(url) -j $(pkg) < ./$(pkg).txt && dictzip $(pkg).dict

install: $(aim)
	install -Dm644 $(pkg).index -t $(DESTDIR)/usr/share/dictd/
	install -Dm644 $(pkg).dict.dz -t $(DESTDIR)/usr/share/dictd/

_clean:
	-rm $(pkg).{index,dict.dz,txt,csv}

clean: _clean
	-rm $(zip)

# vim: ts=2
