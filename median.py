def calculate_median(total_number, data):
    if total_number % 2 == 0:
        median1 = float(data[total_number // 2])
        median2 = float(data[total_number // 2 - 1])

        median = (median1 + median2) / 2
    else:
        median = data[total_number // 2]

    print("median: {}".format(median))

    return median
