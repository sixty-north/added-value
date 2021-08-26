import json

countries = [
    dict(
        name="Denmark",
        code="DK",
        area_km2=42933,
        population_millions=5.85,
        currency="DKK",
    ),
    dict(
        name="Norway",
        code="NO",
        area_km2=385207,
        population_millions=5.39,
        currency="NOK",
    ),
    dict(
        name="Sweden",
        code="SE",
        area_km2=450295,
        population_millions=10.40,
        currency="SEK",
    )
]

json_countries = json.dumps(countries, indent=2)
