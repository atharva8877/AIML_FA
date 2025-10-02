import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np

# Create sample dataframe
np.random.seed(42)
data = {
    'average': np.random.normal(75, 10, 1000),
    'gender': np.random.choice(['male', 'female'], 1000),
    'race/ethnicity': np.random.choice(['group A', 'group B', 'group C', 'group D', 'group E'], 1000),
    'math score': np.random.normal(70, 15, 1000),
    'reading score': np.random.normal(75, 12, 1000),
    'writing score': np.random.normal(72, 14, 1000),
    'lunch': np.random.choice(['standard', 'free'], 1000),
    'test preparation course': np.random.choice(['none', 'completed'], 1000),
    'parental level of education': np.random.choice(['some high school', 'high school', 'some college', "associate's degree", "bachelor's degree", "master's degree"], 1000)
}
df = pd.DataFrame(data)

plt.rcParams['figure.figsize'] = (30, 12)

plt.subplot(1, 5, 1)
size = df['gender'].value_counts()
labels = 'Female', 'Male'
color = ['red','green']


plt.pie(size, colors = color, labels = labels,autopct = '.%2f%%')
plt.title('Gender', fontsize = 20)
plt.axis('off')



plt.subplot(1, 5, 2)
size = df['race/ethnicity'].value_counts()
labels = 'Group C', 'Group D','Group B','Group E','Group A'
color = ['red', 'green', 'blue', 'cyan','orange']

plt.pie(size, colors = color,labels = labels,autopct = '.%2f%%')
plt.title('Race/Ethnicity', fontsize = 20)
plt.axis('off')



plt.subplot(1, 5, 3)
size = df['lunch'].value_counts()
labels = 'Standard', 'Free'
color = ['red','green']

plt.pie(size, colors = color,labels = labels,autopct = '.%2f%%')
plt.title('Lunch', fontsize = 20)
plt.axis('off')


plt.subplot(1, 5, 4)
size = df['test preparation course'].value_counts()
labels = 'None', 'Completed'
color = ['red','green']

plt.pie(size, colors = color,labels = labels,autopct = '.%2f%%')
plt.title('Test Course', fontsize = 20)
plt.axis('off')


plt.subplot(1, 5, 5)
size = df['parental level of education'].value_counts()
labels = 'Some College', "Associate's Degree",'High School','Some High School',"Bachelor's Degree","Master's Degree"
color = ['red', 'green', 'blue', 'cyan','orange','grey']

plt.pie(size, colors = color,labels = labels,autopct = '.%2f%%')
plt.title('Parental Education', fontsize = 20)
plt.axis('off')


plt.tight_layout()
plt.grid()

plt.show()

gender_group = df.groupby('gender').mean(numeric_only=True)
gender_group

plt.figure(figsize=(10, 8))

X = ['Total Average','Math Average']


female_scores = [gender_group['average']['female'], gender_group['math score']['female']]
male_scores = [gender_group['average']['male'], gender_group['math score']['male']]

X_axis = np.arange(len(X))
  
plt.bar(X_axis - 0.2, male_scores, 0.4, label = 'Male')
plt.bar(X_axis + 0.2, female_scores, 0.4, label = 'Female')
  
plt.xticks(X_axis, X)
plt.ylabel("Marks")
plt.title("Total average v/s Math average marks of both the genders", fontweight='bold')
plt.legend()
plt.show()

f,ax=plt.subplots(1,2,figsize=(20,10))
sns.countplot(x='race/ethnicity', data=df, palette = 'bright',ax=ax[0],saturation=0.95)
for container in ax[0].containers:
    ax[0].bar_label(container,color='black',size=20)
    
ax[1].pie(x = df['race/ethnicity'].value_counts(),labels=df['race/ethnicity'].value_counts().index,explode=[0.1,0,0,0,0],autopct='%1.1f%%',shadow=True)
plt.show()

Group_data2=df.groupby('race/ethnicity')
f,ax=plt.subplots(1,3,figsize=(20,8))
sns.barplot(x=Group_data2['math score'].mean().index,y=Group_data2['math score'].mean().values,palette = 'mako',ax=ax[0])
ax[0].set_title('Math score',color='#005ce6',size=20)

for container in ax[0].containers:
    ax[0].bar_label(container,color='black',size=15)

sns.barplot(x=Group_data2['reading score'].mean().index,y=Group_data2['reading score'].mean().values,palette = 'flare',ax=ax[1])
ax[1].set_title('Reading score',color='#005ce6',size=20)

for container in ax[1].containers:
    ax[1].bar_label(container,color='black',size=15)

sns.barplot(x=Group_data2['writing score'].mean().index,y=Group_data2['writing score'].mean().values,palette = 'coolwarm',ax=ax[2])
ax[2].set_title('Writing score',color='#005ce6',size=20)

for container in ax[2].containers:
    ax[2].bar_label(container,color='black',size=15)

plt.rcParams['figure.figsize'] = (15, 9)
plt.style.use('fivethirtyeight')
sns.countplot(df['parental level of education'], palette = 'Blues')
plt.title('Comparison of Parental Education', fontweight = 30, fontsize = 20)
plt.xlabel('Degree')
plt.ylabel('count')
plt.show()

df.groupby('parental level of education').agg('mean', numeric_only=True).plot(kind='barh',figsize=(10,10))
plt.legend(bbox_to_anchor=(1.05, 1), loc=2, borderaxespad=0.)
plt.show()

plt.rcParams['figure.figsize'] = (15, 9)
sns.countplot(df['lunch'], palette = 'PuBu')
plt.title('Comparison of different types of lunch', fontweight = 30, fontsize = 20)
plt.xlabel('types of lunch')
plt.ylabel('count')
plt.show()

plt.figure(figsize=(12,6))
plt.subplot(2,2,1)
sns.barplot(x='lunch', y='math score', hue='test preparation course', data=df)
plt.title('Math Score by Lunch and Test Preparation')

plt.subplot(2,2,2)
sns.barplot(x='lunch', y='reading score', hue='test preparation course', data=df)
plt.title('Reading Score by Lunch and Test Preparation')

plt.subplot(2,2,3)
sns.barplot(x='lunch', y='writing score', hue='test preparation course', data=df)
plt.title('Writing Score by Lunch and Test Preparation')

plt.tight_layout()
plt.show()

plt.subplots(1,4,figsize=(16,5))
plt.subplot(141)
sns.boxplot(df['math score'],color='skyblue')
plt.title('Math Score')

plt.subplot(142)
sns.boxplot(df['reading score'],color='hotpink')
plt.title('Reading Score')

plt.subplot(143)
sns.boxplot(df['writing score'],color='yellow')
plt.title('Writing Score')

plt.subplot(144)
sns.boxplot(df['average'],color='lightgreen')
plt.title('Average Score')

plt.show()
