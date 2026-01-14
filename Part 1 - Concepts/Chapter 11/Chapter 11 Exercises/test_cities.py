from city_functions import get_formatted_city_country


def test_city_country():
    """Does the function work correctly for 'santiago, chile'?"""
    formatted_city_country = get_formatted_city_country("santiago", "chile")

    assert formatted_city_country == "Santiago, Chile"


def test_city_country_population():
    """Does the function work correctly for 'santiago, chile, 5000000'?"""
    formatted_city_country_population = get_formatted_city_country(
        "santiago", "chile", 5000000
    )

    assert formatted_city_country_population == "Santiago, Chile - population 5000000"
