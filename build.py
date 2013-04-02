#!../_env/bin/python
import sys

from flask import Flask, render_template
from flask_flatpages import FlatPages
from flask_frozen import Freezer
from flask.ext.assets import Environment, Bundle

DEBUG = True
FLATPAGES_AUTO_RELOAD = DEBUG
FLATPAGES_EXTENSION = '.md'

app = Flask(__name__)
app.config.from_object(__name__)
pages = FlatPages(app)
freezer = Freezer(app)
assets = Environment(app)

# ASSETS
less = Bundle('less/main.less', filters='less,yui_css', output='css/main.css')
js = Bundle('js/main.js', filters='yui_js', output='js/main-min.js')
assets.register('css', less)
assets.register('js_all', js)

# ROUTES
@app.route('/')
def index():
	return render_template('index.html', pages=pages)

@app.route('/<path:path>/')
def page(path):
	page = pages.get_or_404(path)
	template = page.meta.get('template', 'page.html')
	return render_template(template, page=page)

if __name__ == '__main__':
	if len(sys.argv) > 1 and sys.argv[1] == "build":
		freezer.freeze()
	else:
		app.run(port=8000)