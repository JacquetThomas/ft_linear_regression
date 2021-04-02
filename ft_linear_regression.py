import sys
import matplotlib.pyplot as plt
import matplotlib.animation
import tools as t

def estimate_price(theta_0=0.0, theta_1=0.0, km=0):
    return theta_0 + (theta_1 * km)

def train(display=False):
    learning_ratio=0.3
    theta_0 = 0.
    theta_1 = 0.
    data = t.get_data()
    scaleddata = t.scale(data)
    m = len(data)
    if m == 0:
        return
    
   # Draw base graph 
    if display:
        for dat in data:
            plt.plot(dat[0], dat[1], "ob")
        plt.xlabel("km")
        plt.ylabel("price")
        plt.suptitle("cloud points of price/km")
        line, = plt.plot([250000, 100], [estimate_price(theta_0, theta_1, 250000), estimate_price(theta_0, theta_1, 100)], '-r')

    for i in range(m**3):
        sum_0 = 0.
        sum_1 = 0.
        print("i = {} theta_0={} theta_1={}".format(i, theta_0, theta_1))
        max_km, max_price = t.get_max(data)
        min_km, min_price = t.get_min(data)
        for d in scaleddata:
            sum_0 += estimate_price(theta_0, theta_1, d[0]) - d[1]
            sum_1 += (estimate_price(theta_0, theta_1, d[0]) - d[1]) * d[0]
        delta_0 = learning_ratio * (sum_0 / m)
        delta_1 = learning_ratio * (sum_1 / m)
        print("delta_0={} delta_1={}\n".format(delta_0, delta_1))
        theta_0 -= delta_0
        theta_1 -= delta_1

        # Update linear regression line
        if display:
            line.set_ydata([estimate_price(theta_0, theta_1 / max_km, 250000), estimate_price(theta_0, theta_1 / max_km, 100)])
            plt.pause(0.0001)
    theta_1 /= (max_km)
    print("----------------------------\ntheta_0={} theta_1={}".format(theta_0, theta_1))
    t.save_thetas(theta_0, theta_1)
    if display:
        plt.show()

def display_graph():
    
    plt.plot([250000, 100], [estimate_price(theta_0, theta_1, 250000), estimate_price(theta_0, theta_1, 100)], '-r')

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "-s":
        train(True)
    train()