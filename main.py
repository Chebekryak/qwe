from flask import Flask

from data import db_session
from pages import main_page
from data.__all_models import *

app = Flask(__name__)
app.config['SECRET_KEY'] = 'chebekryak_secret_key'


def main():
    db_session.global_init("db/database.db")
    #
    # db_sess = db_session.create_session()
    #
    # q = Question()
    # q.id_class = 1
    # q.text = "Федя шифрует слово МАРКА." \
    #          " Разные буквы он заменяет на разные цифры," \
    #          " а одинаковые буквы — на одинаковые цифры. Что у него могло получиться?"
    # q.image = ""
    # q.points = 4
    # db_sess.add(q)
    #
    # listok = [(5, "12345", False),
    #           (5, "12343", False),
    #           (5, "12312", False),
    #           (5, "12321", False),
    #           (5, "12342", True)]
    # for i in listok:
    #     a = Answer()
    #     a.id_question = i[0]
    #     a.body = i[1]
    #     a.status = i[2]
    #     db_sess.add(a)
    # db_sess.commit()
    app.register_blueprint(main_page.blueprint)
    app.run()


if __name__ == '__main__':
    main()
