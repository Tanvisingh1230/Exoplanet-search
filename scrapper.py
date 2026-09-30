import requests
from bs4 import BeautifulSoup
import pandas as pd
import csv

url = "https://openexoplanetcatalogue.com/systems/"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/149.0.0.0 Safari/537.36 Edg/149.0.0.0"
}

resp = requests.get(url, headers=header)

print(resp)

soup = BeautifulSoup(resp.content)

tables = soup.find_all("table")

table = tables[2]

rows = table.find_all("tr")

planet_name = []
mass = []
radius = []
mass_earth = []
radius_earth = []
number_of_planets = []
number_of_stars = []

for row in rows:

    data = row.find_all("td")

    if len(data) > 0:

        planet_name.append(data[0].text.strip())
        mass.append(data[1].text.strip())
        radius.append(data[2].text.strip())
        mass_earth.append(data[3].text.strip())
        radius_earth.append(data[4].text.strip())
        number_of_planets.append(data[5].text.strip())
        number_of_stars.append(data[6].text.strip())

df = pd.DataFrame({
    "Planet Name": planet_name,
    "Mass": mass,
    "Radius": radius,
    "Mass Earth": mass_earth,
    "Radius Earth": radius_earth,
    "Number of Planets": number_of_planets,
    "Number of Stars": number_of_stars
})

with open("exoplanet_data.csv", "w") as file:

    writer = csv.writer(file)

    writer.writerow([
        "Planet Name",
        "Mass",
        "Radius",
        "Mass Earth",
        "Radius Earth",
        "Number of Planets",
        "Number of Stars"
    ])

    for i in range(len(planet_name)):

        writer.writerow([
            planet_name[i],
            mass[i],
            radius[i],
            mass_earth[i],
            radius_earth[i],
            number_of_planets[i],
            number_of_stars[i]
        ])

print("Data saved")