import matplotlib.pyplot as plt

def main():
    # x 轴数据列表
    x_values = [x for x in range(1, 11)]
    # y 轴数据列表
    y_values = [x ** 2 for x in range(1, 11)]
    # 设置图表标题以及 x、y 轴的说明
    plt.title('Square Numbers')
    plt.xlabel('Value', fontsize=18)
    plt.ylabel('Square', fontsize=18)
    # 设置刻度标记的文字大小
    plt.tick_params(axis='both', labelsize=16)
    # 绘制折线图
    plt.plot(x_values, y_values)
    plt.show()
    

if __name__ == "__main__":
    main()