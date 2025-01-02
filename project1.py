import seaborn as sns
import pandas as pd

import matplotlib.pyplot as plt

creditcard_df = pd.read_csv('creditcard.csv')

# ● How many rows and columns are in the dataset?

num_cols = len(creditcard_df.columns)
num_rows = len(creditcard_df.index)

print(f'The number of rows is {num_rows} and the num of columns is {num_cols}')
# Or I can also use this to find out print(creditcard_df.info)

# ● What are the column names and their data types?

print(creditcard_df.info())

# ● Are there any missing or null values in the dataset?

is_null = creditcard_df.isna().sum().sum()
print(is_null)
print('There are no NUll or NaN values in the given dataset')

# ● How many transactions are fraudulent, and how many are legitimate?
classes = creditcard_df['Class'].value_counts()
class_legitimate = creditcard_df['Class'].value_counts()[0]
class_fraudulent = creditcard_df['Class'].value_counts()[1]
print(f'There are {class_legitimate} legitimate transactions and {class_fraudulent} fraudulent transactions')
print(classes)

# ● What percentage of transactions are fraudulent?
total = class_legitimate + class_fraudulent
percentage_fraudulent = (class_fraudulent / total ) * 100

print(f'The percentage of fraudulent transactions is {percentage_fraudulent:.2f}%')

# ● What are the minimum, maximum, mean, and median values for
# numerical columns like Amount?

print(creditcard_df['Amount'].describe().loc[['min','max','mean','50%']].to_frame())

# ● What is the maximum transaction amount in the dataset, and is it
# fraudulent?

max_transaction = creditcard_df['Amount'].max()
fraud_or_legit = creditcard_df[creditcard_df['Amount']== max_transaction]['Class'].iloc[0]

print(f'The maximum trasaction is {max_transaction} and it is {'Fraudulent' if {fraud_or_legit} == 1 else 'Legitimate'}')

# ● Can we create a bar chart showing the count of fraudulent vs.
# legitimate transactions?

sns.countplot(x='Class',palette=['khaki','red'], data=creditcard_df)
plt.title('Fraudulent vs Legitimate Transactions')
plt.xticks(ticks=[0,1],labels=['Legitimate','Fraudulent'])
plt.xlabel('Class')
plt.ylabel('Count')
plt.show()

# ● What does the histogram of transaction amounts look like?

sns.histplot(creditcard_df['Amount'], edgecolor='black', bins=30)
plt.title('Histogram of Transaction Amounts')
plt.xlabel('Transaction Amount')
plt.ylabel('Frequency')
plt.show()

# ● Can we use a heatmap to visualize the correlation between numerical features?

sns.heatmap(creditcard_df.corr(), cmap='coolwarm')
plt.title('Correlation between numerical features')
plt.show()
