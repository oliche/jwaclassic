#!/usr/bin/env bash
rm -fR ./www
bundle exec jekyll build --config _config.yml --destination ./www


