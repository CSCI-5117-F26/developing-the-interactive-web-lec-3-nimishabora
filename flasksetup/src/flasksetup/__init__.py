from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
names: list[str] = []


@app.route("/", methods=["GET", "POST"])
def guestbook():
    if request.method == "POST":
        name = request.form.get("name", "").strip()
        if name:
            names.append(name)
        return redirect(url_for("guestbook"))

    return render_template("index.html", names=names)


def main() -> None:
    app.run(debug=True)
