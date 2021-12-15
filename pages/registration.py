from flask import Blueprint
from flask import render_template

blueprint = Blueprint(
    'registration', __name__,
    template_folder='templates'
)


@blueprint.route('/registration/')
def registration():
    return render_template('registration.html')