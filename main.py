from flask import Flask, render_template, request

class Todo():
    def __init__(self, id:int, title:str, status:bool) -> None:
        self.id = id
        self.title = title
        self.status = status

todos = []

app = Flask(__name__, template_folder="templates", static_folder="staticFiles")

@app.route("/")
def home():
    return render_template("home.html", todos=todos)

@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
            id = len(todos) + 1
            title = request.form.get("title")
            todos.append(Todo(id, title, False))
            return render_template("home.html", todos=todos)
    
@app.route("/remove/<int:todo_id>")
def remove(todo_id):
    for todo in todos:
        if(todo.id == todo_id):
            todos.remove(todo)

    return render_template("home.html", todos=todos)