from menu import Menu

#クラスをインスタンス化する
juice = Menu('JUICE', 280, r"static\img\juice_orange.png")
coffee = Menu('COFFEE', 380, r"static\img\coffee01_blend.png")
curry = Menu('CURRY', 800, r"static\img\food_curryrice_white.png")
pasta = Menu('PASTA', 780, r"static\img\food_spaghetti_bolognese_meatsauce.png")

#インスタンス化したクラスをリストに格納
menu = [juice, coffee, curry, pasta]
