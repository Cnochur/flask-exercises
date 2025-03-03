from flask import Flask

app = Flask(__name__)

from views.index import index
from views.projects import projects
from views.contact import contact


app.register_blueprint(index, url_prefix="/")
app.register_blueprint(projects, url_prefix="/projects/")
app.register_blueprint(contact, url_prefix="/contact/")


if __name__ == "__main__":
    app.run(debug=True)