{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOB9CRks+dc4HNbo2jlHMhh"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "jZJWAV1lvOXi"
      },
      "outputs": [],
      "source": [
        "IngrCocktail = {'aperol' : ['prosecco', 'aperol', 'soda', 'orange', 'ice'],\n",
        "                'espressomartini' : ['vodka', 'liquor', 'ice'],\n",
        "                                     'negroni' : ['soda', 'aperol', 'ice']}\n",
        "\n",
        "def CocktailGenerator(Ingridients):\n",
        "  IngridientsList = Ingridients.split(', ')\n",
        "  # print(IngridientsList)\n",
        "  for i in IngrCocktail:\n",
        "    # print(set(IngrCocktail[i]), set(IngridientsList)), len(IngrCocktail[i])\n",
        "    if len(set(IngrCocktail[i]) & set(IngridientsList)) == len(IngrCocktail[i]):\n",
        "      print(i, IngrCocktail[i])\n",
        "\n",
        "CocktailGenerator('prosecco, aperol, soda, orange, ice')"
      ]
    }
  ]
}