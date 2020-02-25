1 # coding=utf-8
  2 import random
  3 import re
  4 import os
  5 import time
  6 
  7 FOUR_OPERATOR = [' + ',' - ',' * ',' / ']                                   #+-*x符号
  8 POWER_OPERATOR = ['√','^2']                                                 #初中运算的根号和平方
  9 TRIGONOMETRIC = ['sin','cos','tan']                                         #高中运算的三角函数
 10 BRACKET_SIT = [[0,2],[2,4]  ,[4,6],[0,4],[2,6]  ,[0,6],[2,8],[4,8],[6,8]]   #操作数为3-5时括号的组合情况，操作数小于3括号无意义
 11 MAXN = 100                                                                  #操作数的取值范围最大值
 12 MINN = 1                                                                    #操作数的取值范围最小值
 13 OPERATOR_MAX = 5                                                            #操作符最大取值
 14 USER = ''                                                                   #用户ID
 15 GRADED = ''                                                                 #用户学历
 16 QUESTION_NUB = 0                                                            #问题数目
 17 targetPath = ''
 18 
 19 def main():
 20     global  targetPath
 21     #log_in()
 22     number_chose()
 23     time_name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())        #格式化获得当前时间
 24     q_set = set()                                                           #集合保存生成的问题，用于去重
 25     history_data = ''                                                       #历史题目
 26     curPath = os.getcwd()                                                   #获得当前文件目录
 27     targetPath = curPath+os.path.sep+USER                                   #构建绝对地址
 28     if not os.path.exists(targetPath):                                      #如果不存在，则新建文件夹
 29         os.makedirs(targetPath)
 30     files = os.listdir(targetPath)                                          #该文件夹下所有文件名
 31     for f in files:
 32         txt_path = targetPath + '/' + f
 33         contents = open(txt_path,'r')
 34         history_data +=contents.read()
 35     for i in range(QUESTION_NUB):
 36         q_Temp = ''.join(arithmetic_production())                           #将列表转换为字符串
 37         q_set.add(q_Temp)                                                   #加入集合
 38         if len(q_set) == i or (q_Temp in history_data):                     #判定是否重复，重复则重新生成
 39             i -= 1
 40             continue
 41         file_output('[' + str(i+1)+'] ' + q_Temp , time_name)               #写入文件
 42 
 43 def log_in():
 44     global USER,GRADED
 45     print('输入用户名和密码，两者之间用空格隔开')
 46     f = open("UserInformation.txt", "r",encoding="utf-8")                   #打开用户数据库
 47     list = f.read().split('nn')
 48     log_flag = 0                                                            #用于标记是否在数据库内
 49     while 1:
 50         str_user = input().split(' ')
 51         while len(str_user) != 2:
 52             str_user = input('请用正确的格式输入用户名和密码：').split(' ')
 53         in_name = str_user[0]                                               #输入ID
 54         in_password = str_user[1]                                           #输入密码
 55         for i in range(len(list)):                                          #遍历用户数据，查看是否存在用户信息
 56             temp_user = list[i].split('n')
 57             if temp_user[0].lstrip('username:') == in_name:
 58                 if temp_user[1].lstrip('password:') == in_password:
 59                     USER = in_name
 60                     GRADED = temp_user[2].lstrip('grade:')                  #获得学历信息
 61                     log_flag = 1
 62         if log_flag == 1:
 63             break
 64         else:
 65             print('无该用户信息，请重新输入：')
 66 
 67 def number_chose():                                                         #生成题目数目或切换学历
 68     while 1:
 69         global GRADED,QUESTION_NUB
 70         in_str = input('准备生成{}数学题目，请输入生成题目数量(10-30)：'.format(GRADED))
 71         if re.match(r'd+',in_str) :                                        #判断输入为数字
 72             question_nub = int(in_str)
 73             if question_nub<10 or question_nub>30:
 74                 print('题目数量范围错误！')
 75                 continue
 76             QUESTION_NUB = question_nub
 77             break
 78         matchObj = re.match(r'切换为(.*)',in_str)                           #判断输入为切换命令
 79         if matchObj and (matchObj.group(1) == '小学' or matchObj.group(1) == '初中' or matchObj.group(1) == '高中'):
 80             GRADED = matchObj.group(1)
 81             continue
 82 
 83 def arithmetic_production():                                                #产生数学题目
 84     global GRADED
 85     outputDate = []                                                         #保存题目，做返回值
 86     termNub = random.randint(2,OPERATOR_MAX)                                #操作数个数，2-5之间随机
 87     bracket_nub = random.randint(0,termNub-2)                               #括号个数，操作数个数-2
 88     for i in range(termNub - 1):                                            #将操作数和操作符随机加入列表
 89         outputDate.append(str(random.randint(MINN, MAXN)))
 90         outputDate.append(FOUR_OPERATOR[random.randint(0,3)])
 91     outputDate.append(str(random.randint(MINN,MAXN)))
 92     outputDate.append(' = ')
 93 
 94     bracket_chose = []                                                      #选择加入括号的位置
 95     for i in range(bracket_nub):
 96         temp_sit = BRACKET_SIT[random.randint(0,int(termNub*float((termNub-1)/2))-2)]   #括号选择情况与操作数之间存在累加关系
 97         bracket_flag = 1                                                    #标记括号是否交叉
 98         for j in bracket_chose:                                             #交叉判定
 99             if j[1]>=temp_sit[0] and j[0]<temp_sit[0] and j[1]<temp_sit[1] or 
100                     j[0]<=temp_sit[1] and j[1]>temp_sit[1] and j[0]>temp_sit[0] or
101                     j[0] == temp_sit[0] and j[1] ==temp_sit[1]:
102                 bracket_flag = 0
103         if bracket_flag:
104             bracket_chose.append(temp_sit)
105         else:
106             i -= 1
107     for i in bracket_chose:
108         outputDate[i[0]] = '(' + outputDate[i[0]]
109         outputDate[i[1]] += ')'
110 
111     if GRADED == '初中':
112         last_flag = 0                                                       #标记是否已经加入根号和平方
113         for i in range(len(outputDate)):
114             if i%2==0 and random.randint(0,1)==1:
115                 if random.randint(0,1) == 0:
116                     outputDate[i] = POWER_OPERATOR[0] +outputDate[i]    #加入根号
117                 else:
118                     outputDate[i] = outputDate[i]  + POWER_OPERATOR[1]    #加入平方
119                 last_flag = 1
120         if last_flag ==0:
121             outputDate[-2] = outputDate[-2] + POWER_OPERATOR[1]
122     if GRADED == '高中':
123         last_flag = 0                                                       #标记是否已经加入三角函数
124         T_chose = random.randint(0, 2)
125         for i in range(len(outputDate)):
126             if i%2==0 and random.randint(0,1)==1:
127                 outputDate[i] = TRIGONOMETRIC[T_chose] + '(' +outputDate[i] + ')'   #加入三角函数
128                 last_flag = 1
129         if last_flag ==0:
130             outputDate[-2] = TRIGONOMETRIC[T_chose] + '(' + outputDate[-2] + ')'
131 
132     return outputDate                                                       #返回字符串列表
133 
134 def file_output(Equation,tName):                                            #文件输出
135     f = open(targetPath + '/' + tName +'.txt','a')                          #如果不存在，新建txt问题，且追加写入
136     f.write(Equation+'nn')
137 
138 if __name__=="__main__":
139     main()