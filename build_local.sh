CHEM=/home/olivier/Documents/jwaclassic
DROPBOX_IMAGES=/home/olivier/Dropbox/#_Site_internet_JWA/Images
rsync -av --progress  $DROPBOX_IMAGES/* $CHEM/images/
# bundle exec jekyll serve --config _config.yml,_config_dev.yml --destination ./_site

docker-compose up