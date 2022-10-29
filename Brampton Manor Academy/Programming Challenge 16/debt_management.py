def calculation(interest, repayment):
    debt = 100
    total = 0
    count = 0
    while debt > 0:
        debt += (debt * round(interest / 100, 2))
        payment = debt * round(repayment / 100, 2)
        if payment > 50:
            debt -= payment
            total += payment
        else:
            debt -= 50
            if debt < 0:
                total += (debt + 50)
            else:
                total += 50
        count += 1
    return total, count


if __name__ == "__main__":
    total, count = calculation(43, 46)
    print('Total amount repaid: ' + str(total))
    print('Number of payments: ' + str(count))
