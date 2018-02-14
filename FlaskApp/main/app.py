from flask import Flask, render_template, request
import settings
from sources.lib.api import API
from sources.lib.champion.champion import Champion

"""
    Pour connaitre les processus qui tournent : ps -ef | grep python
    Pour éteindre un des processus : kill -9 xxx  remplacer les x par l'id

"""

app = Flask(__name__)

@app.route("/")
def main():
    print("salut")
    return render_template('index.html')

@app.route("/champ")
def showSignUp():
    champions = []
    api = API(settings.API_KEY)
    champions = api.get_champions_data()
    for i in champions:
        champion = i
        if(champion.name == request.args.get('championName')):
            print("name")
            name = champion.name
    print("Request : " + request.method)
    return render_template('index.html')

if __name__ == "__main__":
    app.run()

