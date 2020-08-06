import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostRegressor
from sklearn import linear_model
def Adaboost(data1):
    data1=data1.reset_index()
    data1['work'] = range(len(data1))
    train_x, test_x, train_y, test_y = train_test_split(data1.work.values.reshape(-1,1),data1.cases, test_size=0.2, random_state=33)
    regressor=AdaBoostRegressor()
    regressor.fit(train_x,train_y)
    pre_y=regressor.predict(test_x)
    y_predic, test_x_predic = predic_data(data1)
    test_x_predic = test_x_predic[-5:]
    y_predic=y_predic[-5:]
    dfy_predic=pd.DataFrame(y_predic,index=None,columns=['data'])
    dfy_predic['datework']=test_x_predic
    dfpre_y=pd.DataFrame(pre_y,index=None,columns=['data'])
    dfpre_y['datework']=test_x
    dfpre_y=pd.concat([dfpre_y,dfy_predic])
    dfpre_y_new=dfpre_y.sort_values(by=['datework'],ascending=True)
    test_y=test_y.values.reshape(-1,1)
    dftest_y=pd.DataFrame(test_y,index=None,columns=['data'])
    dftest_y['datework']=test_x
    dftest_y_new=dftest_y.sort_values(by=['datework'],ascending=True)
    x = dfpre_y_new['datework']
    y = dfpre_y_new['data']
    x1 = dftest_y_new['datework']
    y1 = dftest_y_new['data']
    plt.figure()
    plt.plot(x1,y1,color='r',marker='o')
    plt.plot(x,y,marker='o')
    plt.savefig('pre.png')
    # plt.show()
def predic_data(data1):
    datemore=data1[-1:]
    for i in range (5):
        data1=data1.append(datemore,ignore_index=True)
    data1=data1.reset_index()
    data1['work'] = range(len(data1))
    datechange=(pd.date_range(start='2020-08-01',end='2020-08-05',periods=5)).date
    data1.loc[data1.work>(len(data1)-6),'date']=datechange
    data2=data1[-15:]
    test_x=data2.work.values.reshape(-1,1)
    train_x=data2.work[:len(data2)-5]
    train_x=train_x.values.reshape(-1,1)
    train_y=data2.cases[:len(data2)-5]
    train_x=np.array(train_x)
    train_y=np.array(train_y)
    reg = linear_model.LinearRegression()
    reg.fit(train_x,train_y)
    y_pred=reg.predict(test_x)
    return y_pred,test_x
def fucc(numberid):
    data=pd.read_csv('us-states.csv')

    numberid=int(numberid)
    data1 = data[data.fips == numberid]
    # predic_data(data1)
    Adaboost(data1)
if __name__ == '__main__':

    fucc(2)