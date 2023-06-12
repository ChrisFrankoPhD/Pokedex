import requests as req
import climage

rep = req.get('https://pokeapi.co/api/v2/pokemon/?limit=151')
json = rep.json()
pokedex = json.get('results')
# print(pokedex)

while True:
    # get user input for pokemon name   
    query = input("Enter pokemon name, or enter 's' to search pokemon names: ").lower().strip()

    # if user wants to search, ask for search query, and make list of search results
    if query == 's' or query == 'search':
        query = input("Enter search query for pokemon names: ").lower().strip()
        
        # make search results list using query and "in"
        search_results = [pokemon.get('name') for pokemon in pokedex if query in pokemon.get('name')]
        # print(search_results)
        # if no search results, let user know and restart loop
        if not search_results:
            print(f'No search results found for "{query}"')
            continue
        # build output string from search results list
        search_str = '\nSearch Results:\n\n'
        counter = 0
        for result in search_results:
            search_str += f"{result}\n"
            counter += 1
            if counter >= 3:
                counter = 0
                # search_str = search_str.rstrip()
                search_str += '\n'
        search_str = search_str.rstrip()
        search_str += f'\n'
        print(search_str)
    # if user did not want to search, try to get API pokemon data for given input
    else:
        try:
            rep = req.get(f'https://pokeapi.co/api/v2/pokemon/{query}')
            poke1 = rep.json()
        # if API call returns error, restart loop
        except:
            print('Invalid Pokemon Name')
            continue
        # if API is successful, finish loop
        else:
            break

# get sprite URL and save sprite to local image file with handler, then convert this file to a terminal printable image made out of NASI escape codes with the climage package
poke_url1 = poke1.get('sprites').get('front_default')
img_data = req.get(poke_url1).content
with open('sprite1.jpg', 'wb') as handler:
    handler.write(img_data)
poke_sprite1 = climage.convert('sprite1.jpg', width=32, is_unicode=True, is_256color=False, is_truecolor=True)

# get pokemon name and capitalize
poke_name1 = poke1.get('species').get('name').capitalize()

# get pokemon types from the type list, and save the type names in a list with comprehension, then build string from list for printout 
poke_types1 = [type.get('type').get('name') for type in poke1.get('types')]
poke_types1_str = ''
for type in poke_types1:
    poke_types1_str += f'{type} \t'

# get pokemon stats from stat list, 
poke_stats1 = {stat.get('stat').get('name'): stat.get('base_stat') for stat in poke1.get('stats')}
poke_stat1_str = f"HP: {poke_stats1.get('hp')}\t\tAtt: {poke_stats1.get('attack')}  \tDef: {poke_stats1.get('defense')}\nSp-Att: {poke_stats1.get('special-attack')}\tSp-Def: {poke_stats1.get('special-defense')}\tSpeed: {poke_stats1.get('speed')}"
# counter = 0
# for key, value in poke_stats1.items():
#     poke_stat1_str += f'{key}: {value}\t'
#     counter += 1
#     if counter >= 3:
#         poke_stat1_str += f'\n'
#         counter = 0
poke_weight1 = poke1.get('weight')
poke_height1 = poke1.get('height')

print(f'\n{poke_name1}:\n')
print(poke_sprite1)
print(f"Type: \t{poke_types1_str}\n\nHeight: {poke_height1} \t Weight: {poke_weight1}\n\n{poke_stat1_str}\n")

