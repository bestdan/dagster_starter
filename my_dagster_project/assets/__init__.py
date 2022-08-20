import csv

import requests
from dagster import asset


@asset
def poo_face_ezra():
    response = requests.get("https://docs.dagster.io/assets/cereal.txt")
    lines = response.text.split("\n")
    cereal_rows = [row for row in csv.DictReader(lines)]

    return cereal_rows


@asset
def crazy_face(cereals):
    """Cereals manufactured by Nabisco"""
    return [row for row in cereals if row["mfr"] == "N"]
