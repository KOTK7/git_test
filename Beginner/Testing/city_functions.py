def city_country(City, Country, Population=0):
    """returns a string with city and country"""
    if Population:
        formatted_city_country = f"{City}, {Country} - {Population}"
    else:
        formatted_city_country = f"{City}, {Country}"
    return formatted_city_country.title()
city_country("Santiago","Chile")