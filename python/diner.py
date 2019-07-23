def menu_talk():
  while True:
    print('Hi, welcome to Bottegas exotic diner! Would you like to see our menu items for this evening?')
    conversation = input()

    if conversation == 'yes':
      print(menu_items)
      break
    else:
      print('Okay, let me know when you are ready!')
      conversation = input()

def order_entrees():
    entry = input('What would you like to order as your entree this evening?')
    if entry == 'steak':
      print('Perfect choice, that is grilled to perfection on our artisan salt block!')
  
    if entry == 'salmon':
      print('Good option, we just imported that from the North Atlantic!')

    if entry == 'tuna':
      print('Nice pick, fresh from the south pacific!')

    if entry == 'king crab':
      print('Great pick, we just sourced that freshly from the mediterrean!')




def order_sides():
    entry = input('What would you like for your sides today? You can pick two of them!')
    if entry == 'soup':
      print('Awesome we make that daily!')
  
    if entry == 'salad':
      print('Good option, we source that from italy!')

    if entry == 'fries':
      print('Nice pick, we have a potato farm out back')

    if entry == 'jalepeno poppers':
      print('Nice, we love our mexican heritage here at bottega!')

def order_sides_2():
    entry = input('What would you like for your second side today?')
    if entry == 'soup':
      print('I would have picked that as well, it compliments your first one nicely.')
  
    if entry == 'salad':
      print('I would have picked that as well, it compliments your first one nicely.')

    if entry == 'fries':
      print('I would have picked that as well, it compliments your first one nicely.')

    if entry == 'jalepeno poppers':
      print('I would have picked that as well, it compliments your first one nicely.')

    print('you want the bill?')









menu_items = [
  {
    'entrees': {
      'steak': '$20',
      'salmon': '$18',
      'tuna': '$15',
      'king crab': '$50',
    }
  },
  {
    'sides': {
      'soup': '$4',
      'salad': '$5',
      'fries': '$3',
      'jalepeno poppers': '$8',
    }
  }
]

menu_talk()
order_entrees()
order_sides()
order_sides_2()






