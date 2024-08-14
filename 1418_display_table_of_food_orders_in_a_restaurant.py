class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        foodItems = set()
        tableNumbers = set()
        foodCountforEachTable = dict()
        for order in orders:
            tableNumber = int(order[1])
            food = order[2]
            tableNumbers.add(tableNumber)
            foodItems.add(food)
            foodforEachTable = foodCountforEachTable.get(tableNumber, {})
            foodforEachTable[food] = foodforEachTable.get(food, 0) + 1
            foodCountforEachTable[tableNumber] = foodforEachTable
        foodlist = list(foodItems)
        foodlist.sort()

        tablelist = list(tableNumbers)
        tablelist.sort()

        header = []
        header.append('Table')
        header.extend(foodlist)

        table = []
        table.append(header)

        for tableNumber in tablelist:
            row = []
            row.append(str(tableNumber))
            foodCount = foodCountforEachTable.get(tableNumber)
            for food in foodlist:
                count = foodCount.get(food, 0)
                row.append(str(count))
            table.append(row[:])
        return table