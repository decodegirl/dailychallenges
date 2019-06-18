print(" Welcome, I am going to help you determine whether your credit card is valid or not.")

card_number = input(" Now  Please enter your credit card number: ")


def validate_credit_card_number(card_number):
    # convert the string into a list of numbers
    temp_list = []
    for c in card_number:
        temp_list.append(int(c))

    for i in range(0, len(card_number), 2):

        temp_list[i] = temp_list[i] * 2
        if temp_list[i] >= 10:
            # if doubling up the digits results in a number greater than
            # 10 add up the digits to get a singular number
            temp_list[i] = temp_list[i] // 10 + temp_list[i] % 10

    if sum(temp_list) % 10 == 0:
        print('This  is a valid credit card')

    else:
        print('This is not valid credit card')

validate_credit_card_number(card_number)
