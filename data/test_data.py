def courier_missing_login():
    return ["", "password", "first name"]

def courier_missing_password():
    return ["login", "", "first name"]

def courier_missing_firstname():
    return ["login", "password", ""]

def courier_login_missing_login():
    return ["", "password"]

def courier_login_missing_password():
    return ["login", ""]

def invalid_login_data():
    return {"login": "wrong_user", "password": "wrong_pass"}

def first_color():
    return ["BLACK"]

def second_color():
    return ["GREY"]

def both_colors():
    return ["BLACK", "GREY"]
