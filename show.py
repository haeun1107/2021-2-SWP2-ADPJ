import menu

def showConsol(componentName):

    Food_Name = []
    Food_Components = []

    if componentName in menu.components_list:
        for i in range(len(menu.menu)):
            Food_Name += "검색한 성분이 해당되는 음식" + i + ":" + menu.food_key[i] + "\n"
            Food_Components = "해당 음식의 다른 성분들" + i + ":" + menu.food_value[i] + "\n"

            return Food_Name, Food_Components
    else:
        pass



