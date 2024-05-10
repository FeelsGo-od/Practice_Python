class Scenario:
    def __init__(self, description, options, outcomes):
        self.description = description
        self.options = options
        self.outcomes = outcomes

    def present_scenario(self):
        print("\n" + self.description)
        for i, option in enumerate(self.options, 1):
            print(f"{i}. {option}")

    def get_outcome(self, choice):
        return self.outcomes[choice - 1]


scenario1 = Scenario(
    description="The Emperor has set an unrealistic deadline for completing the project. What do you do?",
    options=[
        "Push the team to work overtime and meet the deadline at all costs.",
        "Negotiate with the Emperor for a more reasonable deadline.",
    ],
    outcomes=[
        "Success: You meet the deadline but risk team burnout.",
        "Failure: You fail to meet the deadline and face consequences.",
    ],
)

scenario2 = Scenario(
    description="The Death Star project is underway, and you must choose a project management methodology. You have an extensive documentation and requirements are unlikely to change.",
    options=[
        "Adopt an agile methodology.",
        "Implement a traditional waterfall methodology.",
        "Choose a hybrid approach.",
    ],
    outcomes=[
        "Failure: Agile approach leads to flexibility and adaptability, but in the current project it was difficult to establish a budget and scope.",
        "Success: Waterfall approach provides structured management.",
        "Success: Hybrid approach combines benefits of both methodologies, but your team and you were struggling at the first changes in the beginning.",
    ],
)

scenario3 = Scenario(
    description="As the project manager, you must set a motivational goal for the team to inspire collaboration and drive progress towards completing the Death Star. What do you do?",
    options=[
        "Set a challenging but achievable goal.",
        "Set a more modest goal.",
    ],
    outcomes=[
        "Success: The team is motivated and achieves outstanding results.",
        "Failure: The team lacks motivation and fails to meet the goal, leading to delays.",
    ],
)

scenario4 = Scenario(
    description="The Death Star project faces competing priorities and limited resources. What priority setting approach will you choose?",
    options=[
        "Prioritize tasks based on their criticality.",
        "Spread resources evenly across all tasks.",
    ],
    outcomes=[
        "Success: High-impact activities are completed first, minimizing risk.",
        "Failure: Resources are spread too thin, leading to inefficiency and missed deadlines.",
    ],
)

scenario5 = Scenario(
    description="The Empire's new energy source requires the forced labor of enslaved populations. What do you do?",
    options=[
        "Continue using forced labor to meet project requirements.",
        "Seek alternative, ethical solutions.",
    ],
    outcomes=[
        "Success: The project moves forward, but ethical concerns remain.",
        "Failure: Attempting to find ethical solutions leads to delays and compromises, endangering the project's timeline.",
    ],
)


scenarios = [scenario1, scenario2, scenario3, scenario4]
