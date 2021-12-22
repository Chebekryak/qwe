from flask import Flask, redirect
import os
from data import db_session
from pages import main_page
from data.__all_models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chebekryak_secret_key'


@app.errorhandler(404)
def internal_error(error):
    return redirect('/')


def main():
    db_session.global_init("db/database.db")
    app.register_blueprint(main_page.blueprint)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    main()
    app.run(host='0.0.0.0', port=port)
