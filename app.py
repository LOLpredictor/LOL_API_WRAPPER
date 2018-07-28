from flask import Flask, render_template, request

from .sources.lib.user.user import User
from .sources.lib.api import API
from utilities import Utility


app = Flask(__name__)


@app.route('/')
def index(name=None):
    return render_template('index.html')


@app.route('/searchUser',methods=['POST'])
def search_user():
    data = API().get_summoner(name=request.form['summoner_name'],localisation=request.form['platform'])
    user = User()
    user.user_from_riot_api(data)
    user.revisionDate = Utility.epoch_to_date_time(user.revisionDate)
    return render_template('show_user_profile.html',user=user)


if __name__ == '__main__':
    app.run()