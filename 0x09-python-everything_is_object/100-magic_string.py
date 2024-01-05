def magic_string():
    magic_string.c = getattr(magic_string, 'count', 0) + 1
    return "BestSchool" + ", BestSchool" * (magic_string.c - 1)

