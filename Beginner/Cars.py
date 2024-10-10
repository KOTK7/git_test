def make_car(manufacturer, model_name, **car_info):
    car_info["manu"] = manufacturer
    car_info["model"] = model_name
    return car_info
car = make_car('subaru', 'outback', color='blue', tow_package=True)
print(car)