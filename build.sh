#!/bin/bash

FEDORA_RELEASE=$(grep VERSION_ID /etc/os-release | cut -d"=" -f2 -)

fedpkg --release f$FEDORA_RELEASE mockbuild

