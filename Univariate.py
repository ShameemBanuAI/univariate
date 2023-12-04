class Univariate():
    def quanqual(dataset):

        quan=[]
        qual=[]
        for colName in dataset.columns:
            if (dataset[colName].dtypes)=='O':
                qual.append(colName)
            else:
                quan.append(colName)
        return qual,quan
    def Univariate(dataset,quan):
        descriptive=pd.DataFrame(index=["mean","median","mode","Q1:25","Q2:50","Q3:75","99th","Q4:100",
                                       "IQR","1.5IQR","LesserRange","GreaterRange","MinValue","MaxValue",
                                       "Skew","Kurtosis","Variance","StdDeviation"],columns=quan)
        for colName in quan:
            descriptive[colName]["mean"]=dataset[colName].mean()
            descriptive[colName]["median"]=dataset[colName].median()
            descriptive[colName]["mode"]=dataset[colName].mode()[0]
            descriptive[colName]["Q1:25"]=dataset.describe()[colName]["25%"]
            descriptive[colName]["Q2:50"]=dataset.describe()[colName]["50%"]
            descriptive[colName]["Q3:75"]=dataset.describe()[colName]["75%"]
            descriptive[colName]["99th"]=np.percentile(dataset[colName],99)
            descriptive[colName]["Q4:100"]=dataset.describe()[colName]["max"]
            descriptive[colName]["IQR"]=descriptive[colName]["Q3:75"]- descriptive[colName]["Q1:25"]
            descriptive[colName]["1.5IQR"]=1.5 * descriptive[colName]["IQR"]
            descriptive[colName]["LesserRange"]= descriptive[colName]["Q1:25"] - descriptive[colName]["1.5IQR"]
            descriptive[colName]["GreaterRange"]= descriptive[colName]["Q3:75"] + descriptive[colName]["1.5IQR"]
            descriptive[colName]["MinValue"]=dataset[colName].min()
            descriptive[colName]["MaxValue"]=dataset[colName].max()
            descriptive[colName]["Skew"]=dataset[colName].skew()
            descriptive[colName]["Kurtosis"]=dataset[colName].kurtosis()
            descriptive[colName]["Variance"]=dataset[colName].var()
            descriptive[colName]["StdDeviation"]=dataset[colName].std()
        return descriptive

    
   
    
    def freqTable(colName,dataset):
        freqTable=pd.DataFrame(columns=["UniqueValues","Frequency","RelativeFrequency","Cusum"])
        freqTable["UniqueValues"]=dataset[colName].value_counts().index
        freqTable["Frequency"]=dataset[colName].value_counts().values
        freqTable["RelativeFrequency"]=freqTable["Frequency"]/len(dataset[colName])
        freqTable["Cusum"]=freqTable["RelativeFrequency"].cumsum()
        return freqTable