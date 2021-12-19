from flask import Blueprint
from flask import render_template, request

blueprint = Blueprint(
    'main_page', __name__,
    template_folder='templates',
    static_folder='static'
)


@blueprint.route('/')
def main_page():
    return render_template('main.html', title="Главная")


@blueprint.route('/registration/')
def registration():
    return render_template('registration.html', title="Выбор класса")


@blueprint.route('/test/<string:_class>', methods=['GET', 'POST'])
def test(_class):
    test_test = [{"id": 1, "text": "текст", "picture": "images/1.png", "answers": ["1", "2", "3", "4", "5"],
                  "right_answer": '1'},
                 {"id": 2, "text": "тексттексттекстекст", "picture": None, "answers": ["a", "b", "c", "d", "e"],
                 "right_answer": 'a'},
                 {"id": 3, "text": "тексттекст", "picture": None, "answers": ["а", "б", "в", "г", "д"],
                  "right_answer": 'а'}]
    if request.method == 'GET':
        return render_template('test.html', title="Тест", _class=_class, test=test_test)
    elif request.method == 'POST':
        c = 0
        for i in range(1, len(test_test) + 1):
            if request.form.get(f'{i}') == test_test[i - 1]["right_answer"]:
                c += 1
        return results(c / len(test_test) * 100)


@blueprint.route('/results/')
def results(res):
    return render_template('results.html', title="Результаты", res=res)
