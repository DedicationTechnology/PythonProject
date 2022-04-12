# 数据预处理之：均值移除示例

# import numpy as np
# import sklearn.preprocessing as sp

# 样本数据
# raw_samples = np.array([  # array表示生成一个数组
#     [3.0, -1.0, 2.0],
#     [0.0, 4.0, 3.0],
#     [1.0, -4.0, 2.0]
# ])
#"""方法1:自己写代码实现标准化"""
# print(raw_samples)
# print(raw_samples.mean(axis=0))  # 求每列的平均值
# print(raw_samples.std(axis=0))  # 求每列标准差
# std_samples = raw_samples.copy()  # 复制样本数据(复制一个数组)
# 实现标准化
# for col in std_samples.T:  # 遍历每列
#     col_mean = col.mean()  # 计算平均数
#     col_std = col.std()  # 求标准差
#     col -= col_mean  # 减平均值
#     col /= col_std  # 除标准差
#
# print(std_samples)
# print(std_samples.mean(axis=0))
# print(std_samples.std(axis=0))

# """方法2:通过sklearn提供的API实现标准化"""
# std_samples = sp.scale(raw_samples) # 实现标准化
# print(std_samples)
# print(std_samples.mean(axis=0))
# print(std_samples.std(axis=0))


# 数据预处理之：范围缩放

# import numpy as np
# import sklearn.preprocessing as sp
#
# # 样本数据
# raw_samples = np.array([
#     [1.0, 2.0, 3.0],
#     [4.0, 5.0, 6.0],
#     [7.0, 8.0, 9.0]]).astype("float64")
#
# # print(raw_samples)
# mms_samples = raw_samples.copy()  # 复制样本数据
#
# # """方法1:自己写代码实现范围缩放"""
# # for col in mms_samples.T:
# #     col_min = col.min()
# #     col_max = col.max()
# #     col -= col_min
# #     col /= (col_max - col_min)
# # print(mms_samples)
# # 我们也可以通过sklearn提供的对象实现同样的功能，如下面代码所示：
#
# """方法2:我们也可以通过sklearn提供的对象实现同样的功能"""
# # 根据给定范围创建一个范围缩放器对象
# mms = sp.MinMaxScaler(feature_range=(0, 1))# 定义对象(修改范围观察现象),这里表示最小值缩放到0最大值缩放到1
# # 使用范围缩放器实现特征值范围缩放
# mms_samples = mms.fit_transform(raw_samples) # 缩放
# print(mms_samples)


# 线性回归示例
"""方法1:自己编码实现"""
# import numpy as np
# import matplotlib.pyplot as mp  # 绘图
# from mpl_toolkits.mplot3d import axes3d  # 绘3D图
# import sklearn.preprocessing as sp
#
# # 训练数据集
# train_x = np.array([0.5, 0.6, 0.8, 1.1, 1.4])  # 输入集
# train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])  # 输出集
# # 当x为0.5时y为5.0,依此类推
# n_epochs = 1000  # 迭代次数
# lrate = 0.01  # 学习率【控制梯度下降的幅度】
# epochs = []  # 记录迭代次数
# losses = []  # 记录损失值
#
# w0, w1 = [1], [1]  # 定义线性模型的参数以及模型初始值
#
# for i in range(1, n_epochs + 1):  # 循环1000次
#     epochs.append(i)  # 记录第几次迭代
#     # 通过线性模型计算(计算结果即为预测值)，计算y=wx+b(wb就是w0和w1)
#     y = w0[-1] + w1[-1] * train_x  # 取出最新的w0,w1计算线性方程输出
#     # 损失函数(均方差)，就是切线的斜率，越趋于0表示越准确
#     loss = (((train_y - y) ** 2).sum()) / 2  # 真实值与预测值的平方求和除以2为损失函数
#     losses.append(loss)  # 记录每次迭代的损失值
#
#     # print("%d: w0=%f, w1=%f, loss=%f" % (i, w0[-1], w1[-1], loss))
#
#     # 计算w0,w1的偏导数(梯度)
#     d0 = -(train_y - y).sum()  # w0的梯度
#     d1 = -(train_x * (train_y - y)).sum()  # w1的梯度
#
#     # 更新w0,w1
#     w0.append(w0[-1] - (d0 * lrate))
#     w1.append(w1[-1] - (d1 * lrate))

