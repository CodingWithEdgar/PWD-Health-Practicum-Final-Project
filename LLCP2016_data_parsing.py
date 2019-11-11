def read_data(file_path):
    """
    Read a data file and return a list of dictionaries, where each
    dictionary has incrementing keys and data (for each row)

    Input: string name of the file_path
    Outut: a list of dictionaries, with one dictionary for each
            row of data, where the keys come from the file header,
            and each row of data is data about suicides for one country
    """
    file = open(file_path, "r")
    iterable_file = file.readlines()
    file.close()
    result = {}
    counter = 0
    for line in iterable_file:
        result[counter] = line.strip().rstrip("\n")
        counter = counter + 1

    return result


def get_column(dictionary, column):
    """Retrieves the column of the data and compiles that into a new dictionary mapped by the keys of
    the original data"""
    column_data = {}
    for key, value in dictionary.items():
        temp_column = value[column - 1]  # grabs the value at the intended column with 0 index taken into account
        column_data[key] = temp_column
    return column_data


def get_value_breakdown(dictionary):
    """Gets the value representation of a column of data
    input: dictionary representation of a single column of data
    output: dictionary representation of the value breakdown of that column of data"""
    value_counter = {}
    for key, value in dictionary.items():
        if value not in value_counter.keys():
            value_counter[value] = 0
        else:
            value_counter[value] = value_counter[value] + 1

    return value_counter


def get_percentage_breakdown(dictionary):
    percentages = {}
    total = 0
    for value in dictionary.values():
        total = total + value

    for key,value in dictionary.items():
        percentages[key] = (value/total) * 100

    return percentages


data = read_data("LLCP2016.asc")
chronic_column = get_column(data, 111)
print(get_value_breakdown(chronic_column))
print(get_percentage_breakdown(get_value_breakdown(chronic_column)))
