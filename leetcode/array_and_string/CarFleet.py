class CarFleet:
    def solution(self, position, speed, target):
        zip(position, speed)
        # sorted_zip_ary = zip_ary


if __name__ == '__main__':
    position, speed, target = [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 12
    n = len(position)
    car_list = sorted(zip(position, speed), reverse=True)
    # print(car_list)
    cur_max = -1
    group = 0
    for pos, sp in car_list:
        time = (target - pos) / sp
        if time > cur_max:
            group += 1
        cur_max = max(cur_max, time)

    print(group)
