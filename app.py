from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
# from requests import request

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
db = SQLAlchemy(app)

class TODO(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    content = db.Column(db.String(200), nullable = False)
    completed = db.Column(db.Integer, default = 0)
    created  = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self):
        return super().__repr__('<Task %r>'% self.id)

@app.route('/', methods = ['POST', 'GET'])
def index():
    if request.method == 'POST':
        content = request.form['content']
        new_task = TODO(content = content)
        return content
        try:
            db.session.add(new_task)
            db.session.commit()
            return redirect('/')
        except Exception as e:
            print('There was some issue')
    else:
    # return 'Hello  world'
        return render_template('index.html')

if __name__ == '__main__':
    app.run(debug= True)