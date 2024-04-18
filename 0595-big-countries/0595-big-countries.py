import pandas as pd

def big_countries(world: pd.DataFrame) -> pd.DataFrame:
    df_area = pd.DataFrame(world[world['area']>= 3000000])
    df_population = pd.DataFrame(world[world['population']>= 25000000])
    df = pd.concat([df_area, df_population]).drop_duplicates(subset='name')
    return df[['name', 'population', 'area']]