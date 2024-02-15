from flask import Flask, render_template, jsonify

app = Flask(__name__)

BOOKS =[
    {
        "id":1,
        "title":"Book 1",
        "genre":"Sus"
    },
    {
        "id":2,
        "title":"Book 2",
        "genre":"Romcom"
    },
    {
        "id":3,
        "title":"Book 3",
        "genre":"Sus"
    },
    {
        "id":4,
        "title":"Book 4",
        "genre":"Romcom"
    }
]

@app.route("/")
def hello_world():
    return render_template("home.html", books=BOOKS, creator="Me")


@app.route("/api/books")
def list_jobs():
    return jsonify(BOOKS)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)