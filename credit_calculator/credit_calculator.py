import math
import argparse


def annuity_monthly_payment(principal, periods, interest):
    """
    Calculates the annuity (equal) monthly payment on a loan.

    :param principal: loan amount
    :param periods: number of months (periods) of payments
    :param interest: annual interest rate (in percent)
    :return: monthly payment rounded up
    """
    a = interest / (12 * 100)  # converting percentage to monthly decimal rate
    annuity = principal * (a * (1 + a) ** periods) / ((1 + a) ** periods - 1)
    return math.ceil(annuity)


def loan_principal(payment, periods, interest):
    """
    Calculates the loan amount given the annuity payment, term, and interest rate.

    :param payment: monthly payment
    :param periods: number of months
    :param interest: annual interest rate (in percent)
    :return: loan amount rounded down
    """
    a = interest / (12 * 100)
    principal = payment / ((a * (1 + a) ** periods) / ((1 + a) ** periods - 1))
    return math.floor(principal)


def number_of_month(principal, payment, interest):
    """
    Calculates the number of months needed to pay off a loan.

    :param principal: loan amount
    :param payment: monthly payment
    :param interest: annual interest rate (in percent)
    :return: number of months rounded up
    """
    a = interest / (12 * 100)
    b = math.log(payment / (payment - a * principal), 1 + a)  # logarithmic formula
    months = math.ceil(b)
    return months


def differentiated_payments(principal, periods, interest):
    """
    Displays differentiated payments by month and returns the overpayment amount.

    :param principal: loan amount
    :param periods: number of months
    :param interest: annual interest rate (in percent)
    :return: loan overpayment
    """
    a = interest / (12 * 100)
    total_payment = 0

    for f in range(1, periods + 1):
        # formula for differentiated payment in a given month
        diff_payment = math.ceil(principal / periods + a * (principal - (principal * (f - 1) / periods)))
        print(f'Month {f}: payment is {diff_payment}')
        total_payment += diff_payment

    overpayment = total_payment - principal
    if overpayment < 0:
        overpayment = 0
    return overpayment


def main():
    """
    Main function:
    - reads command line arguments;
    - determines the calculation type (annuity or diff);
    - performs the corresponding calculations;
    - displays the result and overpayment.
    """
    # Setting up the argument parser
    parser = argparse.ArgumentParser(description='Credit Calculator')
    parser.add_argument('--type', choices=['annuity', 'diff'])
    parser.add_argument('--payment', type=float)
    parser.add_argument('--principal', type=float)
    parser.add_argument('--periods', type=int)
    parser.add_argument('--interest', type=float)
    args = parser.parse_args()

    # Check for negative values
    parameters = [args.payment, args.principal,args.periods, args.interest]
    if any(p is not None and p < 0 for p in parameters):
        print('Incorrect parameters')
        return

    # Percentage is required
    if args.interest is None:
        print('Incorrect parameters')
        return

    # Differentiated payments
    if args.type == 'diff':
        if args.principal is None or args.periods is None or args.payment is not None:
            print('Incorrect parameters')
            return
        overpayment = differentiated_payments(args.principal, args.periods, args.interest)
        print(f'Overpayment = {int(overpayment)}')
        return

    # Annuity payments
    elif args.type == 'annuity':
        non_none = [args.payment, args.principal, args.periods]
        if non_none.count(None) != 1:
            print('Incorrect parameters')
            return

        # Find principal
        if args.principal is None:
            principal = loan_principal(args.payment, args.periods, args.interest)
            print(f'Your loan principal = {principal}')
            print(f'Overpayment = {int(args.payment * args.periods - principal)}')

        # Find payment
        elif args.payment is None:
            payment = annuity_monthly_payment(args.principal, args.periods, args.interest)
            print(f'Your annuity payment = {payment}')
            print(f'Overpayment = {int(payment * args.periods - args.principal)}')

        # Find periods
        elif args.periods is None:
            months = number_of_month(args.principal, args.payment, args.interest)
            years, rem_months = divmod(months, 12)
            time_output = []
            if years:
                time_output.append(f"{years} year{'s' if years > 1 else ''}")
            if rem_months:
                time_output.append(f"{rem_months} month{'s' if rem_months > 1 else ''}")
            print(f"It will take {' and '.join(time_output)} to repay this loan")
            print(f'Overpayment = {args.payment * months - args.principal:.0f}')
    else:
        print('Incorrect parameters')
        return


if __name__ == '__main__':
    main()
