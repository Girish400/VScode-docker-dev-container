
def http_error(status):
    match status:
        case 400:
            return "Bad request"
        case 404:
            return "Not found"
        case 418:
            return "I'm a teapot"
        case _:
            return "Something's wrong with the internet"

def http_error1(status):
    match status:
        case 401 | 403 | 404:
            return "Not allowed"
            
print(http_error(404))
print(http_error1(404))
