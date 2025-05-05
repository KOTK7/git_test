def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info


user_profile = build_profile('Jake', 'Paul',
    location='USA',
    field='Conten Creation')

for key, value in user_profile.items():
    print(f'-{key} : {value}')