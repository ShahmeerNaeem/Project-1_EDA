
Exploratory Data Analysis (EDA): Credit Card Fraud Detection

I’ve recently completed an EDA project on a Credit Card Fraud Detection Dataset, focusing on identifying patterns in fraudulent transactions. Here’s what I uncovered:

Number of Rows and Columns
	•	Rows: 284,807
	•	Columns: 31

Missing Values or NaN
	•	No missing or null values were found in the dataset, making it clean and ready to analyze.

Transaction Analysis
	•	Legitimate Transactions: 284,315
	•	Fraudulent Transactions: 492

Fraudulent Transaction Percentage
	•	Fraudulent transactions make up only 0.17% of the dataset, which highlights the severe class imbalance.

Statistics of Transaction Amount
	•	Minimum Amount: 0.0
	•	Maximum Amount: 25,691.16 (this was a legitimate transaction!)
	•	Mean Amount: 88.35
	•	Median Amount: 22.0

Insights from Visualizations
	•	Histogram: Most transaction amounts fall between 0 and 5,000, and the data is right-skewed.
	•	Bar Chart: A simple fraud vs. legitimate bar chart didn’t work well due to the huge class imbalance.
	•	Correlation Analysis: Heatmaps didn’t add much value here, so scatter plots worked better for exploring relationships between numerical features.

This was a foundational project for me, and it’s been super insightful! I’m looking forward to exploring more complex datasets and tackling advanced projects in the future