# 训练过程可视化
## 损失函数收敛过程
# w0 = np.array(w0[1:])  # 去掉初始的自定义值，保证一共有1000个值
# w1 = np.array(w1[1:])
#
# mp.figure("Losses", facecolor="lightgray")  # 创建一个窗体,名为Losses
# mp.title("epoch", fontsize=20)  # 图形标题
# mp.ylabel("loss", fontsize=14)  # y轴名称为loss
# mp.grid(linestyle=":")  # 网格线：虚线
# mp.plot(epochs, losses, c="blue", label="loss")  # 绘制曲线图：x轴、y轴、曲线颜色、曲线的图例文字
# mp.legend()  # 图例
# mp.tight_layout()  # 紧凑格式
# # mp.show()
#
# ## 显示模型直线
# pred_y = w0[-1] + w1[-1] * train_x  # 根据x预测y
# mp.figure("Linear Regression", facecolor="lightgray")
# mp.title("Linear Regression", fontsize=20)
# mp.xlabel("x", fontsize=14)
# mp.ylabel("y", fontsize=14)
# mp.grid(linestyle=":")
# mp.scatter(train_x, train_y, c="blue", label="Traing")  # 绘制样本散点图
# mp.plot(train_x, pred_y, c="red", label="Regression")
# mp.legend()
# # mp.show()
#
# # 显示梯度下降过程(复制粘贴即可，不需要编写)
# # 计算损失函数曲面上的点 loss = f(w0, w1)
# arr1 = np.linspace(0, 10, 500)  # 0~9间产生500个元素的均匀列表
# arr2 = np.linspace(0, 3.5, 500)  # 0~3.5间产生500个元素的均匀列表
#
# grid_w0, grid_w1 = np.meshgrid(arr1, arr2)  # 产生二维矩阵
#
# flat_w0, flat_w1 = grid_w0.ravel(), grid_w1.ravel()  # 二维矩阵扁平化
# loss_metrix = train_y.reshape(-1, 1)  # 生成误差矩阵（-1,1）表示自动计算维度
# outer = np.outer(train_x, flat_w1)  # 求外积（train_x和flat_w1元素两两相乘的新矩阵）
# # 计算损失：((w0 + w1*x - y)**2)/2
# flat_loss = (((flat_w0 + outer - loss_metrix) ** 2).sum(axis=0)) / 2
# grid_loss = flat_loss.reshape(grid_w0.shape)
#
# mp.figure('Loss Function')
# ax = mp.gca(projection='3d')
# mp.title('Loss Function', fontsize=14)
# ax.set_xlabel('w0', fontsize=14)
# ax.set_ylabel('w1', fontsize=14)
# ax.set_zlabel('loss', fontsize=14)
# ax.plot_surface(grid_w0, grid_w1, grid_loss, rstride=10, cstride=10, cmap='jet')
# ax.plot(w0, w1, losses, 'o-', c='orangered', label='BGD', zorder=5)
# mp.legend(loc='lower left')
#
# mp.show()

# 方法2:通过sklearn API实现,利用LinearRegression实现线性回归
# import numpy as np
# import sklearn.linear_model as lm  # 线性模型
# import sklearn.metrics as sm  # 模型性能评价模块
# import matplotlib.pyplot as mp
#
# train_x = np.array([[0.5],
#                     [0.6],
#                     [0.8],
#                     [1.1],
#                     [1.4]])  # 输入集
# train_y = np.array([5.0, 5.5, 6.0, 6.8, 7.0])  # 输出集
#
# # 创建线性回归器
# model = lm.LinearRegression()
# # 用已知输入、输出数据集训练回归器
# model.fit(train_x, train_y)
# # 根据训练模型预测输出
# pred_y = model.predict(train_x)
#
# print("coef_:", model.coef_)  # 系数
# print("intercept_:", model.intercept_)  # 截距
#
# # 可视化回归曲线
# mp.figure('Linear Regression', facecolor='lightgray')
# mp.title('Linear Regression', fontsize=20)
# mp.xlabel('x', fontsize=14)
# mp.ylabel('y', fontsize=14)
# mp.tick_params(labelsize=10)
# mp.grid(linestyle=':')
#
# # 绘制样本点
# mp.scatter(train_x, train_y, c='blue', alpha=0.8, s=60, label='Sample')
#
# # 绘制拟合直线
# mp.plot(train_x,  # x坐标数据
#         pred_y,  # y坐标数据
#         c='orangered', label='Regression')
#
# mp.legend()
# mp.show()
