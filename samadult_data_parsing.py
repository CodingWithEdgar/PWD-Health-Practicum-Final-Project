def read_data(file_path):
    file = open(file_path, "r")
    iterable_file = file.readlines()
    file.close()

    return [line.rstrip("\n").split(",") for line in iterable_file]


def separate_header_and_body(data):
    return data[0], data[1:]


def get_column(header, body, desired_column):
    if str(desired_column) in header:
        return [row[header.index(str(desired_column))] for row in body]
    else:
        # throws an error if the desired_column is not in header
        raise ValueError("desired_column must be an element within the given header")


def get_column_value_breakdown(column_data_no_header):
    result = {}

    for value in column_data_no_header:
        if value not in result.keys():
            result[value] = 0
        else:
            result[value] = result[value] + int(value)

    return result


def get_column_percentage_breakdown(column_value_breakdown):
    total = 0
    result = {}

    for value in column_value_breakdown.values():
        total = total + value

    for key, value in column_value_breakdown.items():
        result[key] = (value/total) * 100

    return result


data = read_data("../samadult.csv")
header, body = separate_header_and_body(data)
print(get_column_percentage_breakdown(get_column_value_breakdown(get_column(header, body, "FPX"))))



