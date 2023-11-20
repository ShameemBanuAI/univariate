class Univariate():
    def quanqual(dataset):
        quan=[]
        qual=[]
        for colName in dataset.columns:
            #print(columnName)
            if (dataset[colName].dtypes=='O'):
               # print("Qual")
                qual.append(colName)
               # print(qual)
            else:
                #print("quan")
                quan.append(colName)
              #  print(quan)
        return quan,qual