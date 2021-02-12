import numpy as np

def data_load_to_array(file):
    """Reads in the data from csv file and stores it in an array."""
    with open(file, "r") as data_str:
        data_list = []
        for i in data_str:
            list_str = i.split("\n")
            del list_str[-1]
            data_list.append(list_str)
    
    data_array = []
    for line in data_list:
        data_array.append(np.array(line[0].split(",")))
    data_array = np.array(data_array)
    header = data_array[0]
    array_data_set = data_array[1:]
    array_data_set = array_data_set.reshape((len(array_data_set), len(header)))

    return array_data_set

def main():
	"""Main function for executing each of the functions with corresponding parameters."""
	file_acc = "road_safety_data_accidents_2019.csv"
	accidents_2019_data = data_load_to_array(file_acc)
	file_cas = "road_safety_data_casualties_2019.csv"
	# casualties_2019_data = data_load_to_array(file_cas)
	file_veh = "road_safety_data_vehicles_2019.csv"
	# vehicles_2019_data = data_load_to_array(file_veh)

if __name__ == "__main__":
	main()
