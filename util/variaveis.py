
pessoas = [
    ('Lisbon', 'LIS'),
    ('Madrid', 'MAD'),
    ('Paris', 'CDG'),
    ('Dublin', 'DUB'),
    ('Brussels', 'BRU'),
    ('London', 'LHR'),
]

destino = 'FCO' # Roma
'''
voos = [
    {
    'origem': linha.split(',')[0],
    'destino': linha.split(',')[1],
    'partida': linha.split(',')[2],
    'chegada': linha.split(',')[3],
    'distancia': (linha.split(',')[4]).replace('\n', ''),
    }
    for linha in open('util/flights.txt')
    if linha.split(',')[1] == 'FCO'
]
voos_lis = [voo for voo in voos if voo['origem'] == 'LIS']
voos_mad = [voo for voo in voos if voo['origem'] == 'MAD']
voos_dub = [voo for voo in voos if voo['origem'] == 'DUB']
voos_lhr = [voo for voo in voos if voo['origem'] == 'LHR']
voos_bru = [voo for voo in voos if voo['origem'] == 'BRU']
'''

voos = {}
for linha in open('util/flights.txt'):
    origem, destino, chegada, partida, preco = linha.split(',')
    voos.setdefault((origem, destino),[])
    voos[(origem, destino)].append({'chegada':chegada, 'partida':partida, 'preco':int(preco)})
        


