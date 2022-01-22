# KNN-Genre-Classifier
*Note: this was a final project for CSC590 -- Machine Learning.*

## Project Description
This project will attempt to predict a song’s genre based off all the variables in the dataset’s rows. The program will run twice. The first run will attempt to predict genres that are very similar; in this case, they are HipHop, Rap, and Underground Rap. The second run will attempt to predict genres that are not so similar; in this case, they are ‘Techno’, ‘Emo’, ‘Rap’.

- **Given a song’s qualities (i.e., danceability, loudness, etc), can a song’s genre be predicted?**
- **When faced with similar genres, how well will the algorithm classify?**

## Dataset
The Spotify API dataset[^1] illustrates the data Spotify has gathered on songs of various genres. The data was hosted on Kaggle and only holds 15 genres. The datasets variables are explained in Table 1.

### Data Processing
The application of KNN[^2] developed for this project relies on the data being structured in a table format. The algorithm presumes that the non-genre columns contain only numerical data. The data that will be removed are the *'type', 'uri', 'track_href', 'analysis_url', 'Unnamed: 0', ‘song_name’, ‘id’, and 'title'* as they don’t hold any useful data. Then, all the data except for time signature, is normalized from a range of zero to one.

**Table 1: Variable Descriptions of genre_v2.csv**
| Variable | Description|
|------|------|
| Valence | The positivity of the track. Ranges between 0-1.|
|Acousticness | How acoustic a song is. Ranges between 0-1.|
|Danceability | How danceable a song is. Ranges between 0-1.|
|Duration | The length of the track (in milliseconds).|
|Energy | The energy of the track. Ranges between 0-1.|
|Instrumentalness | The ratio of a song being instrumental. Ranges between 0-1.|
|Key | The keys of an octave ranging from 0 to 11, where C is 0 and C# is 1 and so on.|
|Liveness | How “live” a song is. Ranges between 0-1.|
|Loudness | The loudness (dB) of a track. Ranges between -60 and 0 dB.|
|Mode | The modality of a track. Major is 1 and Minor is 0.|
|Speechiness | The length of time in a track a song holds a “human voice”. Ranged between 0-1.|
|Tempo | The tempo of the track in Beat Per Minute (BPM).|
|Type | Describes the tracks as an audio-feature.|
|Track_HREF | The track’s Reference URL.|
|Analysis URL | The song’s Audio Analysis URL.|
|Unnamed: 0 | No Information.|
Title |The track’s title.|

## Methods
The classification model developed in conjunction with this dataset was the K-Nearest Neighbors algorithm. The former captures the distance between points. The method used to perform this is known as the Euclidean distance.

### K-Nearest Neighbors
The way the algorithm was designed was as follows: the K-value is initialized to determine the number of neighbors; the data was loaded; the distance was calculated, and its index was added to a collection; the collection was sorted by distance; and the labels are classified and returned.

#### K-Value
When selecting a K-Value, one must choose a K-Value that will be able to maintain the algorithm’s accuracy when making predictions on unknown data as well as that reduce the number of errors the algorithm will encounter.

**Things to note:**
1. When K is decreased, predictions become less stable.
2. When K is increased, predictions become more stable because of a higher average
3. If K is increased to high, there will be a higher error rate.

## Results
### Statistical Analysis
Before performing any machine learning on my dataset, I wanted to understand the data by performing a genre analysis using seaborn.

#### Data Distribution
<details><summary>Click Here to View Figures</summary>
<p>

![Figure 1](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig1.png)
![Figure 2](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig2.png)
![Figure 3](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig3.png)
![Figure 4](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig4.png)
![Figure 5](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig5.png)
![Figure 6](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig6.png)
![Figure 7](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig7.png)
![Figure 8](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig8.png)
![Figure 9](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig9.png)
![Figure 10](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig10.png)
![Figure 11](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig11.png)
![Figure 12](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig12.png)
![Figure 13](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig13.png)
![Figure 14](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig14.png)
![Figure 15](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig15.png)
![Figure 16](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig16.png)
![Figure 17](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig17.png)
![Figure 18](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig18.png)
![Figure 19](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig19.png)
![Figure 20](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig20.png)
![Figure 21](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig21.png)
![Figure 22](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig22.png)
![Figure 23](https://github.com/torrwill/KNN-Genre-Classifier/blob/main/figures/fig23.png)

</p>
</details>


### Accuracy
The accuracy rates of the KNN model, as explained by *Table 2*, can be described as pretty inaccurate when it comes to classifying genres that are similar such as **‘Hiphop’**, **’Rap’**, and **‘Underground Rap’** because the rates were almost always below *90%*.
With all the tested k-values as shown by *Table 3*, the classifier mistook the **‘Hiphop’** songs for **‘Rap’** songs and would struggle with classifying **‘Underground Rap’** between **‘Rap’** and **‘Hiphop’**.
When it came to classifying genres that are different, the classifier determined that **techno** and **Emo** had a similar sound as it mistook the two songs as the specific genres. Most of my runs, the classifier successfully determined **Emo** as the genre it was trying to find. The accuracy returned *69.4%* on a lot of runs as **Emo** was almost always right and I am assuming the rest were at the very least half right.

**Table 2: K-Value Accuracy Ratings (Hiphop, Rap, Underground Rap)**
|Kvalue |Error|Accuracy Rating|
|---|---|---|
|1|0.5|0.5|
|2|0.6|0.4|
|3|0.4|0.6|

**Table 3: K-Value Accuracy Ratings (Techno, Emo, Rap)**
|Kvalue |Error| Accuracy Rating|
|---|---|---|
|1|0.3|0.7|
|2|0.2|0.8|
|3|0.18|0.82|

[^1]: [Kaggle: Spotify Dataset](https://www.kaggle.com/mrmorj/dataset-of-songs-in-spotify)
[^2]: Introduction to Data Mining (Second Edition) by Pang-Ning Tan