
from flask import Flask

app = Flask(_name_)

@app.route('/')
def home():
    return 'hello world'


if _name_ == '_main_':
    app.run()
