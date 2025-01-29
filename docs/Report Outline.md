# Intro

The intersection of luxury real estate and social media has created a fascinating niche on YouTube, where mansion tour videos have become increasingly popular. Among the most prominent creators in this space is Enes Yilmazer, whose channel has garnered significant attention  for its detailed walkthroughs of some of the world's most expensive properties, from luxurious mansions to superyachts and private jets.

A compelling question arises: Does the language used in these videos correlate with the price points of the properties being showcased? This analysis aims to explore the relationship between verbal presentation and property value by examining the linguistic patterns in Yilmazer's video catalog spanning 283 videos as of December 2024.

# Data Collection and Preparation

## Source Data Overview

The analysis is based on Enes Yilmazer's YouTube channel, which contained 283 videos as of December 2024. The dataset required extensive preprocessing to prepare for analysis, primarily focusing on:

* Video transcripts
* Video titles and descriptions
* Property valuations
* Asset classification

## Property Value Identification

Property values were identified through a three-tier approach:

1. **Title Extraction**: Primary source for property values, typically explicitly stated
2. **Description Analysis**: Secondary source when titles didn't contain pricing information
3. **Manual Research**: For remaining videos, values were determined through:
   * Thumbnail information
   * Internet research of property listings
   * Cross-referencing with real estate databases

## Data Cleaning Process

The cleaning process involved several key steps:

1. **Transcript Standardization**

* Removal of timestamps
* Normalization of text (lowercase, punctuation removal)
* Elimination of common YouTube-specific phrases and filler words

2. **Value Standardization**

* Converting all prices to USD
* Normalizing price formats (e.g., "12.5M" to "12500000")
* Verification of current values versus historical listing prices

3. **Asset Classification**

* Categorization of properties (mansions, penthouses, etc.)
* Identification of non-residential assets (yachts, jets)
* Tagging of special features or unique characteristics

## Final Dataset Composition

After cleaning and validation:

* 239 videos with confirmed dollar amounts
* Complete transcripts for all included videos
* Standardized property values
* Asset classification tags

The resulting dataset provides a robust foundation for analyzing the relationship between linguistic patterns and property values across different types of luxury assets.

# Analysis

The initial investigation focused on distinguishing different types of luxury assets through natural language processing of video
transcripts. Rather than relying on explicit categorization, this approach allowed patterns to emerge naturally from the language used in presentations.
Using unsupervised learning techniques, four distinct clusters emerged from the data, each representing different periods and types of content on Yilmazer's channel. The first cluster predominantly contained earlier content, including smaller luxury homes valued between $1M-$10M, along with private jets and high-end motorhomes. These videos typically featured simpler vocabulary and shorter tour durations. The second cluster centered around properties filmed during the COVID-19 pandemic (2020-2021), primarily mansions in the $10M-$50M range, with notable emphasis on home offices and wellness amenities.

Yacht tours formed their own distinct cluster, characterized by specialized maritime vocabulary and detailed technical specifications. The fourth cluster comprised recent ultra-luxury mansion tours, typically properties valued above $50M, featuring more sophisticated vocabulary and longer, more detailed presentations of architectural features and amenities.

The decision to implement Bisecting K-Means clustering proved particularly effective for this analysis. This method offered several advantages over traditional K-Means clustering, including better handling of outliers and more consistent results with text data. The algorithm successfully separated assets into two primary categories: unique assets (jets, yachts, tiny homes) and traditional properties (mansions, estates, penthouses).

For price prediction, various regression models were tested using TF-IDF features with a maximum of 1000 features. Ridge Regression showed particularly strong performance, maintaining consistency across different feature sets and suggesting the presence of multicollinearity in the features. The ensemble method, combining multiple models, achieved the best overall performance with a mean absolute error of $11.89M after log transformation of price values.

Location-related terms, luxury amenity descriptions, and architectural vocabulary emerged as strong predictive features across all models. Interestingly, while principal component analysis (PCA) was tested as a dimensionality reduction technique, it didn't consistently improve results, suggesting that important information was contained in the original feature set. The analysis demonstrates that linguistic patterns in luxury real estate videos can indeed predict property values with reasonable accuracy. However, there remains significant room for improvement through further refinement of features and model architecture. Future work could explore incorporating visual features or expanding the analysis to multiple channels to create a more robust prediction model.

## Model Performance Comparison

| Model Type        | MAE     |
| ----------------- | ------- |
| Linear Regression | $23.84M |
| Ridge             | $13.16M |
| Random Forest     | $17.72M |
| Ensemble          | $11.89M |


## Conclusion and Future Directions

This analysis demonstrates that linguistic patterns in luxury real estate videos can effectively predict property values, achieving a mean  absolute error of $11.89M through ensemble modeling. We observed clear evolution in Yilmazer's presentation style as his channel progressed from local LA properties to international ultra-luxury estates, with vocabulary and tour comprehensiveness adapting to match increasing property values.

## Current Limitations

* Single-channel analysis
* Sample size of 239 properties
* Text-only analysis, excluding visual elements
* Market fluctuation effects not considered

## Future Opportunities

The most promising directions for expanding this research include:

* Cross-channel analysis incorporating other luxury real estate creators
* Integration of visual elements through computer vision
* Addition of market context and economic indicators
* Implementation of advanced language models and custom embeddings

These enhancements could provide deeper insights into how luxury properties are presented across digital platforms while improving prediction accuracy. As luxury real estate content continues to grow in popularity, such analytical approaches become increasingly valuable for understanding high-value property presentation in digital media.
