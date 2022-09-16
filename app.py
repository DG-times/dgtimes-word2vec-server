from flask import Flask

import src.word2vec_controller as controller

app = Flask(__name__)
app.register_blueprint(controller.app)


if __name__ == '__main__':
    app.run('0.0.0.0', port=5000, debug=True)
