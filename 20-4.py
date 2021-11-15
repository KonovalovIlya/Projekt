players = {

    ("Ivan", "Volkin"): (10, 5, 13),

    ("Bob", "Robbin"): (7, 5, 14),

    ("Rob", "Bobbin"): (12, 8, 2)

}

l = [tuple(list(i) + list(j)) for i, j in players.items()]
    
print(l)