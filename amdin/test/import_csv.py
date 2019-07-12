import csv
date=csv.reader(open('../data_info/info.csv','r'))
for user in date:
	
	username=user[0]
	password=user[1]
	print(username,password)
#读取txt文件
		#user_file=open('login_user_data.txt','r')
		#users=user_file.readlines()
		#user_file.close()
		#for user in users:
		#	username=user.split(',')[0]
		#	password=user.split(',')[1]