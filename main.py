from flask import Flask

from pages import main_page, registration, test, results

app = Flask(__name__)


def main():
    app.register_blueprint(main_page.blueprint)
    app.register_blueprint(registration.blueprint)
    app.register_blueprint(test.blueprint)
    app.register_blueprint(results.blueprint)
    app.run()


if __name__ == '__main__':
    main()