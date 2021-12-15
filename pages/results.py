from flask import Blueprint
from flask import render_template

blueprint = Blueprint(
    'results', __name__,
    template_folder='templates'
)


@blueprint.route('/results/')
def results():
    return render_template('results.html')