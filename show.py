import menu

def showConsol(componentName):

    Food_Name = []
    Food_Components = []

    for i in range(len(menu.food_value)):
        for j in range(len(menu.food_value[i])):
            if componentName == menu.food_value[i][j]:
                Food_Name += ( "검색한 성분이 해당되는 음식" + i + ":" + menu.food_key[i] + "\n" )
                Food_Components += ( "해당 음식의 다른 성분들" + i + ":" + menu.food_value[i] + "\n" )
            else:
                continue

    return Food_Name, Food_Components


