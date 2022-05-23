import requests as r 

def poke_guetter():
    data = r.get('https://pokeapi.co/api/v2/pokemon/entei')
    if data.status_code == 200:
        data = data.json()
    else:
        return 'Broken API.'
    name = data['name']
    Entei_versions = [v['version']['name'] for v in data ["game_indices"]]
    weight = data['weight']
    types = data['types'][0]['type']['name']
    abilities = [v['ability']['name'] for v in data ['abilities']]
    return{
        'names':name,
        'Versions': Entei_versions, 
        'Weight': weight,
        'Types': types,
        'Abilities' : abilities,
        
    }

