#mais um exemplo de fixação do tipo dicionário
#função pra listar o inventário de um rpg de fantasia

stuff = {'rope':1,'torch':6,'gold coin':42,'dagger':1,'arrow':12}

def display_inventory(inventory):
    print('Inventory:')
    item_total = 0
    for k,v in inventory.items():
        print(f'{v} {k}')
        item_total += v
    print(f'Total number of items: {item_total}')

display_inventory(stuff)
