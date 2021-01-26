from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///tmp/test.db'
db = SQLAlchemy(app)



class UserData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    currentWeight = db.Column(db.Integer, nullable=False)
    name = db.Column(db.Text, nullable=False)

    
    def __str__(self):
        return f'{self.id}, {self.currentWeight}, {self.name}'


def userData_serializer(userdata):
    return{
        'id': userdata.id,
        'currentWeight': userdata.currentWeight,
        'name':userdata.name
    }


@app.route('/api', methods=['GET'])
def api():
    return{
        'userID': 100,
        'username': "Justin Kessler",
        'currentWeight': 155
    }



@app.route('/test', methods=['GET'])
def testApi():
    return{
        'userID':69,
        'username': "Spooby Looby",
        'currentWeight': 255
    }


@app.route('/test2', methods=['GET'])
def testApi2():
    

    return jsonify([*map(userData_serializer, UserData.query.all())])



if __name__ == '__main__':
    app.run(debug=True)