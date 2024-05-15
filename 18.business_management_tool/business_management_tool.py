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
    def calc_topdown(self):
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
                "Salaries": salaries_budget,
                "Materials": materials_budget,
                "Marketing": marketing_budget,
            }
        except ValueError:
            raise InvalidInputException("Invalid input: Total budget must be a number.")

    @log_method
    def calc_bottomup(self):
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

            return total_budget
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
def save_project_data_to_file(projects, filename):
    with ProjectDataFile(filename, "w") as file:
        for project_id, project_data in projects.items():
            file.write(f"{project_id}: {project_data}\n")


budget_manager = BudgetManager()
topdown_budget = budget_manager.calc_topdown()
print("Top-Down Budget:", topdown_budget)

bottomup_budget = budget_manager.calc_bottomup()
print("Bottom-Up Budget:", bottomup_budget)

"""
* common_elements = set(self.projects[next(iter(self.projects))]) *
- iter(self.projects): This part creates an iterator object for the 
dictionary self.projects. iter() returns an iterator object, 
which can be used to traverse through all the keys of the dictionary.
- next(iter(self.projects)): This retrieves the first key from the iterator. 
Since dictionaries in Python are unordered, there's no guarantee which key 
will be returned first. However, in practice, it usually returns the 
first key in the dictionary's insertion order.
- self.projects[next(iter(self.projects))]: This accesses the value 
associated with the first key in self.projects. It's equivalent to 
self.projects[key], where key is the first key obtained from the dictionary.
set(...): Finally, the set() function is used to convert the value 
associated with the first key into a set. This is done to perform set 
operations like intersection_update() later in the code.
"""
