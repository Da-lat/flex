from champs.random_champ_weighted import get_random_champs_weighted, make_43_grid_from_champs


champs = get_random_champs_weighted(40)
img = make_43_grid_from_champs(champs)
img.save("test.png", format='PNG')
