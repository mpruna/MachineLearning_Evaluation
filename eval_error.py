#!/home/anaconda3/envs/py37_covidenv/bin/python
import numpy as np


#Mean Absolute Error
def mae(predict, actual):

    '''
    predict = np.array(predict)
    actual = np.array(actual)
    '''

    difference = abs(predict - actual)
    score = difference.mean()

    return score

#Mean Squared Error
def mse(predict, actual):
    '''
    predict = np.array(predict)
    actual = np.array(actual)
    '''

    difference = predict - actual
    square_diff = np.square(difference)

    score = square_diff.mean()
    return score

#Root Mean Squared Error
def rmse(predict, actual):
    '''
    predict = np.array(predict)
    actual = np.array(actual)
    '''

    difference = predict - actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()
    score = np.sqrt(mean_square_diff)
    return score

#Root Mean Square Logarithmic Error
def rmsle(predict, actual):
    '''
    predict = np.array(predict)
    actual = np.array(actual)
    '''

    log_predict = np.log(predict+1)
    log_actual = np.log(actual+1)

    difference = log_predict - log_actual
    square_diff = np.square(difference)
    mean_square_diff = square_diff.mean()

    score = np.sqrt(mean_square_diff)

    return score

#Mean Bias Deviation
def mbd(predict, actual):
    '''
    predict = np.array(predict)
    actual = np.array(actual)
    '''
    difference = predict - actual
    numerator = np.sum(difference) / len(predict) 
    denumerator =  np.sum(actual) / len(predict)
    print(numerator)
    print(denumerator)

    score = float(numerator) / denumerator * 100

    return score

x = np.linspace(0, 100, 50)
y = 2*x + 1

noise = np.random.normal(0, 7, y.shape)
y_2 = y + noise

mae=mae(predict=y, actual=y_2)
print("MAE error {}".format(mae))

mse=mse(predict=y, actual=y_2)
print("MSE error {}".format(mse))

rmse=rmse(predict=y, actual=y_2)
print("RMSE error {}".format(rmse))

rmsle=rmsle(predict=y, actual=y_2)
print("RMSLE error {}".format(rmsle))

mbd=mbd(predict=y, actual=y_2)
print("MBD error {}".format(mbd))