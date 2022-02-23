from flask import Flask, redirect, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


db = SQLAlchemy(app)

class Todo(db.Model):
    todo_item = db.Column(db.String(60))

@app.route("/")
def index():
    return render_template("index.html", todos = todo_data)


todo_data = [] #stores data entered
update = []


@app.route("/create-todo", methods=["POST"])
def create_todo():
    new_todo = request.form.get("new_todo") #create a variable that stores form data
    todo_data.append(new_todo) # appends data to an array
    # print(todo_data) #prints array of things to do
    return redirect(url_for("index")) #redirects back to the index page



@app.route('/delete/<todo_item>')
def delete(todo_item):
    todo_data.remove(todo_item)

    return redirect(url_for("index"))

item = ''
@app.route('/update/<todo_item>', methods=['GET','POST']) #renders page to update
def update(todo_item):

    index = todo_data.index(todo_item) #gets index of item to be changed

    global item     # make this variable global(accessible outside this scope)
    item = index    

    return render_template('update.html', todo_item = todo_item) # render and take todo_item
    

@app.route('/update_item', methods=['POST'])  #performs the update function
def update_item():
    if request.method == 'POST':
        new_item = request.form.get('new_item')  #get that particular item u just updated from the form
        todo_data[item] = new_item  # set the new item to index of the old item to replace the old one

    return redirect(url_for('index')) # redirect to index page


if __name__ == "__main__":
    app.run(debug = True)