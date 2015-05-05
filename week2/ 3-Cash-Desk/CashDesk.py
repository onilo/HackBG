from Bill import Bill
from BatchBill import BatchBill


class CashDesk():

    def __init__(self):
        self.desk = {}

    def take_money(self, money):
        self.desk.append(currency)

    def total(self):
        result = 0
        for money in self.desk:
            result += int(money)

        return result

    def inspect(self):

        lines = []
        total = self.total()

        lines.append("We have {}$ in the desk.".format(total))

        if total > 0:
            lines.append("Bills are:")

            bills = list(self.desk.keys())
            bills.sort()

            for bill in bills:
                line = ("${} - {}".format(int(bill), self.desk[bill]))
                lines.append(line)
        return "\n".join(lines)
