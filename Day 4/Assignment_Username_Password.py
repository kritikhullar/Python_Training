
#User Defined Exception
class InvalidCredentials(Exception):
    def __init__(self,msg="Invalid Credentials Provided!"):
        Exception.__init__(self,msg)
try:
    creds={
        "Rakesh":"rakesh",
        "Venkat":"venkat",
        "Naveen":"naveen"}
    
    u_name=input("Enter Username: ")
    password = input("Enter Password: ")
    
    if u_name not in creds or password not in creds[u_name]:
        raise InvalidCredentials
    print("Welcome ",u_name)

    
except InvalidCredentials as e:
    print(e)
except Exception as e:
    print("Generic Handler! ",e)


