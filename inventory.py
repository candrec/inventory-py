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

#add uma lista de loot no inventário original

def add_inventory(stuff,dragon_loot):
    for loot in dragon_loot:
        stuff.setdefault(loot,0)
        stuff[loot] = stuff[loot] + 1

dragon_loot = ['gold coin','dagger','gold coin','gold coin','ruby']
print(f'Dragon Loot = {dragon_loot}')
add_inventory(stuff,dragon_loot)
display_inventory(stuff)
