# we are going to do linear regression
import numpy as np
import matplotlib.pyplot as plt

def main():
    x = [1, 2, 3, 4, 5]
    y = [1.2, 1.8, 2.6, 3.2, 3.5]
    x_transpose = np.transpose(x)
    y_transpose = np.transpose(y)

    #passing variables to the function
    value_one, value_two = caluculat_func(x, y, x_transpose, y_transpose)

    #passing value to predict plor
    predict_value(value_one, value_two)

    #Passing x and y value for graph
    plot_graph(x, y)


def predict_value(value_one, value_two) -> None:

    a_value = round(value_one, 2)
    b_value = round(value_two, 2)
    coeff = float(input("Enter Coffecient: "))
    predicted_point = a_value + b_value * coeff
    print(f"The predicted value {coeff} is {predicted_point}")

def caluculat_func(x, y, x_transpose, y_transpose) -> float: #This function used to calculate a = ((xT.x)xT)Y using this we wil obtain the function

    #We need to add bais to the x 
    ones = np.ones(len(x))
    x_tranpose_bais = np.vstack([ones, x]).T
    
    #we need to mutiply bais x T and bias x inner fun 
    inverse_fun = np.dot(np.transpose(x_tranpose_bais) , x_tranpose_bais)
    inner_fun = np.linalg.inv(inverse_fun)

    #Let's do outer function a = ((xT.x)xT)Y fiannly complete this function
    outter_fun = np.dot(inner_fun, np.transpose(x_tranpose_bais))
    result = np.dot(outter_fun, y)
    a_zero, a_one = result
    return a_zero, a_one

def plot_graph(x, y) -> None:
    plt.scatter(x, y)
    plt.plot(x, y)
    plt.show()


main()