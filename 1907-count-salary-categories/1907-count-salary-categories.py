import pandas as pd

def count_salary_categories(accounts: pd.DataFrame) -> pd.DataFrame:
    low_sal = accounts[accounts['income']< 20000]
    avg_sal = accounts[(accounts['income'] >= 20000) & (accounts['income'] <= 50000)]
    high_sal = accounts[accounts['income'] > 50000]
    res = {'category':['Low Salary', 'Average Salary', 'High Salary'],
            'accounts_count':[len(low_sal), len(avg_sal), len(high_sal)]}
    return pd.DataFrame(res)