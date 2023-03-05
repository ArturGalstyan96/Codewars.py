def cakes(recipe, available):
    for key in recipe.keys():
        if key not in available:
            return 0
    cake_num = min([available[key] // val for key, val in recipe.items()])
    return cake_num