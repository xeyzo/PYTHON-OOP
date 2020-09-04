items = []

class Cart:
    def __init__(self):
        self.items = items

    def getAll(self):
        print(self.items)

    def addItem(self, items):
        self.items.append(items)
        return self

    def removeItem(self, id):
        for i, d in enumerate(items):
            if d['id'] == id:
                return items.pop(i)



cart = Cart()

(
cart.addItem({ 'item_id': 1, 'price': 6000, 'quantity': 3 })     
    .addItem({ 'item_id': 3, 'price': 8000, 'quantity': 2 })
    .addItem({ 'item_id': 4, 'price': 4000, 'quantity': 6 })
)


cart.getAll()
