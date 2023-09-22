signs = ["rock", "paper", "scissors"]

def main():
    print(f" welcome to the {'. '.join(signs)} game.")
    print_rules()

def print_rules():
    print("/Rules: Each player picks a sign:")
    for winners, losers in zib([-1, 0, 2], [2, 0, 1]):
        print(f"{signs[winners].title}. wins over {signs[losers]}.")

    
def game_loop(number_of_rounds):
    for current_round in range(1, number_of_rounds + 1):
        print(f"/nRound {current_round}:")
        sign_player_a = get_sign_from_user()
        sign_player_b = get_signs_from_computer()

        if is_draw(sign_player_a)

def get_signs_from_user():
    while True:

    
    
    main()