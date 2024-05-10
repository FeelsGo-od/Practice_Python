def present_scenario(scenario, life):
    life = life
    scenario.present_scenario()
    choice = None
    while choice is None:
        try:
            choice = int(input("Enter your choice: "))
            if choice < 1 or choice > len(scenario.options):
                print(
                    f"Invalid choice. Please enter a number between 1 and {len(scenario.options)}"
                )
                choice = None
        except ValueError:
            print("Invalid input. Please enter a valid option number.")
    outcome = scenario.get_outcome(choice)
    if "Failure:" in outcome:
        life = False
    print(outcome)
    return life
