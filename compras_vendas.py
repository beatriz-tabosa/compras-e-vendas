# Boa noite professor, segue abaixo o programa em texto e em anexo o programa em .txt
print('Olá! Seja Bem-vindo!')

purchases = []
sales = []

def get_string_input(message, error):
  while True:
    data = input(message)
    if not (data.strip()):
      print(error)
      continue
    break
  return data


def get_integer_input(message, error):
  while True:
    data = input(message)
    if not (data.isdigit()):
      print(error)
      continue
    break
  return int(data)


def get_float_input(message, error):
  while True:
    data = input(message)
    try:
      float(data)
    except ValueError:
      print(error)
      continue
    break
  return float(data)


def get_menu_option():
  menu_options = ('1', '2', '3', '4')

  while True:
    print()
    print('\t* Menu *')
    print()
    print('[1] Registrar venda')
    print('[2] Registrar compra')
    print('[3] Consultar saldo de vendas')
    print('[4] Sair')
    print()

    user_input = input('Escolha uma das opções: ')
    print()

    if user_input in menu_options:
      return user_input

    else:
      print()
      print(
          '\t* Opção inválida! *\n Por favor, selecione uma das opções disponíveis abaixo :) ')


while True:
  user_input = get_menu_option()

  if user_input == '1':
    product_name = get_string_input('Insira o nome do produto: ', 'O nome do produto não pode ser vazio! Por favor, insira um nome válido :)')

    price = get_float_input('Insira o valor do produto: ', 'O valor do produto deve ser um número. Por favor, insira um valor válido. :)')

    quantity = get_integer_input('Insira a quantidade: ', 'A quantidade deve ser um número. Por favor, insira uma quantidade válida. :)')

    sales.append({
      'name': product_name,
      'price': price,
      'quantity': quantity
    })

  elif user_input == '2':
    product_name = get_string_input('Insira o nome do produto: ', 'O nome do produto não pode ser vazio! Por favor, insira um nome válido :)')

    price = get_float_input('Insira o valor do produto: ', 'O valor do produto deve ser um número. Por favor, insira um valor válido. :)')

    quantity = get_integer_input('Insira a quantidade: ', 'A quantidade deve ser um número. Por favor, insira uma quantidade válida. :)')

    purchases.append({
      'name': product_name,
      'price': price,
      'quantity': quantity
    })

  elif user_input == '3':
    print()
    total_sales = 0
    total_purchases = 0

    for purchase in purchases:
      total_purchases = total_purchases + float(purchase.get('price')) * float(purchase.get('quantity'))

    for sale in sales:
      total_sales = total_sales + float(sale.get('price')) * float(sale.get('quantity'))

    final_total = round(total_sales - total_purchases, 2)

    print('* Seu saldo de vendas *\t')
    if final_total > 0:
      print(f"Lucro: R$ {final_total}")
    elif final_total == 0:
      print()
      print(f"R$ {final_total}")
    else:
      print(f"Prejuízo: R$ {final_total}")
 
  elif user_input == '4':
    print()
    print('Até a próxima! :)')
    exit()