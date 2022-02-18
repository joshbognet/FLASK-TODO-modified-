from crypt import methods
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html", todos = todo_data)


todo_data = [] #stores data entered


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




if __name__ == "__main__":
    app.run(debug = True)