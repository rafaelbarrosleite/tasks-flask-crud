from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_word():
    return "Hello Word!"

@app.route("/about")
def aboout():
    return "Página sobre"

#utilizado debug somente para rodar local o __main__ significa que está local sendo executado manualmente
if __name__== "__main__":
    app.run(debug=True)