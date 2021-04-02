import sys
import matplotlib.pyplot as plt
from ft_linear_regression import estimate_price
from tools import get_data
from tools import get_thetas
from tools import scale
from tools import map

def display(estimated_price, mileage):
    thetas = get_thetas()
    data = get_data()
    theta_0 = thetas[0]
    theta_1 = thetas[1]
    max_data = max(data)
    min_data = min(data)
    for d in data:
        plt.plot(d[0], d[1], "ob")
    plt.plot([max_data[0], min_data[0]], \
        [estimate_price(theta_0, theta_1, max_data[0]), \
            estimate_price(theta_0, theta_1, min_data[0])], '-r')
    plt.plot(mileage, estimated_price, "og")
    plt.xlabel("km")
    plt.ylabel("price")
    plt.suptitle("cloud points price/km")
    plt.show()

def main():
    theta_0 = 0.
    theta_1 = 0.
    mileage = input("Please enter a mileage: ")
    try:
        mileage = float(mileage)
        thetas = get_thetas()
        theta_0 = thetas[0]
        theta_1 = thetas[1]
        estimated_price = estimate_price(float(theta_0), float(theta_1), mileage)
        print("Estimate price : {:.2f}".format(estimated_price))
        return estimated_price, mileage
    except ValueError as e:
        print(e)
        print("error: Please enter a number.")
        main()

if __name__ == "__main__":
    values = main()
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        display(values[0], values[1])

