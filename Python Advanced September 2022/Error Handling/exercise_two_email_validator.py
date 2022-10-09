
class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolError(Exception):
    pass


email = input()

while email != "End":

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")
    if email.count('@') > 1:
        raise MoreThanOneAtSymbolError("Email should contain only one @")

    # Unpacking the username and the host+domain
    username, host_and_domain = email.split('@')

    # Checks if the length of the username is more than 4 chars
    if len(username) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    # Checks if the host_and_domain variable doesn't end with the provided valid domains
    elif not (host_and_domain.endswith('.com') or host_and_domain.endswith('.bg')
              or host_and_domain.endswith('.org') or host_and_domain.endswith('.net')):
        raise InvalidDomainError(f"Domain must be one of the following: .com, .bg, .org, .net")

    # If no exceptions were raised...
    print("Email is valid")

    email = input()




