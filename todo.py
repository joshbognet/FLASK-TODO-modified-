from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
 
app = Flask(__name__)



# Conneccting database_file(todo.db) to SQLAlchemy dependencies
app.config["SQLALCHEMY_DATABASE_URI"] ='sqlite:///db.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"]= False


db = SQLAlchemy(app)

class Todo(db.Model):
    id = db.Column(db.Integer, unique=True, primary_key=True, nullable=False) 
    title= db.Column(db.String(60), unique=False, nullable =False)
    date=db.Column(db.DateTime, default=datetime.utcnow)



@app.route("/", methods = ['GET', 'POST'])
def index():
    if request.form:
        new_todo= request.form.get('new_todo')

        todo = Todo(title = new_todo)
        db.session.add(todo)
        db.session.commit()
    todos = Todo.query.all() 
    return render_template("index.html", todos = todos)


"""
***#NOTE***
Also check  Html to see form 

@app.route('/edit', methods=['POST'])  #performs the update function
def edit(): 
edit_todo=request.form.get('edit_todo')   # this represents the edit input from the form
  old_todo= request.form.get('old_todo')   # this represents the item to be updated/edited   
     item = Todo.query.filter_by(title=old_todo).first()  #this queries the db to retrieve the specific item to be updated/edited by its title
         item.title=edit_todo   #this updates/edits the old todo to the new todo

    return redirect('/') # redirect to index page
"""


@app.route("/edit", methods = ["POST"])
def edit():
    edit_todo = request.form.get('edit_todo')
    old_todo = request.form.get('old_todo')
    todo = Todo.query.filter_by(title=old_todo).first()
    todo.title=edit_todo
    db.session.commit()
    return redirect('/')
    

@app.route('/delete', methods=["POST"])
def delete():
    title=request.form.get('title') #
    todo=Todo.query.filter_by(title=title).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect('/')


if __name__ == "__main__":
    db.create_all()
    
    
    app.run(debug = True)
    