order = "salad water hamburger salad hamburger"

def item_order(order):
    s = order.count('salad')
    salad = "salad:%s "%s
    h = order.count('hamburger')
    ham = "hamburger:%s "%h
    w = order.count('water')
    water = "water:%s"%w
    return salad + ham + water