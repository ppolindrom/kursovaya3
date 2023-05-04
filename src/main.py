from unit import load_data, get_last, sorted_operation, change_date, \
    masked_number


def main():
    data = load_data()
    last_operation = get_last(data)
    sorted = sorted_operation(last_operation)
    for i in sorted:
        from_card = change_date(i['date'])
        name_trans = i['description']
        try:
            from_ = masked_number(i['from'])
        except KeyError:
            from_ = "no information"
        try:
            to_ = masked_number(i['to'])
        except KeyError:
            to_ = "no information"
        sum = i['operationAmount']['amount']
        valu = i['operationAmount']['currency']['name']


        print(f'{from_card} {name_trans}\n{from_} -> {to_}\n{sum} {valu}')
        print(" ")
    return


    # from_card = masked_card_number(sorted)
    # to_card = masked_account_number(sorted)

main()