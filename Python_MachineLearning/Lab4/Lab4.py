import numpy as np
import matplotlib.pyplot as plt
from pandas import read_csv
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier

accuracyAthroisma=0
precisionAthroisma=0
recallAthroisma=0
fmeasureAthroisma=0
sensitivityAthroisma=0
specificityAthroisma=0

def evaluate(t, predict,criterion):
  
  global tn,fn,tp,fp
  global precisionP,recallP,fmeasure,sensitivity,specificity
  global accuracyAthroisma,precisionAthroisma,recallAthroisma,fmeasureAthroisma
  global sensitivityAthroisma,specificityAthroisma
  
  tp=0.0
  fn=0.0
  tn=0.0
  fp=0.0
  for i in range(0,15):
      if((t[i]==0 and predict[i]==0) ):
        tn +=1
      elif((t[i]==1 and predict[i]==0) ):
        fn +=1
      elif((t[i]==1 and predict[i]==1) ):
        tp +=1
      elif((t[i]==0 and predict[i]==1) ):
        fp +=1
  
  if(criterion =="accuracy"):   
    accuracy=(tp+tn)/(tp+tn+fp+fn)
    accuracyAthroisma += accuracy
    print "Accuracy: ",accuracy
    
 
  elif(criterion =="precision"):
    p1=(tp+fp)
    if(p1 !=0):
     precisionP=tp/p1
    else:
     precisionP=99999
    precisionAthroisma += precisionP
    #precisionP=precision
    #print "Precision: ",precision
  
  elif(criterion =="recall"):
    re=tp+fn
    if(re !=0):
     recall=tp/re
    else:
      recall=999999
    recallAthroisma += recall
    
    recallP=recall
    print "Recall: ",recall

  elif(criterion =="fmeasure"):
    f1=(precisionP+recallP)/2
    if(f1 !=0):
     fmeasure=(precisionP*recallP)/f1
    fmeasureAthroisma += fmeasure  
    print "Fmeasure: ",fmeasure
  
  elif(criterion =="sensitivity"):
    s1=tp+fn
    if(s1 !=0):
     sensitivity=tp/(tp+fn)
    else:
      sensitivity=999999
    sensitivityAthroisma +=sensitivity
    
    print "sensitivity: ", sensitivity
  elif(criterion =="specificity"):
    specificity = tn/(tn+fp)
    specificityAthroisma += specificity
    print "specificity: ", specificity
    
#diavazoyme apo to arxeio iris.data kai ta vazoume se ena object d
d=read_csv('iris.data',header=None).values

#plithos twn xaraktiristikwn dhladh ti xaraktirizei ena louloudi
print "NumberOfAttributes",d.shape[1]
#plitos twn deigmatwn dhl posa louloudia xrisimopoii8ikan
numOfPatterns=d.shape[0]
print "NumberOfPatterns: ",d.shape[0]
#dhmiourgia mia sthlhs me asous gia ton x
xOnes=np.ones([numOfPatterns,1])
#dhmiourgia prwtipwn toy pinaka x
x=d[:,[0,1,2,3]].astype(np.float64)
#me thn hstack prosthetoume ston x mia sthlh me asous thn xOnes
x=np.hstack((x,xOnes))
#print "X epau3imeno",x
xplus=np.linalg.pinv(x)


fullData=d[:,[0,1,2,3]].astype(np.float64)
plt.figure(1)
plt.title("Graph For three Classes")
x2=d[0:50,0]
y=d[51:99,0]
z=d[100:150,0]

x1=d[0:50,2]
y1=d[51:99,2]
z1=d[100:150,2]
plt.xlabel("X")
plt.ylabel("Y")
plt.plot(x2,x1,'r*')
plt.plot(y,y1,'ko')
plt.plot(z,z1,'b<')
plt.show

t=np.zeros([numOfPatterns,1])

