# --------------
# Import packages
import numpy as np
import pandas as pd
from scipy.stats import mode 

# code starts here

bank = pd.read_csv(path)

categorical_var = bank.select_dtypes(include = ['object'])
print(categorical_var)

numerical_var = bank.select_dtypes(include = ['number'])
print(numerical_var)
# code ends here


# --------------
# code starts here


#code ends here

bank = bank.drop(['Loan_ID'], axis=1)
print(bank.isnull().sum())
bank_mode = bank.mode
print(bank_mode)
banks = bank.fillna(bank_mode)
print(banks)




# --------------
# Code starts here

avg_loan_amount = banks.pivot_table(index = ['Gender', 'Married', 'Self_Employed'],values='LoanAmount',aggfunc=np.mean)

# code ends here



# --------------
# code starts here
loan_approved_se = banks[(banks['Self_Employed'] == 'Yes') & (banks['Loan_Status']=='Y')].count()

loan_approved_se = loan_approved_se['Loan_Status']

loan_approved_nse = banks[(banks['Self_Employed'] == 'No') & (banks['Loan_Status']=='Y')].count()

loan_approved_nse = loan_approved_nse['Loan_Status']

percentage_se = (loan_approved_se/614)*100
percentage_nse = (loan_approved_nse/614)*100

# code ends here


# --------------
# code starts here

loan_term = banks['Loan_Amount_Term'].apply(lambda x: x/12)

big_loan_term = len(banks[loan_term>=25])

# code ends here



# --------------
# code ends here

loan_groupby = banks.groupby(['Loan_Status'])['ApplicantIncome', 'Credit_History']
print(loan_groupby)

mean_values = loan_groupby.mean()
print(mean_values)
# code ends here


