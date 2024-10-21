from city_functions import city_country
def test_city_country():
    """test the function"""
    function_testing = city_country("Santiago","Chile")
    assert function_testing == "Santiago, Chile"
def test_city_country_population():
    """test the function in addition to population"""
    function_testing = city_country("Santiago","Chile", 500000)
    assert function_testing == "Santiago, Chile - 500000"