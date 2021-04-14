from flask import Flask
from bp.example import example_api_bp
from bp.utils.riot_api import riot_api_bp


app = Flask(__name__)
app.config.from_pyfile('config.cfg')

# api
app.register_blueprint(example_api_bp, url_prefix='/api/')

# utils
app.register_blueprint(riot_api_bp)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
