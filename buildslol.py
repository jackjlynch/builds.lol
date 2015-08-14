from flask import Flask
from flask import render_template
from riotwatcher.riotwatcher import RiotWatcher

app = Flask(__name__)

riot_api = None
items = None
dd_urls = {}

@app.route('/')
def index():
    return app.send_static_file('index.html')

@app.route('/items')
def items():
    return render_template('items.html', items=items['data'], dd_url=dd_urls['na'])

@app.route('/userinfo/<username>')
def user_info(username):
    game = riot_api.get_current_game(riot_api.get_summoner(name=username)['id'])
    return render_template('items.html', participants=game['participants'])

if __name__ == '__main__':
    app.debug = True
    app.config.from_pyfile('dev.cfg')
    riot_api = RiotWatcher(app.config['API_KEY'])
    items = riot_api.static_get_item_list()

    for region in ['br', 'eune', 'euw', 'kr', 'lan', 'las', 'na', 'oce', 'ru', 'tr']:
        data = riot_api.static_get_realm(region)
        dd_urls[region] = data['cdn'] + '/' + data['v']
    app.run()
