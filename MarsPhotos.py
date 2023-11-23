from flask import Flask, render_template
import requests
import json

apoc_url_url = "https://api.nasa.gov/planetary/apod?api_key=jrhqOnOsdsUHJ5q86Sl5yQtzIdrjhYut0Cceb6wB"

def getUrl():
    response = requests.get(apoc_url_url)
    json_data = response.json()
    return json_data   #.get('url','')   #json_data['url']


app = Flask(__name__)


@app.route('/')
def home_page():

    webimage = getUrl()
    return render_template('home.html'
                        ,imgurl=webimage.get('url')
                        ,pageHeader=webimage.get('title')
                        ,desc=webimage.get('explanation')
                        )
    
    # imgtag = "<IMG src='" + webimage.get('url','') + "' style='width:200px;'></IMG>" 
    
    # myresponse = '<h1>Our Awesome Nasa Website:)!!!!!!</h1><br/>' 
    # myresponse += '<h2>'+webimage.get('title','')+'</h2>'
    # myresponse += imgtag
    # myresponse += '<p>'+webimage.get('explanation','')+'</p>'
    
    # return myresponse

# if __name__ == "__main__":
#     app.run()

#export FLASK_APP='MarsPhotos'
#export FLASK_ENV=development
# flash run

# Hit Ctrl-<Click> on http://127.0.0.1:5000
#   

# python3 -m pip install requests
#APi key: jrhqOnOsdsUHJ5q86Sl5yQtzIdrjhYut0Cceb6wB
#GET https://api.nasa.gov/planetary/apod 