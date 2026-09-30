# Exoplanet Explorer

Exoplanet Explorer is a Flask-based web application that collects, analyzes, and presents information about exoplanets in an interactive and easy-to-understand way.

## Features

- Collects exoplanet data using web scraping
- Displays exoplanet information
- Performs basic data analysis using Pandas
- Provides statistical information about the dataset
- Includes data visualizations using Matplotlib
- Interactive web interface built with Flask
- Handles errors through a dedicated error page

## Technologies Used

- Python
- Flask
- Pandas
- Matplotlib
- BeautifulSoup
- Requests
- HTML
- CSS

## Project Structure

```text
Exoplanet-search/
│
├── app.py
├── scrapper.py
├── exoplanet_data.csv
├── requirements.txt
│
├── static/
│   ├── images/
│   ├── mass.png
│   ├── mass_radius.png
│   ├── planets.png
│   ├── radius.png
│   ├── stars.png
│   └── style.css
│
└── templates/
    ├── index.html
    ├── results.html
    ├── statistics.html
    ├── viz.html
    └── error.html