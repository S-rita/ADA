customer_dict = {}
possible_money_to_collect = []
total_sum = 0

initial_input = input()
initial_input_list = initial_input.split(' ')
amount_people_in_queue = int(initial_input_list[0])
time_until_close = int(initial_input_list[1])

for customer in range(amount_people_in_queue):
    current_line_input = input()
    current_line_list = current_line_input.split(' ')
    money_to_deposit = int(current_line_list[0])
    time_until_leave = int(current_line_list[1])
    customer_dict.setdefault(time_until_leave, []).append(money_to_deposit)

for time in range(time_until_close)[::-1]:
    if time in customer_dict.keys():
        for money in customer_dict[time]:
            possible_money_to_collect.append(money)
        if possible_money_to_collect:
            total_sum += max(possible_money_to_collect)
            possible_money_to_collect.remove(max(possible_money_to_collect))

print(total_sum)
