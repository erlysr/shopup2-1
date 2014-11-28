import re


def rm_double_space(string):
    return re.sub(' +', ' ', string).strip().title()


# str.title()  --> Primeras letras de frase en Mayus
# str.strip() --> Trim
