def info(city, country, population=''):
    if population:
        full_info = f'{city}, {country} - population = {population}'
    else:
        full_info =  f'{city}, {country}'
    return full_info