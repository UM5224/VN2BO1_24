styles =['daily','weelky','monthly','yearly']
avg =[70,20,5,1]
results=["most","few","veryfew","few"]

file=zip(styles,avg,results)
all =list(file)
print(all)

styles,avg,results=zip(*all)

print(styles)
print(avg)
print(results)