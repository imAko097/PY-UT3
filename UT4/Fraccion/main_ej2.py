from fraccion import Fraccion

def main():
    # Create two fractions (same denominator) and add them
    f1 = Fraccion(10, 5)
    f2 = Fraccion(7, 5)

    f3 = f1.add(f2)
    print(f"- Add (same denominator): {f1.__str__()} + {f2.__str__()} = {f3.__str__()}")

    # Create two fractions (different denominator) and add them
    f1 = Fraccion(1, 4)
    f2 = Fraccion(1, 6)

    f3 = f1.add(f2)
    print(f"- Add (different denominator): {f1.__str__()} + {f2.__str__()} = {f3.__str__()}")

    # Create two fractions (same denominator) and subtract them
    f1 = Fraccion(10, 5)
    f2 = Fraccion(7, 5)

    f3 = f1.subtract(f2)
    print(f"- Subtract (same denominator): {f1.__str__()} - {f2.__str__()} = {f3.__str__()}")

    # Create two fractions (different denominator) and subtract them
    f1 = Fraccion(1, 4)
    f2 = Fraccion(1, 6)

    f3 = f1.subtract(f2)
    print(f"- Subtract (different denominator): {f1.__str__()} - {f2.__str__()} = {f3.__str__()}")

    # Multiply two fractions
    f1 = Fraccion(12, 4)
    f2 = Fraccion(28, 34)

    f3 = f1.multiply(f2)
    print(f"- Multiply: {f1.__str__()} * {f2.__str__()} = {f3.__str__()}")

    # Divide two fractions
    f1 = Fraccion(2, 10)
    f2 = Fraccion(1, 6)

    f3 = f1.divide(f2)
    print(f"- Divide: {f1.__str__()} / {f2.__str__()} = {f3.__str__()}")

    # Compare two fractions (equals)
    f1 = Fraccion(2, 10)
    f2 = Fraccion(2, 6)

    print(f"- Compare: {f1.__str__()} == {f2.__str__()} = {f1.equals(f2)}")

    # Compare two fractions (less than)
    f1 = Fraccion(10, 6)
    f2 = Fraccion(2, 6)

    print(f"- Compare: {f1.__str__()} < {f2.__str__()} = {f1.less_than(f2)}")

    

main()