import pandas as pd

def second_highest_salary(employee: pd.DataFrame) -> pd.DataFrame:
    # Drop duplicate salaries and sort them in descending order
    sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    # Check if there are at least 2 unique salaries
    if len(sorted_salaries) >= 2:
        # Retrieve the Nth highest salary
        second_highest_salary = sorted_salaries.iloc[1]
        # Create a DataFrame with the nth highest salary
        result = pd.DataFrame({'SecondHighestSalary': [second_highest_salary]})
        return result
    else:
        # If there are fewer than N unique salaries, return None
        return pd.DataFrame({'SecondHighestSalary': [None]})