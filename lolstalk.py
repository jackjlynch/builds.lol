from flask import Flask
from riotwatcher.riotwatcher import RiotWatcher

app = Flask(__name__)

riot_api = None

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/userinfo/<username>')
def user_info(username):
    return str(riot_api.get_summoner(name=username)['id'])


if __name__ == '__main__':
    app.debug = True
    app.config.from_pyfile('dev.cfg')
    riot_api = RiotWatcher(app.config['API_KEY'])
    app.run()
