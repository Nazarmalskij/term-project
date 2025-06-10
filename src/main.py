def calculate_tax(income, tax_rate):
    """
    Обчислює суму податку.

    :param income: float - дохід
    :param tax_rate: float - податкова ставка у вигляді десяткового дробу (наприклад, 0.2 для 20%)
    :return: float - розрахований податок
    """
    if income < 0:
        raise ValueError("Income cannot be negative")
    if not 0 <= tax_rate <= 1:
        raise ValueError("Tax rate must be between 0 and 1")
    return round(income * tax_rate, 2)


def main():
    try:
        income = float(input("Enter your income: "))
        tax_rate = float(input("Enter tax rate (e.g. 0.2 for 20%): "))
        tax = calculate_tax(income, tax_rate)
        print(f"Your tax is: {tax}")
    except ValueError as e:
        print(f"Input error: {e}")


if __name__ == "__main__":
    main()
