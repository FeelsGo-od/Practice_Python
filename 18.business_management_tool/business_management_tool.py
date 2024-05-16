import logging

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


class BudgetExceededException(Exception):
    """Exception raised when the budget exceeds the specified limit."""

    pass


class InvalidInputException(Exception):
    """Exception raised for invalid user input."""

    pass


# Decorator for logging
def log_method(func):
    def wrapper(*args, **kwargs):
        logging.info(f"Executing method: {func.__name__}")
        return func(*args, **kwargs)

    return wrapper


# Generator for generating project reports
def generate_report(projects):
    for project_id, project_data in projects.items():
        yield f"Project ID: {project_id}, Project Data: {project_data}"


# Context manager for file handling
class ProjectDataFile:
    def __init__(self, filename, mode):
        self.filename = filename
        self.mode = mode

    def __enter__(self):
        self.file = open(self.filename, self.mode)
        return self.file

    def __exit__(self, exc_type, exc_value, traceback):
        self.file.close()


# Example usage of decorators, generators, and context managers
class BudgetManager:
    @log_method
    def calc_topdown(self, project_id):
        try:
            logging.info("Calculating top-down budget...")
            total_budget = float(input("Enter the total budget for the project: "))
            if total_budget <= 0:
                raise InvalidInputException(
                    "Invalid input: Total budget must be a positive number"
                )

            # Example: Allocate 30% for salaries, 20% for materials, 10% for marketing, etc.
            salaries_budget = total_budget * 0.3
            materials_budget = total_budget * 0.2
            marketing_budget = total_budget * 0.1

            # Round the budget for each category to 2 decimal places
            salaries_budget = round(salaries_budget, 2)
            materials_budget = round(materials_budget, 2)
            marketing_budget = round(marketing_budget, 2)

            return {
                project_id: {
                    "Salaries": salaries_budget,
                    "Materials": materials_budget,
                    "Marketing": marketing_budget,
                }
            }
        except ValueError:
            raise InvalidInputException("Invalid input: Total budget must be a number.")

    @log_method
    def calc_bottomup(self, project_id):
        try:
            logging.info("Calculating bottom-up budget...")
            # Inititalize variables to hold total budget and expenses for each category
            total_budget = 0
            salaries_expense = 0
            materials_expense = 0
            marketing_expense = 0

            # Prompt the user to input expenses for each category
            salaries_expense = float(input("Enter expenses for salaries: "))
            materials_expense = float(input("Enter expenses for materials: "))
            marketing_expense = float(input("Enter expenses for marketing: "))

            if any(
                expense < 0
                for expense in [salaries_expense, materials_expense, marketing_expense]
            ):
                raise InvalidInputException(
                    "Invalid input: Expenses must be positive numbers."
                )

            # Calculate total budget by summing up the expenses
            total_budget = salaries_expense + materials_expense + marketing_expense

            return {project_id: total_budget}
        except ValueError:
            raise InvalidInputException("Invalid input: Expenses must be numbers.")


class ProjectAnalyzer:
    def __init__(self):
        self.projects = {}  # Dictionary to store project data

    def add_project(self, project_id, project_data):
        """Add project data to the analyzer."""
        self.projects[project_id] = project_data

    def compare_projects(self, project_id1, project_id2):
        comparison_data = []

        """Compare two projects based on their attributes."""
        if project_id1 not in self.projects or project_id2 not in self.projects:
            raise InvalidInputException("Invalid project IDs.")

        project1 = self.projects[project_id1]
        project2 = self.projects[project_id2]

        # Compare project attributes (e.g., budget, duration, team size)
        if project1.budget > project2.budget:
            comparison_data.append(
                f"{project_id1} has a higher budget than {project2}."
            )
        elif project1.budget < project2.budget:
            comparison_data.append(
                f"{project_id2} has a higher budget than {project1}."
            )

        if project1.duration > project2.duration:
            comparison_data.append(
                f"{project_id1} has a longer duration than {project2}."
            )
        elif project1.duration < project2.duration:
            comparison_data.append(
                f"{project_id2} has a longer duration than {project1}."
            )

        return comparison_data

    def find_common_elements(self):
        """Find common elements among all projects."""
        if not self.projects:
            return set()

        common_elements = set(self.projects[next(iter(self.projects))])

        for project_data in self.projects.values():
            common_elements.intersection_update(project_data)

        return common_elements


# Usage of generator for project reports
def print_project_reports(projects):
    for report in generate_report(projects):
        print(report)


# Usage of context manager for file handling
def save_project_data_to_file(project_data, filename):
    with ProjectDataFile(filename, "a") as file:
        file.write(f"{project_data}\n")


budget_manager = BudgetManager()
project_id = input("Enter project name(or ID): ")

topdown_budget = budget_manager.calc_topdown(project_id)
print("Top-Down Budget:", topdown_budget)

bottomup_budget = budget_manager.calc_bottomup(project_id)
print("Bottom-Up Budget:", bottomup_budget)

print_project_reports(topdown_budget)

save_project_data_to_file(
    topdown_budget,
    r"C:\Users\PC\Desktop\Practice Python\18.business_management_tool\project_data.txt",
)


"""
## Dictionary Iteration:
- `iter(self.projects)`: Creates an iterator object for the dictionary `self.projects`, allowing traversal through its keys.
- `next(iter(self.projects))`: Retrieves the first key from the iterator. In dictionaries, insertion order is not guaranteed, but this typically returns the first key.
- `self.projects[next(iter(self.projects))]`: Accesses the value associated with the first key in `self.projects`.
- `set(...)`: Converts the value associated with the first key into a set for set operations like `intersection_update()`.

## Logging Configuration:
- `logging.basicConfig()`: Configures the logging system, typically called once at the beginning of the program.
- `level=logging.INFO`: Sets the logging level to INFO, processing only messages with severity INFO or higher.
- `format='%(asctime)s - %(levelname)s - %(message)s'`: Specifies the format of log messages using placeholders for time, log level, and message.

## Accessing Function Names:
- `func.__name__`: Accesses the name of the function being decorated (`func`), used to construct log messages indicating the executed method.

## *args and **kwargs:
- `*args`: Captures variable positional arguments passed to a function.
- `**kwargs`: Captures variable keyword arguments passed to a function.
- In decorators, `*args` and `**kwargs` allow accepting any number of arguments without explicitly specifying them.
"""
