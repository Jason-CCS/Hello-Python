class CarFleet:

    def solution(self, position, speed, target):
        """
        This approach is from Neetcode
        Sort the car array by position in descending order.
        By counting the time from pos to target,
        we can compare the time in descending order and understand if the current time spending is greater than cur_max,
        we will introduce one more car group.
        For other cases, they will be the same group because the speed of the car behind any latter car is faster than
        the latter car, and they will be the same group.
        Time Complexity: O(n*log(n)) cause sort.
        :param position:
        :param speed:
        :param target:
        :return:
        """
        car_list = sorted(zip(position, speed), reverse=True)
        group, cur_max = 0, float('-inf')
        for pos, sp in car_list:
            time = (target - pos) / sp
            if time > cur_max:
                group += 1
            cur_max = max(cur_max, time)

        return group


if __name__ == '__main__':
    position, speed, target = [10, 8, 0, 5, 3], [2, 4, 1, 1, 3], 12
    print(CarFleet().solution(position, speed, target))
