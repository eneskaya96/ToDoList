from flask_swagger_ui import get_swaggerui_blueprint
from flask import Flask
from routes import request_api
from models import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///todo.db'

db.init_app(app)

### swagger specific ###
SWAGGER_URL = '/swagger'
API_URL = '/static/swagger3.json'
SWAGGERUI_BLUEPRINT = get_swaggerui_blueprint(
    SWAGGER_URL,
    API_URL,
    config={
        'app_name': "TODO-Python-Flask-REST"
    }
)
app.register_blueprint(SWAGGERUI_BLUEPRINT, url_prefix=SWAGGER_URL)
### end swagger specific ###
app.register_blueprint(request_api.get_blueprint())

if __name__ == "__main__":
    app.run(debug=True)