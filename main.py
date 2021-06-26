import requests


print('-------------------------')
print('#####Consulta CEP #######')
print('-------------------------')
print()

cep_input = input('Digite o CEP para consulta')

if len(cep_input) != 8:
    print('Quantidade de digitos invalida')
    exit()
request = requests.get('https://viacep.com.br/ws/{}/json/'.format(cep_input))

address_data = request.json()

if 'erro' not in address_data:
    print('--CEP ENCONTRADO--')
    print('CEP: {}'.format(address_data['cep']))
    print('Cidade: {}'.format(address_data['localidade']))
    print('Logradouro: {}'.format(address_data['uf']))

else:
    print('CEP invalido.'.format(cep_input))

option = int (input('Deseja realizar um nova consulta?\n1. Sim\n2 Sair'))
