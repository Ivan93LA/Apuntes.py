def user_schema(user) -> dict:
    return{"_id" : str(user)["_id"], #Hay que asegurarse de que se transforma en String
           "username" : user["username"],
           "email" : user["email"]}

