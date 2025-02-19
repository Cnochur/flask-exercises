from flask import Blueprint, render_template, redirect, request


views = Blueprint(__name__, "views")

tasks = []

@views.route("/")
def home():
    return render_template("index.html", content= tasks )


@views.route("/add_task/", methods= ["POST"])
def add_task():
    task_title = request.form["title"]
    task_description = request.form["description"]
    tasks.append({task_title: task_description})
    return redirect("/")


@views.route("/delete_task/<task_title>", methods=["POST"])
def delete_task(task_title):
    print(tasks)
    print(task_title)
    for ind, task in enumerate(tasks):
        for key, value in task.items():
            if task_title == key:
                print(key)
                tasks.pop(ind)
    return redirect("/")