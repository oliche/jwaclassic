#!/usr/bin/env bash
CHEM=/home/olivier/Documents/jwaclassic
SYNC_IMAGES=/home/olivier/OneDrive/_Flotte_JWA_Classic/00_images_site
rsync -av --progress  $SYNC_IMAGES/* $CHEM/images/
rm -fR ./_site
bundle exec jekyll build --config _config.yml --destination ./_site
