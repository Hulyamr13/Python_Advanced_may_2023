class NameTooShortError(Exception):
    pass

class MustContainAtSymbolError(Exception):
    pass

class InvalidDomainError(Exception):
    pass

while True:
    email = input()

    if email == "End":
        break

    if len(email.split("@")[0]) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if "@" not in email:
        raise MustContainAtSymbolError("Email must contain @")

    domain = email.split(".")[-1]
    valid_domains = [".com", ".bg", ".org", ".net"]
    if domain not in valid_domains:
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    print("Email is valid")
