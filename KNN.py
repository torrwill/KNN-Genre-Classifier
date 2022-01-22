import numpy as np
import pandas as pd
from collections import Counter

#############################
#         Distance          #
#############################

# worked with Kavindra to understand determining distance via numpy (provided the stack overflow link)
def get_distance(df_test, df_train):
  # init distance list
  distances = []

  # determine the euclidian distance
  # stack overflow: https://stackoverflow.com/questions/1401712/how-can-the-euclidean-distance-be-calculated-with-numpy
  for i,j in df_test.iterrows():
    
    # set a and b values
    a = np.array(j[1:5])
    b = df_train.iloc[:,1:].to_numpy()

    # calculate euclidian distance
    euclid_distance = np.linalg.norm(a - b, axis = 1)

    # for the indexes i and j, append the distances found by euclid_distance in the Type column in df_train: 
    distances.append([[i,j] for i,j in zip(euclid_distance.tolist(), df_train['Type'].tolist())])
  
  return distances

#############################
#     Nearest Neighbors     #
#############################
def determine_knn(distances):
  # worked with Kavindra to estimate the nearest neighbors
  
  # init count lists
  count_total = []
  count = []
  
  # init k value
  k = 10

  # get types from the euclid_distance
  for x in distances:

    # for each "type" in "distance", 
    # take the first k values and sort from highest to lowest distance
    # (explanation provided by Kavindra)
    neighbors = [dist_list[1] for dist_list in sorted(x)[:k]] 
    
    # append the neighbors to count
    count.append(neighbors)

    # calculate the most common values from the first indeces
    count_result = Counter(neighbors).most_common(1)[0][0]

    # append total count value to count_total
    count_total.append((count_result))

  return count_total

#############################
#          Average          #
#############################
def determine_accuracy_rate(distances, df_test):
  # append predicitions to df_test; check the rows that are correct
  df_test["count"] = determine_knn(distances)    

  # init counter list
  accuracy_count = []

  # find values in "Type" that equal to count and set as booleans
  comparison = np.where(df_test["Type"] == df_test["count"], True, False)
  
  # if there is a True value in df_test["count"], it gets added to accuracy_count
  for i in comparison:
      if i == True:
          accuracy_count.append(1)

  return accuracy_count

#############################
#       Run Classifier      #
#############################

def main():

  # load data
  #df = pd.read_excel('./IrisDataSet.xlsx')


  df = pd.read_csv("genres_v2.csv")
  #print(df.head())
  #print(df.shape)
  #print(df.isna().sum())

  # clear unwanted data
  df = df.drop(['type', 'uri', 'track_href', 'analysis_url', 'Unnamed: 0', 'title'], 1)
  df = df.drop(['song_name', 'id'], 1)


  genres = ['Dark Trap', 'dnb', 'Emo', 'hardstyle',
            'Hiphop', 'Pop', 'psytrance', 'Rap',
            'RnB', 'techhouse', 'techno', 'trance',
            'trap', 'Trap Metal', 'Underground Rap']
  
  for i in range(len(genres)):
    df.loc[(df.genre == genres[i]),'genre'] = i
  print(df.head())
  
  # selecting rows based on condition

  df_1 = df.loc[df['genre'] == 5] # pop
  df_2 = df.loc[df['genre'] == 2] # emo
  df_3 = df.loc[df['genre'] == 10] # techno


  #df_1 = df.loc[df['genre'] == 4] # hiphop
  #df_2 = df.loc[df['genre'] == 7] # rap
  #df_3 = df.loc[df['genre'] == 13] # und. rap

  frames = [df_1, df_2, df_3]
  df = pd.concat(frames)
  print(df)
  
  #########################
  # Scale between 0 and 1 #
  #########################
  df["key"] = (df["key"] / df["key"].max())
  df["tempo"] = (df["tempo"] / df["tempo"].max())
  df["loudness"] = (df["loudness"] / df["loudness"].min())
  #print(df.head())
  
  # split data
  df_train = df.sample(frac=0.10)
  df_test = df[~(df.index.isin(df_train.index))]

  # run functions
  distances = get_distance(df_test, df_train)
  determine_accuracy_rate(distances, df_test)

main()
