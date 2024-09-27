# %%
# import packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %%
# show the title
sns.set()
st.title('Titanic App by Tianqi Liu')

# %%
# read csv and show the dataframe
df=pd.read_csv('train.csv')
st.write(df)

# %%
# create a figure with three subplots, size should be (15, 5)
# show the box plot for ticket price with different classes
# you need to set the x labels and y labels
# a sample diagram is shown below
import matplotlib.pyplot as plt
fig,ax=plt.subplots(1,3,figsize=[15,5])
df_sorted1=df_train[df_train.Pclass==1]
df_sorted2=df_train[df_train.Pclass==2]
df_sorted3=df_train[df_train.Pclass==3]
#df_train[df_train.Pclass==1].Fare.plot.box()
ax[0].boxplot(df_sorted1.Fare)
ax[0].set_xlabel('paclass=1')
ax[0].set_xticks([1])  # Position for the label
ax[0].set_xticklabels(['Fare'])  # Label for the x-axis
ax[1].boxplot(df_sorted2.Fare)
ax[1].set_xlabel('paclass=2')
ax[1].set_xticks([1])  # Position for the label
ax[1].set_xticklabels(['Fare'])  # Label for the x-axis
ax[2].boxplot(df_sorted3.Fare)
ax[2].set_xlabel('paclass=3')
ax[2].set_xticks([1])  # Position for the label
ax[2].set_xticklabels(['Fare'])  # Label for the x-axis
ax[0].set_ylabel('Fare')



