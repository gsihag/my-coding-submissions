import pandas as pd

def article_views(views: pd.DataFrame) -> pd.DataFrame:
    author = pd.DataFrame(views[(views['author_id'] == views['viewer_id'])]['author_id'].unique(), columns=['id']).sort_values(by=['id'])
    return author