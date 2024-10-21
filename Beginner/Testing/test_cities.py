from city_functions import city_country
def test_city_country():
    """test the function"""
    function_testing = city_country("Santiago","Chile")
    assert function_testing == "Santiago, Chile"