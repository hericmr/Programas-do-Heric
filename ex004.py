h = input('Manda qulquer coisa digitada ai pra nois truta: ')
print(f'Mermão, você acaba de digitar: {h}')
print(f'O tipo primitivo da entrada {h} é', type(h))
print(f'{h} é uma entrada totalmente numerica?', h.isnumeric())
print(f'{h} é uma entrada totalmente alfa numerica?', h.isalnum())
print(f'{h} está em ASCII?', h.isascii())
print(f'{h} é uma entrada composta por letras alfabeticas?',h.isalpha())
print(f'{h} é digito?', h.isdigit())
print(f'{h} é decimal?' ,h.isdecimal())
print(f'{h} é identifier (seja la o que isso for)???', h.isidentifier())
print(f'A entrada {h} foi escrita totalmente caixa baixa???', h.islower())
print(f'{h} é uma entrada printavel?????', h.isprintable())
print(f'A entrada {h} só tem espaço?', h.isspace())
print(f'A entrada {h} está capitalizada?', h.istitle())
print(f'{h} é uma entrada escrita totalmente em letras maiusculas?', h.isupper())

