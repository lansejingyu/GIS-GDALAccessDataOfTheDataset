# -*- coding: utf-8 -*-
# @Project : GIS-GDALAccessDataOfTheDataset
# @File : GDALAccessDataOfTheDataset
# @IDE：PyCharm
# @Author : KT15
# @Time : 2022/10/17 18:18
from osgeo import gdal
import numpy as np
import pandas as pd
import os
import mysql.connector


def ColorOrder():
	# 打开已有的GeoTIF文件
	FilePath = input("输入.TIF文件路径+文件名：")
	dataset = gdal.Open(r'' + FilePath)  # 打开已有的GeoTIF文件 E:\TIF\masaike\K50F038012.tif <1048576

	X = dataset.RasterXSize
	Y = dataset.RasterYSize
	# 读取从第0行第0列开始的3行和3列的图像数据(数组形式返回)。举例：area = band.ReadAsArray(1400, 6000, 6, 3): 读取从第6000行第1400列开始的3行和6列图像数据
	area = dataset.ReadAsArray(0, 0, Y, X)

	if X * Y <= 1048576:
		# 将area的三位数组利用np.reshape()函数转换为二维数组。
		data = np.reshape(area, (-1, X * Y))
		data = pd.DataFrame(data.T)
		# 写入Excel文件
		writer = pd.ExcelWriter(r"E:\GIS-GDALAccessDataOfTheDataset\data.xlsx", )
		data.to_excel(writer, 'page_1', engine='openpyxl', index=False, float_format='%d')
		writer.save()
	elif X * Y > 1048576:
		if (X * Y - 1048576*1) <= 1048576:
			data = np.reshape(area, (-1,1048576))
			# 写入Excel文件
			writer1 = pd.ExcelWriter(r"E:\GIS-GDALAccessDataOfTheDataset\data1.xlsx", )
			data.to_excel(writer1, 'page_1', engine='openpyxl', index=False, float_format='%d')
			writer1.save()

			data = np.reshape(area, (-1, (X * Y - 1048576*1)))
			writer2 = pd.ExcelWriter(r"E:\GIS-GDALAccessDataOfTheDataset\data2.xlsx", )
			data.to_excel(writer2, 'page_1', engine='openpyxl', index=False, float_format='%d')
			writer2.save()
		# data = pd.DataFrame(data.T)  # 将上面的二维数组利用np.T函数转置

		# 将上面的二维数组利用np.T函数转置后保存到txt文本中。
		# np.savetxt(r"E:\GIS-GDALAccessDataOfTheDataset\data.txt", data, fmt='%d')

		# 写入Excel文件
		# writer = pd.ExcelWriter(r"E:\GIS-GDALAccessDataOfTheDataset\data.xlsx", )
		# data.to_excel(writer, 'page_1', engine='openpyxl', index=False, float_format='%d')
		# writer.save()


		# data.to_csv(r"E:\GIS-GDALAccessDataOfTheDataset\data.csv", float_format='%d')# 写入csv文件

	# mydb = mysql.connector.connect(host='localhost', user='root',
	# 							   passwd='Z5708007Hl', database='league_test')
	#
	# mycursor = mydb.cursor()
ColorOrder()
os.system('pause')
