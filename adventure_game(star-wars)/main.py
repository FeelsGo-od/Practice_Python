from scenarios import scenarios
from utils import present_scenario


def main():
    life = True
    for scenario in scenarios:
        if life:
            life = present_scenario(scenario, life)
        else:
            print(
                "\n You are dead. The Emperor strangled you. P.S - ChatGPT made this scenario evil :D"
            )
            break

    if not life:
        print(
            "\n You are dead. The Emperor strangled you. P.S - ChatGPT made this scenario evil :D"
        )
    else:
        print("\n You win the game. The Emperor praised you and promoted you.")


if __name__ == "__main__":
    main()
