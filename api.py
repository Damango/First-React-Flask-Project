from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET'])
def api():
    return{
        'userID': 1,
        'username': "Justin Kessler",
        'currentWeight': 155

    }



if __name__ == '__main__':
    app.run(debug=True)