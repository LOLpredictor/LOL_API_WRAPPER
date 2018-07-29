from flask import Flask, render_template, request

from .sources.lib.user.user import User
from .sources.lib.api import API
from .sources.lib.user.championMastery import ChampionMastery
from utilities import Utility


app = Flask(__name__)


@app.route('/')
def index(name=None):
    return render_template('index.html')


@app.route('/searchUser',methods=['POST'])
def search_user():
    data = API().get_summoner(name=request.form['summoner_name'],localisation=request.form['platform'])
    user = User.user_from_riot_api(data)
    data_champions_mastery = API().get_all_champions_mastery(user.id,request.form['platform'])
    tab_cm = []
    for cm in ChampionMastery.top_3_champion_mastery(data_champions_mastery):
        print(cm)
        cham_mastery = ChampionMastery.champion_mastery_from_riot_api(cm)
        print(cham_mastery)
        cham_mastery.get_name_champion(request.form['platform'],'en_US')
        tab_cm.append(cham_mastery)

    return render_template('show_user_profile.html',user=user,championM=tab_cm)


if __name__ == '__main__':
    app.run()