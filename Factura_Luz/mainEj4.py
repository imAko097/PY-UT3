from factura_luz import FacturaLuz

def main():
    my_bill = FacturaLuz(245.65)
    print("Consumed kilowatts:", my_bill.getKwConsumed(), "kw")
    print(f"Total price of the electricity bill: {round(my_bill.calculatePrice(), 2)} euros")

main()