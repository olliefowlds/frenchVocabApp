from flask import Flask, render_template, url_for, session, request, redirect

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():

    if request.method == "POST":
        topicSelect = request.form.get("topicSelect")
        print(topicSelect)

    return render_template("home.html")

if __name__ == "__main__":
    app.run(debug=True)