from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class Event(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.Text, nullable=False)

    def __str__(self):
        return f'{self.id} {self.title}'

def event_serializer(event):
    return {
        'id' : event.id,
        'title' : event.title
    }

@app.route("/events")
def showEvents():
    return jsonify([*map(event_serializer, Event.query.all())])

if __name__ == "__main__":
    app.run()