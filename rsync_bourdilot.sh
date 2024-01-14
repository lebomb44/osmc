#!/bin/bash

/usr/bin/rsync -av --progress --append-verify --files-from=/home/osmc/Movies/Bourdilot.txt /home/osmc/Movies/. -e "ssh -p 2205" osmc@bourdilot.tbd.tbd:/home/osmc/Movies/.

