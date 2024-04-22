import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    if N <= 0:  # Check if N is non-positive
        return pd.DataFrame({'getNthHighestSalary(' + str(N) + ')': [None]})
    
    # Drop duplicate salaries and sort them in descending order
    sorted_salaries = employee['salary'].drop_duplicates().sort_values(ascending=False)
    
    # Check if there are at least N unique salaries
    if len(sorted_salaries) >= N:
        # Retrieve the Nth highest salary
        nth_highest_salary = sorted_salaries.iloc[N - 1]
        # Create a DataFrame with the nth highest salary
        result = pd.DataFrame({'getNthHighestSalary(' + str(N) + ')': [nth_highest_salary]})
        return result
    else:
        # If there are fewer than N unique salaries, return None
        return pd.DataFrame({'getNthHighestSalary(' + str(N) + ')': [None]})
