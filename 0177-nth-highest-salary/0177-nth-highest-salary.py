import pandas as pd

def nth_highest_salary(employee: pd.DataFrame, N: int) -> pd.DataFrame:
    sal = employee['salary'].drop_duplicates().tolist()
    sal = sorted(sal, reverse=True)
    print(sal)
    res = {"getNthHighestSalary({n})".format(n=N):[]}
    #if N <= 0:
    #    res["getNthHighestSalary({n})".format(n=N)].append(None)
    #else:
    if N not in range(1,len(sal)+1):
        res["getNthHighestSalary({n})".format(n=N)].append(None)
    else:
        res["getNthHighestSalary({n})".format(n=N)].append(sal[N-1])

    print(res)
    return pd.DataFrame(res)
