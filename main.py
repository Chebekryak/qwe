from flask import Flask

from pages import main_page

app = Flask(__name__)


def main():
    app.register_blueprint(main_page.blueprint)
    app.run()


if __name__ == '__main__':
    main()
