#!/usr/bin/env bash
CHEM=/home/olivier/Documents/jwaclassic
SYNC_IMAGES=/home/olivier/OneDrive/_Flotte_JWA_Classic/00_images_site
rsync -av --progress  $SYNC_IMAGES/* $CHEM/images/
bundle exec jekyll serve --config _config.yml,_config_dev.yml --destination ./_site
# docker-compose up