"""
	###########################################################################
	#		                                                                  #
	#		Project: Dynamic programming                                      #
	#		                                                                  #
	#		Filename: yep.py                                                  #
	#		                                                                  #
	#		Programmer: Vincent Holmes                                        #
	#		                                                                  #
	#		Description: 动态规划算法,优化为两步长                            #
	#		                                                                  #
	#		Start_date: 2020-07-25                                            #
	#		                                                                  #
	#		Last_update: 2020-07-25                                           #
	#		                                                                  #
	###########################################################################
"""


import numpy as np
import matplotlib.pyplot as plt
from matplotlib.pyplot import MultipleLocator


def plot2d(x_lst, y_lst, title=None):

    """
    
    这是一个二维的画图器。
    
    Args:
        x_lst是一个包含了所有要画的取线的x矩阵的列表。如要画3条线就有3个矩阵;
        y_lst是一个包含了所有要画的取线的y矩阵的列表。如要画3条线就有3个矩阵;
        title是整个图的标题，默认为无
        
    Returns:
        不返回值，会绘制一个图表并显示出来
    """
    
    line_lst = []
    
    plt.figure("2D")       # 创建一个名字叫2D的图表
    for x, y in zip(x_lst, y_lst):
        line, = plt.plot(x, y, 'g-.', marker='^', markersize=10)
        line_lst.append(line)
    plt.legend(line_lst, bbox_to_anchor=(0.3, 1), loc='lower right' )
    
    # 设置范围
    ax=plt.gca() # ax为两轴的实例
    ax.yaxis.set_major_locator(MultipleLocator(1))
    ax.xaxis.set_major_locator(MultipleLocator(1))
    
    # 显示网格线(alpha是透明度)
    plt.grid(linestyle="--", alpha=0.5)
    
    # 添加标题
    if title != None:
        plt.title(title)
    
    # 显示图层
    plt.show()
    
    
class Min:
    """
    Parameter:
        ary: an array
    """
    def __init__(self, ary):
        self.ary = ary
        self.path = [[0,0]]
        self.x_lst = []
        self.y_lst = []
        
        
    def min(self):
        """
        Function:
            to find and return the mini-sum of the path
        """
        for i in range(round(sum(self.ary.shape)/2-1)):
            try:
                x, y = self.jump()
                self.path.append(x)
                self.path.append(y)
            except:
                x = self.jump()
                self.path.append(x)
        final_path = []
        [final_path.append(item) for item in self.path if item not in final_path]
        print("The final path is: %s"%(final_path))
        f_sum = 0
        for i in final_path:
            f_sum += self.ary[i[0]][i[1]]
            self.x_lst.append(i[1]+1)
            self.y_lst.append(-i[0]-1)
        
        return f_sum, self.x_lst, self.y_lst
        
    def jump(self):
        f_step = self.posit(self.path[-1])
        sec_step = {}
        for n in f_step:
            sec_step[str(n)] = self.posit(n)
        
        # initialize the path chosing
        sum = -1
        mini = [[-1, -1]]
        for x in f_step:
            for y in sec_step[str(x)]:
                try:
                    # print("%s %s"%(x, y))
                    # print(self.ary[x, y])
                    tem_sum = self.ary[x[0]][x[1]] + self.ary[y[0]][y[1]]
                    if sum == -1:
                        sum = tem_sum
                        mini = [x, y]
                    elif sum > tem_sum:
                        sum = tem_sum
                        mini = [x, y]
                except:
                    pass
        # print(mini)
        if mini != [[-1, -1]]:
            return mini[0], mini[1]
        else:
            return [-1, -1], [-1, -1]
        
        
    def posit(self, p):
        """
        Parameter:
            p: an index to show the position
        
        Functiom:
            to return the possible position
        """
        return [[p[0]+1, p[1]],[p[0], p[1]+1]]

if __name__ == "__main__":
    # initialize
    rand = np.random.randint(1, 10, (7,5))
    m = Min(rand)

    # show the array
    print(" This is the original array ".center(80, '*'))
    print(rand)

    # show the result
    mini_sum, x, y = m.min()
    print(" This is the result ".center(80, "*"))
    print("\nThe smallest sum: %s"%(mini_sum))
    plot2d([x], [y])