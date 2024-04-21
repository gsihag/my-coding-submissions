import pandas as pd

def fix_names(users: pd.DataFrame) -> pd.DataFrame:
    for idx,name_str in users['name'].items():
        #print(name_str, len(name_str))
        first_let = name_str[0].upper()
        let_rest = name_str[1:].lower()
        corrected_name = first_let+let_rest
        #print(corrected_name, len(corrected_name))
        users['name'][idx] = corrected_name
    
    users.sort_values(by='user_id', inplace=True)
    return users