import csv

def get_data():
    filename = "data.csv"
    with open(filename, 'r') as f:
        data=[(int(line["km"]),int(line["price"])) for line in  csv.DictReader(f)]
    return data

def get_thetas():
    try:
        with open("thetas_file", 'r') as f:
            values = f.readline()
            theta_0, theta_1 = values.split(',')
    except Exception as e:
        print("message: {}".format(e))
        theta_0, theta_1 = 0.0, 0.0
    return [float(theta_0), float(theta_1)]

def save_thetas(theta_0, theta_1):
    try:
        with open("thetas_file", 'w') as thetas_file:
            thetas_file.write('{}, {}'.format(theta_0, theta_1))
    except Exception as e:
        print("An error occur during saving thetas.\n{}".format(e))

def scale(dataset):
    max_data = max(dataset)
    min_data = min(dataset)
    print("max={} min={}".format(max_data, min_data))
    scaleddata = []
    #print("minX: {} maxX:{}".format(min_x, max_x))
    for data in dataset:
        new = [map(data[0], min_data[0], max_data[0], 0, 1), data[1]]
        #print("old: {}\nnew: {}".format(data, new))
        scaleddata.append(new)
    return (scaleddata)

def get_max(dataset):
    max_data = max(dataset)
    return (max_data[0], max_data[1])

def get_min(dataset):
    min_data = min(dataset)
    return (min_data[0], min_data[1])

def map(value, min, max, new_min, new_max):
    return (value - min) / float((max - min)) * (new_max - new_min) + new_min

