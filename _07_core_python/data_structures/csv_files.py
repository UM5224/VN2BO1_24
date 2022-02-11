import pandas as pd
cd =pd.read_csv("annual.csv")
print(cd)
cd.to_csv("new.csv") #write the data to new.csv file

print(pd.__version__)

styles =['daily','weelky','monthly','yearly']
avg =[70,20,5,1]


ser =pd.Series(styles,avg)
print(ser)