#!/bin/bash
# by tuberry

curl -kLO $URL/$VER/$ZIP && unzip $ZIP && mv ultimate.csv $PKG.csv && rm $ZIP
