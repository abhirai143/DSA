import pandas as pd
names=['stuudent1','student2','student3','student4']
marks_percentage=[80,90,70,60]
studentDataSet=list(zip(names,marks_percentage))
print(studentDataSet) 

df=pd.DataFrame(data=studentDataSet,columns=['names','marks_percentage'])
print(df)
