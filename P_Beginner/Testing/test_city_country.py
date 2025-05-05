from City_Country import *
def test_city_country():
    testing = info('Santiago', 'Chile')
    assert testing == "Santiago, Chile"

def test_city_country_population():
    testing = info("Santiago", "Chile", 5000000)
    assert testing == "Santiago, Chile - population = 5000000"