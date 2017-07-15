# To determine whether to provide loan or not!!
import math
import json
with open("data2.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)
newAge=input("Please Enter Your Age!")
newLoan=input("Please Enter Your Required Loan!")
k=input("Value Of K ")#Enter K=1
distance=[]
sortedarray=[]

def totalLength():# finding total dataLength
    dataLength=0
    for classes in json_data:
        if classes == 'data':
            for data1 in json_data['data']:
                dataLength=dataLength+1
    return dataLength

def EuclidianDistance():#measuring Distance
    dataLength=totalLength()
    print(dataLength)
    classes=[]
    for i in range(0,dataLength,1):
        print(json_data['data'][i]['Age'])
        print(json_data['data'][i]['Loan'])
        distance.append(math.sqrt((((json_data['data'][i]['Age'])-(newAge))*((json_data['data'][i]['Age'])-(newAge)))+(((json_data['data'][i]['Loan'])-(newLoan))*((json_data['data'][i]['Loan'])-(newLoan)))))
        classes.append({"dis":distance[i],"attr":json_data['data'][i]['GiveLoan']})
    return classes

def main():
    final=EuclidianDistance()
    print(final)
    dataLength=totalLength()
    nearest=final[0]['dis']
    Firstfinal=[]
    Secondlowest=[]
    for i in range(0,dataLength,1):
        if(final[i]['dis']<nearest): #sort the data .. find the minimum
            nearest=final[i]['dis']
            Firstfinal=({"att":final[i]['attr'],"dist":final[i]['dis']})

    print(nearest) #print minimum data
    print(Firstfinal)
    if(k==1):
        print(" The Nearest Neighbour is %s" %Firstfinal) #for k=1 only;
        value=Firstfinal['att']
        if(value=='yes'):
            print("Congratulations! You can get Loan from us!")
        else:
            print("Sorry! You cannot get loan from us!")
main()
