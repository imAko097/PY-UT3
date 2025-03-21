from fraccion import Fraccion

def main():
    # Create two fractions (same denominator) and add them
    f1 = Fraccion(10, 5)
    f2 = Fraccion(7, 5)

    f3 = f1.add(f2)
    print(f"{f1.get_numerator()}/{f1.get_denominator()} + {f2.get_numerator()}/{f2.get_denominator()} = {f3.get_numerator()}/{f3.get_denominator()}")

    # Create two fractions (different denominator) and add them
    f1 = Fraccion(1, 4)
    f2 = Fraccion(1, 6)

    f3 = f1.add(f2)
    print(f"{f1.get_numerator()}/{f1.get_denominator()} + {f2.get_numerator()}/{f2.get_denominator()} = {f3.get_numerator()}/{f3.get_denominator()}")

    # Create two fractions (same denominator) and subtract them
    f1 = Fraccion(10, 5)
    f2 = Fraccion(7, 5)

    f3 = f1.subtract(f2)
    print(f"{f1.get_numerator()}/{f1.get_denominator()} - {f2.get_numerator()}/{f2.get_denominator()} = {f3.get_numerator()}/{f3.get_denominator()}")

    # Create two fractions (different denominator) and subtract them
    f1 = Fraccion(1, 4)
    f2 = Fraccion(1, 6)

    f3 = f1.subtract(f2)
    print(f"{f1.get_numerator()}/{f1.get_denominator()} - {f2.get_numerator()}/{f2.get_denominator()} = {f3.get_numerator()}/{f3.get_denominator()}")

main()