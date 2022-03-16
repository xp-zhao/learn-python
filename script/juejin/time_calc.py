import calendar
import datetime


def move_list_left(nums: list, n: int):
    for i in range(n):
        nums.insert(0, nums.pop())

def week_day() -> int:
    current_date = datetime.date.today()
    return calendar.weekday(current_date.year, current_date.month, current_date.day)

def calc_days(target_count: int,
              exist_count: int,
              check_in_days: int,
              check_in_today: bool = True) -> int:
    # 通过签到获取的砖石
    check_in_source = [
        100, 150, 512, 250, 300, 350, 1024, 450, 500, 550, 600, 650, 700, 2048,
        700, 700, 700, 700, 700, 700, 4096, 700, 700, 700, 700, 700, 700, 700,
        700, 5120
    ]
    # 通过海底掘金游戏获取的砖石
    sea_gold_source = [1500, 750, 750, 750, 750, 750, 1500]
    # 数字谜题游戏每周能获取的砖石
    shuzi_source_week = 5200
    # 当天是星期几
    day = week_day()
    if check_in_today:
        move_list_left(sea_gold_source, day)
        check_in_days += 1
    else:
        move_list_left(sea_gold_source, day - 1)
    # 记录获取的砖石数
    count = 0
    # 记录需要的天数
    total_day = 0
    # 还需要获取的砖石数量
    need_count = target_count - exist_count
    while count < need_count:
        count += check_in_source[(total_day + check_in_days) % 30]
        count += sea_gold_source[total_day % 7]
        if total_day % 7 == 0:
            count += shuzi_source_week
        total_day += 1
    return total_day


if __name__ == '__main__':
    print(calc_days(4900000, 136620, 83))
