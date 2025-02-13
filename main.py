from calculator_proxy import CalculatorProxy


def main():
    proxy_calculator = CalculatorProxy()

    # Performing allowed operations
    print("Addition:", proxy_calculator.add(5, 3))  # Should return 8
    print("Subtraction:", proxy_calculator.sub(5, 3))  # Should return 2

    # Attempting disallowed operations
    try:
        proxy_calculator.mul(5, 3)
    except NotImplementedError as e:
        print(e)

    try:
        proxy_calculator.div(5, 3)
    except NotImplementedError as e:
        print(e)

    try:
        proxy_calculator.power(5, 3)
    except NotImplementedError as e:
        print(e)


if __name__ == "__main__":
    main()
