import random

Max_lines=3
Max_bet=100
Min_bet=1

rows=3
cols=3

symbol_count={
    "A":2,
    "B":4,
    "C":6,
    "D":8,
}

symbol_values={
    "A":5,
    "B":4,
    "C":3,
    "D":2,
}

def check_winnings(columns, lines, bet, values):
    winnings=0
    winning_line=[]
    for line in range(lines):
        symbol=columns[0][line]
        for column in columns:
            symbol_to_check=column[line]
            if symbol!=symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line+1)
    return winnings, winning_line



def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i!=len(columns)-1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")
        print()



def get_slot_machine_spins(rows, cols, symbols):
    all_symbols=[]
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)

    columns=[]
    for _ in range(cols):
        column=[]
        current_sym=all_symbols[:]
        for _ in range(rows):
            value=random.choice(current_sym)
            current_sym.remove(value)
            column.append(value)
        columns.append(column)

    return columns



def get_bet():
    while True:
        bet=input(f"Enter the amount you want to bet on each line({Min_bet}-{Max_bet}): $")
        if bet.isdigit():
            bet=int(bet)
            if Min_bet <= bet <= Max_bet:
                break
            else:
                print("Enter between the valid range.")
        else:
            print("Enter a valid value.")
    return bet



def lines_to_bet():
    while True:
        lines=input(f"Enter the number of lines you would like to bet on (1-{Max_lines}): ")
        if lines.isdigit():
            lines=int(lines)
            if 1 <= lines <= Max_lines:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Enter a valid number of lines.")
    return lines



def deposit():
    while True:
        amount=input("How much would you like to deposit: $")
        if amount.isdigit():
            amount=int(amount)
            if amount>0:
                break
            else:
                print("Amount should be greater than 0.")
        else:
            print("You need to deposit an amount.")
    
    return amount 



def spin(balance):
    lines=lines_to_bet()
    while True:
        bet=get_bet()
        total_bet=bet*lines

        if total_bet>balance:
            print(f"Insufficient balance. Current Balance ${balance}.")
        else:
            break

        print(f"You are betting ${bet} on {lines} lines. Total bet is {total_bet}.")

    slots=get_slot_machine_spins(rows, cols, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_values)
    print(f"You won: ${winnings}")
    print(f"You won on lines: ", *winning_lines)
    return winnings-total_bet    


def main():
    balance=deposit()
    while True:
        print(f"Current balance is: ${balance}")
        answer = input("Press enter to play (q to quit).")
        if answer == "q":
            break
        balance += spin(balance)

    print(f"You left with ${balance}")
    
main()