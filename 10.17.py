# Taqi Syed
# 1863528

class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_description = "none"
        self.item_price = 0
        self.item_quantity = 0

    def print_item_cost(self):
        print(self.item_name)
        print(self.item_quantity)
        print(self.item_price)

    def print_item_description(self):
        print("Item Name: ", self.item_name)
        print("Description: ", self.item_description)

def main():
    item1 = ItemToPurchase()
    item2 = ItemToPurchase()
    print("Item 1")
    print("Enter the item name:")
    item1.item_name = input()
    print("Enter the item price:")
    item1.item_price = int(input())
    print("Enter the item quantity:")
    item1.item_quantity = int(input())

    print("\nItem 2")
    print("Enter the item name:")
    item2.item_name = input()
    print("Enter the item price:")
    item2.item_price = int(input())
    print("Enter the item quantity:")
    item2.item_quantity = int(input())

    print("\nTOTAL COST")
    item1.print_item_cost()
    item2.print_item_cost()

    item1Cost = item1.item_quantity * item1.item_price
    item2Cost = item2.item_quantity * item2.item_price

    total_cost = item1Cost + item2Cost
    print("\nTotal: $" + str(total_cost))

if __name__ == '__main__':
    main()


