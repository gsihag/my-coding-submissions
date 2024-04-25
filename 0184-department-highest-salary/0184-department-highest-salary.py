import pandas as pd

def department_highest_salary(employee: pd.DataFrame, department: pd.DataFrame) -> pd.DataFrame:
    #res = {'Department': [], 'Employee': [], 'Salary':[]}
    if len(department['id']) == 0:
        return pd.DataFrame([], columns=['Department', 'Employee', 'Salary'])

    if len(employee['id']) == 0:
        return pd.DataFrame([], columns=['Department', 'Employee', 'Salary'])

    results={}
    for idx,depart_id in department['id'].items():
        #results[depart_id] = {}
        #print(depart_id)
        depart_name = department['name'][idx]
        #print(depart_name)
        if depart_id in employee['departmentId']:
            depart_employee_table = employee[employee['departmentId'] ==depart_id]
            #print(depart_employee_table)
            depart_max_salary = max(depart_employee_table['salary'])
            #print(depart_max_salary)
            depart_employee_with_max_sal = depart_employee_table[depart_employee_table['salary']==depart_max_salary]
            #print(depart_employee_with_max_sal)
            depart_employee_with_max_sal['depart_name'] = depart_name
            results[depart_id] = depart_employee_with_max_sal[['depart_name', 'name', 'salary']].rename(columns={'depart_name': 'Department', 'name': 'Employee', 'salary': 'Salary'})
            results_df = pd.concat([res_depart for res_depart in results.values()])
            
        else:
            results_df = pd.DataFrame([], columns=['Department', 'Employee', 'Salary'])
    #print(results_df)
    return results_df
        