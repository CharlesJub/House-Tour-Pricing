# Intro

One of my favorite YouTube rabit-holes is watching expensive mansion tours, sometime this extends to yatch and private jet tours as well, but the videos I watch are typically made by the same person: Enes Yilmazer.

I wanted to know if Yilmazer uses different words for differently priced homes

# Data

To do this I looked at the transcript of his video catelog. Yilmazer has 283 videos (as of 12/19/2024), but not all of these videos have dollar amounts or are acutal asset listings.

## Gathering Data

## Cleaning and Transforming Data

Removing numbers from script and attaching house value to script

Can look for dollar amount in three places:

1. Title
2. Description
3. Thumbnail

Title and description are the easiest. and Get x / 283 dollar amounts

x left to thumbnail and some internet research. This was done by hand for x number of videos

Left with 239 videos with dollar amounts for analysis

# Analysis

## What Assets are Highlighted on this channel?

This channel mainly focuses on house listings, but it also has some other luxury assets like vehicals. These will definitely have different values so I want to see if I can cluster on each asset type only using the script.

I tried to cluster on only terms to see if I was able to seperate the assets.

I found that clustering on scripts was mostly on date of video creation instead of asset type. This makes sense because as time porgressed Enes changed the way he speaks about properties and develops speaking habits over time. It also could be due to the change in asset cost over time. When Enes started his channel he was reviewing expensive LA homes, but now he travels the world to homes that are up to ten times the price of the homes that he originally was reviewing. This can be captured by the fact that motorhomes and tiny homes are captured in the same cluster as the earlier, less expensive, homes.

The four clusters were:

1. Smaller Assets (early homes, jets, and motorhomes)
2. Covid Year Mansions
3. Yatchs
4. Recent Mansions

**EXPLAIN THE BENIFITS OF USING BISECTING KMEANS HERE**

Bisecting KMeans had an optimal k of three, but I only used two clusters because thge clustering algorithm did a good job of spliting items in to unqiue and traditional assets

1. Unqiue assets (jets, yachts, tiny homes)
2. Traditional

## Home Value Reggression

### TF-IDF

Max features of 1000

| Model                    | MAE            | PCA (100) MAE     | Log Transformation MAE |
| ------------------------ | -------------- | ----------------- | ---------------------- |
| Simple Linear Regression | $23,961,860.07 | \$28,610,099.78   | $23835410.70           |
| LASSO                    | $36,361,297.24 | \$28,609,853.22   | $19162763.31           |
| Ridge                    | $18,785,882.68 | \$18,733,956.39   | $13161090.62           |
| Random Forest            | $19,313,536.10 | \$21,263,132.7679 | $17715967.87           |
| XGBoost                  | $20,009,925.67 | \$20,238,477.8399 | $16835319.53           |
| LIghtGBM                 | $19,944,572.21 | \$22,023,846.4364 | $16968777.14           |
| Support Vector Regession | $23,215,341.70 | \$23,215,341.4186 | $18610803.73           |
| Ensemble                 | $18,837,893.41 | \$19,336,458.87   | $11,888,280.54         |

Using just TF-IDF Matrix able to get down to an average absolute error of $18 million, a pretty good starting point but can be improved

# Future Analysis

Only one channel. Is it possible to do this analysis across multiple channels with different vocabulary and tendencies
