from flask import Flask, request,g,redirect, url_for, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_mail import Mail
from app.config import Config
from flask_babel import Babel
from flask_babelex import Babel

babel = Babel( default_locale='fr')
db = SQLAlchemy()
bcrypt = Bcrypt()
mail = Mail()


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(Config)
    db.init_app(app)
    bcrypt.init_app(app)
    mail.init_app(app)
    mail.init_mail(app.config)
    babel.init_app(app)


    from app.main.routes import main
    from app.errors.handlers import errors
    from app.contact.routes import contact
    app.register_blueprint(main)
    app.register_blueprint(contact)
    app.register_blueprint(errors)

    @babel.localeselector
    def get_locale():
        if not g.get('lang_code', None):
            g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
        return g.lang_code

    @app.route('/')
    def start():
        g.lang_code = 'fr'
        return redirect(url_for('main.home'))

    return app