ans=4
while ans == 4:
    print ("Menu Epilogon")
    print ("1: Diaxorismos Iris-setosa apo Iris-versicolor kai Iris-virginica")
    print ("2: Diaxorismos Iris-virginica apo Iris-setosa kai Iris-versicolor")
    print ("3: Diaxorismos Iris-versicolor apo Iris-setosa kai Iris-virginica")
    epilogi=input("Dwse 1/2/3: ")
    if(epilogi==1):
        print("Epelexes to 1")
        dict_Setosa={"Iris-setosa": 1
                     ,"Iris-versicolor": 0
                     ,"Iris-virginica": 0}
        for pattern in range(0, numOfPatterns):
            if(d[pattern,4] == "Iris-versicolor"):
                t[pattern] = dict_Setosa['Iris-versicolor']
            elif(d[pattern,4] == "Iris-setosa"):
                t[pattern] = dict_Setosa['Iris-setosa']         
            else:
                t[pattern] = dict_Setosa['Iris-virginica']

        
    if(epilogi==2):
        print("Epelexes to 2")
        dict_virginica={"Iris-setosa": 0
                         ,"Iris-versicolor": 0
                         ,"Iris-virginica": 1}
        for pattern in range(0, numOfPatterns):
         if(d[pattern,4] == "Iris-versicolor"):
             t[pattern] = dict_virginica['Iris-versicolor']             
         elif(d[pattern,4] == "Iris-setosa"):
             t[pattern] = dict_virginica['Iris-setosa']             
         else:
             t[pattern] = dict_virginica['Iris-virginica']
             
        
    if(epilogi==3):
        print("Epelexes to 3")
        dict_Versicolor={"Iris-setosa": 0
                         ,"Iris-versicolor": 1
                         ,"Iris-virginica": 0}
        for pattern in range(0, numOfPatterns):
         if(d[pattern,4] == "Iris-versicolor"):
             t[pattern] = dict_Versicolor['Iris-versicolor']             
         elif(d[pattern,4] == "Iris-setosa"):
             t[pattern] = dict_Versicolor['Iris-setosa']             
         else:
             t[pattern] = dict_Versicolor['Iris-virginica']  
    #xwrismos protypwn se protipa ekpedeusis kai anaklisis
    setosa=x[0:40,[0,1,2,3]]
    versicolor=x[50:90,[0,1,2,3]]
    virginica=x[100:140,[0,1,2,3]]
    xtrain= np.vstack((setosa,versicolor,virginica)).astype(np.float64)
    
    tSetosa=x[40:50,[0,1,2,3]]
    tVersicolor=x[90:100,[0,1,2,3]]
    tVirginica=x[140:150,[0,1,2,3]]
    xtest=np.vstack((tSetosa,tVersicolor,tVirginica)).astype(np.float64)

    #Dianismata stoxoi ka8e klashs
    targetSetosa=t[0:40,[0]]
    targetVersicolor=t[50:90,[0]]
    targetVirginica=t[100:140,[0]]
    ttrain= np.vstack((targetSetosa,targetVersicolor,targetVirginica))
    
    TtargetSetosa=t[40:50,[0]]
    TtargetVersicolor=t[90:100,[0]]
    TtargetVirginica=t[140:150,[0]]
    ttest=np.vstack((TtargetSetosa,TtargetVersicolor,TtargetVirginica))
    
    plt.figure()
    plt.title("Graph Test-Train set")
    x=xtrain[:,0]
    y=xtrain[:,2]
                    
    x1=xtest[:,0]
    y1=xtest[:,2]
                    
    plt.plot(x,y,'b.')
    plt.plot(x1,y1,'r.')
    plt.show  
    
    #ypologismos wT kai yT gia train
    izo=np.ones([120,1])
    xtrainP=np.hstack((xtrain,izo))
    xtrainPlus=np.linalg.pinv(xtrainP)
    
    ttrain1=ttrain*2-1

    #ypologismos wT kai yT gia Test
    #proetimasia gia ton ypologismo
    eo=np.ones([30,1])
    xtestP=np.hstack((xtest,eo))
    xtestPlus=np.linalg.pinv(xtestP)
    ttest1=ttest*2-1
    ttestT=np.transpose(ttest1)
    print "Epelexe anamesa se:\n1.Stochastic Gradient Descent"
    print "2.LBFGS (Limited memory Broyden–Fletcher–Goldfarb–Shanno)"
    print "3.Adam"
    sol=input("")
    solver_dict={ 1:'sgd', 2:'lbfgs', 3:'adam'}
    
    print "Epelexe::\n 1.‘logistic’ -Sigmoidis (0/1)\n2.‘tanh’- uperfovliki efaptomenh (-1/1)"
    acti=input("")
    activation_dict={1:'logistic',2:'tanh'}
    
    hidden_layer=input("Akairea timi gia to plhthos neyronwn sto kryfo strwma: ")
    epoches=input("Dwse ari8mo megistwn epoxwn: ")
    
    mlpclass=MLPClassifier(solver=solver_dict[sol],activation=activation_dict[acti],hidden_layer_sizes=(hidden_layer)
    ,momentum=0.9,max_iter =epoches,learning_rate='constant', learning_rate_init=0.001)
    fitness=mlpclass.fit(xtrain,ttrain)
    predictions=mlpclass.predict(xtrain)
    print "Predictions: ",predictions

    plt.figure(4)
    plt.title('Train-Predict Graph')
   
    plt.plot(ttrain,'bs')
    plt.plot(predictions,'r.')
    plt.show()
    irisData=fullData #iris.data
    irisTarget=t #iris.Targer
    
    #fitness2=mlpclass.fit(xtest,ttest)
    predictions2=mlpclass.predict(xtest)
    
    plt.figure(5)
    plt.title('Test-Predict Graph')
   
    plt.plot(ttest,'bs')
    plt.plot(predictions2,'r.')
    plt.show()
    
    predictTestF=[]
    kkk=1
    lll=1
    for i in range(1, 10):
     X_train, X_test, T_train, T_test = train_test_split(irisData, irisTarget, test_size=0.1)
     #vriskoume to megethos twn pinakwn
     xtrainLen=len(X_train)
     xtestLen=len(X_test)
     ttrainLen=len(T_train)
     ttestLen=len(T_test)
     #metatropi pinakwn T_train T_test apo 0-1 se 1-1
     T_train1=T_train*2-1
     T_test1=T_test*2-1
     fitnessf=mlpclass.fit(X_train,T_train)
     predictionTest=mlpclass.predict(X_test)
     print "FOLD: ",i
     k=i;
     
     p=1
     while(p<7):
         if(p==1):
             criterion="accuracy"
         elif(p==2):
             criterion="precision"
         elif(p==3):
             criterion="recall"
         elif(p==4):
             criterion="fmeasure"
         elif(p==5):
             criterion="sensitivity"
         elif(p==6):
             criterion="specificity"
         global a
         a=evaluate(T_test,predictionTest,criterion)
         
         p=p+1
     print "\n"
     
     plt.subplot(3,3,lll)
     plt.title('Fold Num: {}'.format(lll))
     plt.plot(T_test,'bs')
     plt.plot(predictionTest,'r.')
     plt.tight_layout(pad=0.4, w_pad=0.5, h_pad=1.0)
     #plt.show()
     predictTestF=[]
     lll=lll+1
    ans=0#input("Dwse 4 gia sinexeia: ") 
   
print "Mesoi Oroi: \n"

print "MO Accuracy: ",accuracyAthroisma/9
if(precisionAthroisma/9<=1.0):
 print "MO precisionAthroisma: ",precisionAthroisma/9
else:
 print "MO precisionAthroisma: N/A"
print "MO recallAthroisma: ",recallAthroisma/9
print "MO fmeasureAthroisma: ",fmeasureAthroisma/9
print "MO sensitivityAthroisma: ",sensitivityAthroisma/9
print "MO specificityAthroisma:",specificityAthroisma/9

accuracyAthroisma=0
precisionAthroisma=0
recallAthroisma=0
fmeasureAthroisma=0
sensitivityAthroisma=0
specificityAthroisma=0
print "Telos Programmatos!"
