import pandas as pd

def calculate_special_bonus(employees: pd.DataFrame) -> pd.DataFrame:
    res = {'employee_id':[], 'bonus':[]}
    for i in range(len(employees)):
        res['employee_id'].append(employees['employee_id'][i])
        if (employees['employee_id'][i]%2 != 0) & (employees['name'][i][0] != 'M'):
            res['bonus'].append(employees['salary'][i])
        else:
            res['bonus'].append(0)
    #print(res)
    return pd.DataFrame.from_dict(res).sort_values(by='employee_id')