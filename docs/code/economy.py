economic_data = {
    "United States": {
        "GDP %": {
            "latest": 3.0,
            "quarter": 3.5,
            "2018": 2.9,
        },
        "Consumer prices %": {
            "latest": 2.3,
            "2018": 2.5,
        },
        "Unemployment rate %": {
            "latest": 3.7,
        },
    },
    "China": {
        "GDP %": {
            "latest": 6.5,
            "quarter": 6.6,
            "2018": 6.6,
        },
        "Consumer prices %": {
            "latest": 2.5,
            "2018": 2.1,
        },
        "Unemployment rate %": {
            "latest": 3.8,
        },
    },
    "Japan": {
        "GDP %": {
            "latest": 1.3,
            "quarter": 3.0,
            "2018": 1.0,
        },
        "Consumer prices %": {
            "latest": 1.2,
            "2018": 0.9,
        },
        "Unemployment rate %": {
            "latest": 2.3,
        },
    },
    "Britain": {
        "GDP %": {
            "latest": 1.2,
            "quarter": 1.6,
            "2018": 1.3,
        },
        "Consumer prices %": {
            "latest": 2.4,
            "2018": 2.4,
        },
        "Unemployment rate %": {
            "latest": 4.0,
        },
    },
}

usa_economic_data = {country: data for country, data in economic_data.items() if country == "United States"}
