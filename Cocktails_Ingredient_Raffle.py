IngrCocktail = {'aperol' : ['prosecco', 'aperol', 'soda', 'orange', 'ice'],
                'espressomartini' : ['vodka', 'liquor', 'ice'],
                                     'negroni' : ['soda', 'aperol', 'ice']} #you can just add more cocktails there

def CocktailGenerator(Ingridients):
  IngridientsList = Ingridients.split(', ')
  # print(IngridientsList)
  for i in IngrCocktail:
    # print(set(IngrCocktail[i]), set(IngridientsList)), len(IngrCocktail[i])
    if len(set(IngrCocktail[i]) & set(IngridientsList)) == len(IngrCocktail[i]):
      print(i, IngrCocktail[i])

CocktailGenerator('prosecco, aperol, soda, orange, ice')
