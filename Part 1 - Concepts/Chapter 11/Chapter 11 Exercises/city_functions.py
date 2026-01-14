def get_formatted_city_country(city, country, population=None):
    """Return a formatted string in the form: city, country - population population."""
    if population:
        formatted_city_country = (
            f"{city.title()}, {country.title()} - population {population}"
        )
    else:
        formatted_city_country = f"{city.title()}, {country.title()}"

    return formatted_city_country
