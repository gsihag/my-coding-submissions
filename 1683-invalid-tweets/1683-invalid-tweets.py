import pandas as pd

def invalid_tweets(tweets: pd.DataFrame) -> pd.DataFrame:
    res1 = {}
    for i in range(len(tweets['content'])):
        res1[tweets['tweet_id'][i]] = len(tweets['content'][i])
    print(res1)
    tweet_ = [i for i in res1.keys() if res1[i]> 15]
    print(tweet_)
    if len(tweet_) == 0:
        return pd.DataFrame([],columns=['tweet_id'])
    else:
        return pd.DataFrame(tweet_, columns=['tweet_id'])
    