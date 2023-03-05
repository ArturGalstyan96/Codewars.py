def better_than_average(class_points, your_points):
    if sum(class_points) < your_points * len(class_points):
        return True
    return False