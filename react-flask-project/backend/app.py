from flask import Flask
from flask_cors import CORS
from routes import notes_bp
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
CORS(app)

db.init_app(app)
app.register_blueprint(notes_bp, url_prefix='/api/notes')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
