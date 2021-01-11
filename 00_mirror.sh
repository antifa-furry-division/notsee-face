#!/usr/bin/env bash

# https://twitter.com/_IntelligenceX/status/1346967229187952644?s=20
lftp  ftp://ftp.intelx.io <<- DOWNLOAD
    set ftp:ssl-allow false
    user Capitol ""
    mirror .
DOWNLOAD
