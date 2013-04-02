# mockup-boot

My template to quickly build design prototypes. Made with Flask, Frozen-Flask and Flask-Flatpages.

## Project Setup

Setup virtualenv and install packages

	virtualenv _env
	_env/bin/pip install -r requirements.txt
	cd path/to/repo
	chmod a+x build.py

## Run Server
	chmod a+x build.py
	./build.py

## Generate Static Site
	./build.py build

## Features

Uses [Flask-Assets](http://elsdoerfer.name/docs/flask-assets/) with configured support for less and yui compression for css and js files. Other filters and configurations can be found [here](http://elsdoerfer.name/docs/webassets/builtin_filters.html).