#pandas series
import pandas as pd
l=["daily","weekly","monthly"]
var = pd.Series(l)
print(var)

data={
    "l1" : [1,2,3],
    "l2": ['telugu', 'tamil', 'english']
}
df = pd.DataFrame(data)
print(df)

#The head() method returns the headers and a specified number of rows, starting from the top
df = pd.read_csv('new.csv')

print(df.head(10))

#corr() method:-The corr() method calculates the relationship between each column in your data set

df = pd.read_csv('data.csv')

print(df.corr())