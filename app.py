from flask import Flask, render_template, request
import pandas as pd
import matplotlib

import matplotlib.pyplot as plt

app = Flask(__name__)

df = pd.read_csv("exoplanet_data.csv")


@app.route("/")
def home():

    planet_names = df["Planet Name"].unique()
    number_of_planets = df["Number of Planets"].unique()
    number_of_stars = df["Number of Stars"].unique()

    return render_template(
        "index.html",
        planet_names=planet_names,
        number_of_planets=number_of_planets,
        number_of_stars=number_of_stars
    )


@app.route("/results")
def results():

    planet_name = request.args.get("planet_name")
    number_of_planets = request.args.get("number_of_planets")
    number_of_stars = request.args.get("number_of_stars")
    output = request.args.get("output")

    planets = df.copy()

    if planet_name:
        planets = planets[
            planets["Planet Name"] == planet_name
        ]

    if number_of_planets:
        planets = planets[
            planets["Number of Planets"] == int(number_of_planets)
        ]

    if number_of_stars:
        planets = planets[
            planets["Number of Stars"] == int(number_of_stars)
        ]

    if planets.empty:

        return render_template(
            "error.html",
            e="No data available for the selected filters."
        )

    if output == "charts":

        return render_template(
            "viz.html",
            data=planets
        )

    return render_template(
        "results.html",
        data=planets
    )


@app.route("/viz")
def viz():

    planet_name = request.args.get("planet_name")
    number_of_planets = request.args.get("number_of_planets")
    number_of_stars = request.args.get("number_of_stars")

    data = df.copy()

    if planet_name:
        data = data[
            data["Planet Name"] == planet_name
        ]

    if number_of_planets:
        data = data[
            data["Number of Planets"] == int(number_of_planets)
        ]

    if number_of_stars:
        data = data[
            data["Number of Stars"] == int(number_of_stars)
        ]

    if data.empty:

        return render_template(
            "error.html",
            e="No data available for the selected filters."
        )

    data["Mass Earth"] = pd.to_numeric(
        data["Mass Earth"],
        errors="coerce"
    )

    data["Radius Earth"] = pd.to_numeric(
        data["Radius Earth"],
        errors="coerce"
    )

    data = data.dropna(
        subset=["Mass Earth", "Radius Earth"]
    )

    if data.empty:

        return render_template(
            "error.html",
            e="No numerical data available for visualization."
        )


    plt.figure()

    plt.hist(data["Radius Earth"])

    plt.xlabel("Radius Earth")
    plt.ylabel("Number of Planets")
    plt.title("Distribution of Planet Radius")

    plt.savefig("static/radius.png")

    plt.close()


    plt.figure()

    plt.hist(data["Mass Earth"])

    plt.xlabel("Mass Earth")
    plt.ylabel("Number of Planets")
    plt.title("Distribution of Planet Mass")

    plt.savefig("static/mass.png")

    plt.close()


    plt.figure()

    data["Number of Planets"].value_counts().sort_index().plot(
        kind="bar"
    )

    plt.xlabel("Number of Planets")
    plt.ylabel("Count")
    plt.title("Number of Planets")

    plt.savefig("static/planets.png")

    plt.close()


    plt.figure()

    data["Number of Stars"].value_counts().sort_index().plot(
        kind="bar"
    )

    plt.xlabel("Number of Stars")
    plt.ylabel("Count")
    plt.title("Number of Stars")

    plt.savefig("static/stars.png")

    plt.close()


    plt.figure()

    plt.scatter(
        data["Radius Earth"],
        data["Mass Earth"]
    )

    plt.xlabel("Radius Earth")
    plt.ylabel("Mass Earth")
    plt.title("Planet Mass vs Planet Radius")

    plt.savefig("static/mass_radius.png")

    plt.close()


    return render_template(
        "viz.html",
        data=data
    )


@app.route("/statistics")
def statistics():

    data = df.copy()

    data["Mass Earth"] = pd.to_numeric(
        data["Mass Earth"],
        errors="coerce"
    )

    data["Radius Earth"] = pd.to_numeric(
        data["Radius Earth"],
        errors="coerce"
    )

    data = data.dropna(
        subset=["Mass Earth", "Radius Earth"]
    )


    if data.empty:

        return render_template(
            "error.html",
            e="No numerical data available for statistics."
        )


    mass_mean = data["Mass Earth"].mean()

    mass_median = data["Mass Earth"].median()

    mass_mode = data["Mass Earth"].mode()[0]


    radius_mean = data["Radius Earth"].mean()

    radius_median = data["Radius Earth"].median()

    radius_mode = data["Radius Earth"].mode()[0]


    return render_template(
        "statistics.html",
        mass_mean=mass_mean,
        mass_median=mass_median,
        mass_mode=mass_mode,
        radius_mean=radius_mean,
        radius_median=radius_median,
        radius_mode=radius_mode
    )


@app.errorhandler(Exception)
def error(e):

    return render_template(
        "error.html",
        e=e
    )


app.run(debug=True, port=5000)
