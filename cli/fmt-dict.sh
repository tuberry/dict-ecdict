#!/bin/bash
# by tuberry
#

dictfmt "$@" $PKG < ./$PKG.txt && dictzip $PKG.dict
