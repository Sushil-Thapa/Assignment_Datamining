import json
import math
with open("data.json") as json_file:
    json_data = json.load(json_file)
    print(json_data)

#Calculation
def totalEntropy():
    dataLength=0
    for classes in json_data:
        if classes == 'data':
            for data1 in json_data['data']:
                dataLength=dataLength+1
    print "Total data= %s " %dataLength
    classes1 = []
    classeswithcount = []
    y=0.0
    n=0.0
    count=0.0
    sum=0.0
    for i in range(0, dataLength, 1):
            index =(json_data['data'][i]['playball'],classes1)
            for yescount in index:
                if yescount=='yes':
                    y=y+1
                elif yescount=='no':
                    n=n+1
    classArray=[y,n]
    for value in classArray:
        sum=sum-((value/dataLength)*(math.log((value/dataLength),2)))
    print "Total entropy = %s " %sum
    return sum

def generalEntropy(proportiona,proportionb):
    y=proportiona
    n=proportionb
    sum=0.0
    classArray=[y,n]
    for value in classArray:
        if(value!=0):
            sum=sum-((value)*(math.log((value),2)))
        else:
            sum=sum
    return sum

def totalLength():
    dataLength=0
    classes1 = []
    for classes in json_data:
        if classes == 'data':
            for data1 in json_data['data']:
                dataLength=dataLength+1
    return dataLength

def twoPropertyGain(att,prop1,prop2):
    dataLength=totalLength()
    attributearray = []
    totalEntropyValue = totalEntropy()
    for i in range(0, dataLength, 1):
        attributearray.append({"attr":json_data['data'][i][att],"classname":json_data['data'][i]['playball']})
    #print attributearray[0]['classname']
    Sweakn=0.0
    Sweaky=0.0
    Sstrongn=0.0
    Sstrongy=0.0
    for i in range(0,dataLength,1):
        if(attributearray[i]['classname']=='no'):
            if(attributearray[i]['attr']==prop1):
                Sweakn=Sweakn+1
            else:
                Sstrongn=Sstrongn+1
        else:
            if(attributearray[i]['attr']==prop1):
                Sweaky=Sweaky+1
            else:
                Sstrongy=Sstrongy+1
    proportion1=Sweaky/(Sweakn+Sweaky)
    proportion2=Sweakn/(Sweakn+Sweaky)
    proportion3=Sstrongy/(Sstrongn+Sstrongy)
    proportion4=Sstrongn/(Sstrongn+Sstrongy)
    entropyweak=generalEntropy(proportion1,proportion2)
    print(" Entropy of %s " %prop1 +"of %s " %att +" is %s "%entropyweak  )
    entropystrong=generalEntropy(proportion3,proportion4)
    print(" Entropy of %s " %prop2 +"of %s " %att +" is %s "%entropystrong  )
    value=(entropyweak*((Sweakn+Sweaky)/dataLength))+(entropystrong*((Sstrongn+Sstrongy)/dataLength))
    gain=totalEntropyValue-value
    return gain

def threePropertyGain(att,prop1,prop2,prop3):
    dataLength=totalLength()
    attributearray = []
    totalEntropyValue = totalEntropy()
    for i in range(0, dataLength, 1):
        attributearray.append({"attr":json_data['data'][i][att],"classname":json_data['data'][i]['playball']})
    Shotn=0.0
    Shoty=0.0
    Smildn=0.0
    Smildy=0.0
    Scooln=0.0
    Scooly=0.0

    for i in range(0,dataLength,1):
        if(attributearray[i]['classname']=='no'):
            if(attributearray[i]['attr']==prop1):
                Shotn=Shotn+1
            elif(attributearray[i]['attr']==prop2):
                Smildn=Smildn+1
            else:
                Scooln=Scooln+1
        else:
            if(attributearray[i]['attr']==prop1):
                Shoty=Shoty+1
            elif(attributearray[i]['attr']==prop2):
                Smildy=Smildy+1
            else:
                Scooly=Scooly+1
    proportion1=Shoty/(Shotn+Shoty)
    proportion2=Shotn/(Shotn+Shoty)
    proportion3=Smildy/(Smildn+Smildy)
    proportion4=Smildn/(Smildn+Smildy)
    proportion5=Scooly/(Scooln+Scooly)
    proportion6=Scooln/(Scooln+Scooly)
    entropyshot=generalEntropy(proportion1,proportion2)
    print(" Entropy of %s " %prop1 +"of %s " %att +" is %s "%entropyshot  )
    entropysmild=generalEntropy(proportion3,proportion4)
    print(" Entropy of %s " %prop2 +"of %s " %att +" is %s "%entropysmild  )
    entropyscool=generalEntropy(proportion5,proportion6)
    print(" Entropy of %s " %prop3 +"of %s " %att +" is %s "%entropyscool  )
    value=(entropyshot*((Shotn+Shoty)/dataLength))+(entropysmild*((Smildn+Smildy)/dataLength))+(entropyscool*((Scooln+Scooly)/dataLength))
    gain=totalEntropyValue-value
    return gain

def gain(attribute):
    dataLength=totalLength()
    if(attribute=='wind'):
        gain=twoPropertyGain('wind','weak','strong')
        print ("gain of WIND= %s" %gain)

    elif(attribute=='humidity'):
        gain=twoPropertyGain('humidity','high','normal')
        print ("gain of HUMIDITY= %s" %gain)

    elif(attribute=='outlook'):
        gain=threePropertyGain('outlook','sunny','overcast','rain')
        print ("gain of OUTLOOK= %s" %gain)

    elif(attribute=='temp'):
        gain=threePropertyGain('temp','hot','mild','cool')
        print ("gain of TEMPERATURE= %s" %gain)
    return gain

#GUI
import Tkinter
from Tkinter import *
root = Tk()
T1 = Text(root, height=2, width=34)
T1.pack()
T2 = Text(root, height=2, width=35)
T2.pack()
T3 = Text(root, height=2, width=34)
T3.pack()
T4 = Text(root, height=2, width=33)
T4.pack()
def resultwind():
    T1.delete(END)
    T1.insert(END, 'The information gain of  Wind  is  %s' %gain('wind'))
def resulttemperature():
    T2.delete(END)
    T2.insert(END, 'The information gain of  Temperature  is  %s' %gain('temp'))
def resulthumidity():
    T3.delete(END)
    T3.insert(END, 'The information gain of  Humidity  is  %s' %gain('humidity'))
def resultoutlook():
    T4.delete(END)
    T4.insert(END, 'The information gain of  Outlook  is  %s' %gain('outlook'))


Label(root,  text='Click to get Information Gain').pack(side=TOP)
Button(root, text='Wind', command=resultwind).pack(side=LEFT)
Button(root, text='Temperature', command=resulttemperature).pack(side=RIGHT)
Button(root, text='Humidity', command=resulthumidity).pack(side=LEFT)
Button(root, text='Outlook', command=resultoutlook).pack(side=RIGHT)
root.mainloop()
