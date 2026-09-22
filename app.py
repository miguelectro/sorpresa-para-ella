from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

CONTRASENA = "biscochito"


@app.route("/", methods=["GET", "POST"])
def inicio():

    error = None

    if request.method == "POST":

        password = request.form.get("password")

        if password == CONTRASENA:
            return redirect(url_for("sorpresa"))

        else:
            error = "Prueba otra vez o no habrá popi para ti 🍪😂"

    return render_template(
        "index.html",
        error=error
    )


@app.route("/sorpresa")
def sorpresa():

    return render_template(
        "sorpresa.html"
    )


@app.route("/menu")
def menu():

    return render_template(
        "menu.html"
    )


@app.route("/carta")
def carta():

    return render_template(
        "carta.html"
    )


@app.route("/recuerdo")
def recuerdo():

    return render_template(
        "recuerdo.html"
    )


@app.route("/juego")
def juego():

    return render_template(
        "juego.html"
    )


@app.route("/sorpresa-final")
def sorpresa_final():

    return render_template(
        "sorpresa_final.html"
    )


if __name__ == "__main__":
    app.run(debug=True)