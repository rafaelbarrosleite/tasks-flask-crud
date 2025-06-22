from flask import Flask, request, jsonify
from models.task import Task
app = Flask(__name__)

#CRUD - Create, Read, Update e Delete

tasks = []
task_id_control = 1
@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(id= task_id_control, title=data['title'], description=data.get("description", ""))
    print(data)
    task_id_control += 1
    tasks.append(new_task)
    print(tasks)
    ##return "Nova tarefa criada com sucesso"
    return jsonify({"messagem": "Nova tarefa criada com sucesso"})

#utilizado debug somente para rodar local o __main__ significa que está local sendo executado manualmente
if __name__== "__main__":
    app.run(debug=True)