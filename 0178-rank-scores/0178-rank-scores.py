import pandas as pd

#--- Method 1 -----------

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    # Sort the scores in descending order based on the 'score' column
    scores = scores.sort_values(by='score', ascending=False)

    # Drop the 'id' column and reset the index
    scores = scores.drop(columns=['id']).reset_index(drop=True)

    # Initialize an empty list to store the ranks
    rank = []

    # Loop through each row in the sorted DataFrame
    for i in range(len(scores)):
        # If this is the first row, assign a rank of 1
        if i == 0:
            rank.append(1)
        # If the current score is the same as the previous score, assign the same rank
        elif scores['score'][i] == scores['score'][i-1]:
            rank.append(rank[i-1])
        # If the current score is less than the previous score, assign a new rank
        elif scores['score'][i] < scores['score'][i-1]:
            rank.append((rank[i-1]+1))

    # Add the 'rank' column to the DataFrame
    scores['rank'] = rank

    # Return the modified DataFrame
    return scores

'''
#--- Method 2 -----------
def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores['rank'] = scores['score'].rank(method='dense', ascending=False)
    return scores.drop('id', axis=1).sort_values('score', ascending=False)

'''