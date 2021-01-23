from flask import Flask

app = Flask(__name__)


@app.route('/api', methods=['GET'])
def api():
    return{
        'userID': 1,
        'username': "Justin Kessler",
        'currentWeight': 155

    }



@app.route('/test', methods=['GET'])
def testApi():
    return[{
        'userID':69,
        'username': "Spooby Looby",
        'currentWeight': 255
    }]



if __name__ == '__main__':
    app.run(debug=True)