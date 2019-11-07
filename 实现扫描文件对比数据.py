import xlrd
import xlwt
import os
import os.path

class RWfile(object):
	def __init__(self, srcPath, inputExcel, outputExcel):
		self.srcPath = srcPath or os.getcwd()  #  srcPath：需要扫描的项目地址  若无则扫描工具所在根目录下的所有文件
		self.inputExcel = inputExcel	# inputExcel： 读取的文件绝对地址
		self.outputExcel = outputExcel or (os.getcwd() + '\\导出.xlsx')  # outputExcel：写入的文件的绝对地址  若无则默认存放在该文件的根目录下
		self.__excel_list = []
		self.__data_list = []


	# 扫描目录下所有vue或js文件的地址  递归扫描
	def find_dir(self, dir_name):
		for path_name, dir_list, files_name in os.walk(dir_name):
			for file in files_name:
				file_content = ''
				fileType = os.path.splitext(file)[1][1:]
				if fileType in ['txt', 'vue', 'js', 'm', 'h', 'java', 'xml', 'gitignore']:
				    with open(path_name+'/'+file, 'r', encoding='UTF-8') as f:
				        for line in f:
				            file_content += line
				        for i in range(0, len(self.__excel_list)):
				            if self.__excel_list[i] in file_content and self.__excel_list[i] not in self.__data_list:
				                self.__data_list.append(self.__excel_list[i])
			for dir_name in dir_list:
				self.find_dir(path_name+'/'+dir_name)


	# 将对比出来的数据存放进新的Excel
	def writeData(self):
		# 文件已存在则删除新建
		if os.path.exists(self.outputExcel):
			os.remove(self.outputExcel)
		xls = xlwt.Workbook()
		sht = xls.add_sheet('数据校验', cell_overwrite_ok=True)
		for i in range(0, len(self.__data_list)):
			sht.write(i, 0, self.__data_list[i])
		xls.save(self.outputExcel)

	# 获取要查找的数据list 读Excel
	def read_excel(self):
		fileType = os.path.splitext(self.inputExcel)[1][1:]
		if fileType == 'txt':
			for line in open(self.inputExcel, 'r', 'UTF-8'):
				self.__excel_list.append(line)
		elif fileType in ['xlsx', 'xls']:
		    wb = xlrd.open_workbook(self.inputExcel)
		    sheet = wb.sheet_by_index(0) #根据索引来获取sheet
		    rows = sheet.nrows  #获取已有的行数
		    cols = sheet.ncols  #获取已有的列数
		    # 获取第一列的数据
		    for item in sheet.col_values(0):
			    self.__excel_list.append(item.split(' ')[0])
		else:
			print('暂不支持' + fileType + '格式')
		print('指定要查找的数据 >>>>> %s'% self.__excel_list)
		self.find_dir(self.srcPath)
		self.writeData()


# 执行程序
# from test1 import RWfile
proPath = input('请输入项目路径，默认'+os.getcwd()+'：');
inp = input('请输入对比数据的完整路径：'); # D:/Candy/testExcel.xlsx
oup = input('请输入导出文件的完整路径，默认'+ os.getcwd()+'\\导出.xlsx：'); # D:/Candy/导出.xlsx
a=RWfile(proPath, inp, oup);
a.read_excel();
outPath = oup or os.getcwd()+'\\导出.xlsx';
print('导出完毕，请在：'+ outPath +'目录下查看')

# 目前只支持vue/js/java/m结尾的文件，其他文件可能存在编码格式问题
# 尝试打开doc/docx/xls/xlsx/txt/h/a
