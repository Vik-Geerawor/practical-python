# mortgage.py
#
# Exercise 1.7


def run():

    principal = 500000.0
    rate = 0.05
    min_payment = 2684.11
    total_paid = 0.0
    extra_payment_start_month = 61
    extra_payment_end_month = 108
    extra_payment = 1000
    month = 0

    while principal > 0:
        month += 1

        if extra_payment_start_month <= month <= extra_payment_end_month:
            payment = min_payment + extra_payment
        else:
            payment = min_payment

        principal = principal * (1 + rate / 12)

        if principal > payment:
            principal -= payment
        else:
            payment = principal
            principal = 0

        total_paid = total_paid + payment

        print(f'{month:>5d} {round(total_paid, 2):>10.2f} {round(principal, 2):>10.2f}')

    print(f'Total paid {round(total_paid, 2):>10.2f}')
    print(f'Months {month:>5d}')

    text = "False"
    print('text = ', text)
    print('bool(text):', bool(text))            # True
    bin_text = ' '.join(format(ord(x), 'b') for x in text)
    print('text in binary:', bin_text)
    print('bool(1) - first number:', bool(1))   # True - first bin number
