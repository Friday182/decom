1 # coding=utf-8
  2 import random
  3 import re
  4 import os
  5 import time
  6 
  7 FOUR_OPERATOR = [' + ',' - ',' * ',' / ']                                   #+-*x����
  8 POWER_OPERATOR = ['��','^2']                                                 #��������ĸ��ź�ƽ��
  9 TRIGONOMETRIC = ['sin','cos','tan']                                         #������������Ǻ���
 10 BRACKET_SIT = [[0,2],[2,4]  ,[4,6],[0,4],[2,6]  ,[0,6],[2,8],[4,8],[6,8]]   #������Ϊ3-5ʱ���ŵ���������������С��3����������
 11 MAXN = 100                                                                  #��������ȡֵ��Χ���ֵ
 12 MINN = 1                                                                    #��������ȡֵ��Χ��Сֵ
 13 OPERATOR_MAX = 5                                                            #���������ȡֵ
 14 USER = ''                                                                   #�û�ID
 15 GRADED = ''                                                                 #�û�ѧ��
 16 QUESTION_NUB = 0                                                            #������Ŀ
 17 targetPath = ''
 18 
 19 def main():
 20     global  targetPath
 21     #log_in()
 22     number_chose()
 23     time_name = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime())        #��ʽ����õ�ǰʱ��
 24     q_set = set()                                                           #���ϱ������ɵ����⣬����ȥ��
 25     history_data = ''                                                       #��ʷ��Ŀ
 26     curPath = os.getcwd()                                                   #��õ�ǰ�ļ�Ŀ¼
 27     targetPath = curPath+os.path.sep+USER                                   #�������Ե�ַ
 28     if not os.path.exists(targetPath):                                      #��������ڣ����½��ļ���
 29         os.makedirs(targetPath)
 30     files = os.listdir(targetPath)                                          #���ļ����������ļ���
 31     for f in files:
 32         txt_path = targetPath + '/' + f
 33         contents = open(txt_path,'r')
 34         history_data +=contents.read()
 35     for i in range(QUESTION_NUB):
 36         q_Temp = ''.join(arithmetic_production())                           #���б�ת��Ϊ�ַ���
 37         q_set.add(q_Temp)                                                   #���뼯��
 38         if len(q_set) == i or (q_Temp in history_data):                     #�ж��Ƿ��ظ����ظ�����������
 39             i -= 1
 40             continue
 41         file_output('[' + str(i+1)+'] ' + q_Temp , time_name)               #д���ļ�
 42 
 43 def log_in():
 44     global USER,GRADED
 45     print('�����û��������룬����֮���ÿո����')
 46     f = open("UserInformation.txt", "r",encoding="utf-8")                   #���û����ݿ�
 47     list = f.read().split('nn')
 48     log_flag = 0                                                            #���ڱ���Ƿ������ݿ���
 49     while 1:
 50         str_user = input().split(' ')
 51         while len(str_user) != 2:
 52             str_user = input('������ȷ�ĸ�ʽ�����û��������룺').split(' ')
 53         in_name = str_user[0]                                               #����ID
 54         in_password = str_user[1]                                           #��������
 55         for i in range(len(list)):                                          #�����û����ݣ��鿴�Ƿ�����û���Ϣ
 56             temp_user = list[i].split('n')
 57             if temp_user[0].lstrip('username:') == in_name:
 58                 if temp_user[1].lstrip('password:') == in_password:
 59                     USER = in_name
 60                     GRADED = temp_user[2].lstrip('grade:')                  #���ѧ����Ϣ
 61                     log_flag = 1
 62         if log_flag == 1:
 63             break
 64         else:
 65             print('�޸��û���Ϣ�����������룺')
 66 
 67 def number_chose():                                                         #������Ŀ��Ŀ���л�ѧ��
 68     while 1:
 69         global GRADED,QUESTION_NUB
 70         in_str = input('׼������{}��ѧ��Ŀ��������������Ŀ����(10-30)��'.format(GRADED))
 71         if re.match(r'd+',in_str) :                                        #�ж�����Ϊ����
 72             question_nub = int(in_str)
 73             if question_nub<10 or question_nub>30:
 74                 print('��Ŀ������Χ����')
 75                 continue
 76             QUESTION_NUB = question_nub
 77             break
 78         matchObj = re.match(r'�л�Ϊ(.*)',in_str)                           #�ж�����Ϊ�л�����
 79         if matchObj and (matchObj.group(1) == 'Сѧ' or matchObj.group(1) == '����' or matchObj.group(1) == '����'):
 80             GRADED = matchObj.group(1)
 81             continue
 82 
 83 def arithmetic_production():                                                #������ѧ��Ŀ
 84     global GRADED
 85     outputDate = []                                                         #������Ŀ��������ֵ
 86     termNub = random.randint(2,OPERATOR_MAX)                                #������������2-5֮�����
 87     bracket_nub = random.randint(0,termNub-2)                               #���Ÿ���������������-2
 88     for i in range(termNub - 1):                                            #���������Ͳ�������������б�
 89         outputDate.append(str(random.randint(MINN, MAXN)))
 90         outputDate.append(FOUR_OPERATOR[random.randint(0,3)])
 91     outputDate.append(str(random.randint(MINN,MAXN)))
 92     outputDate.append(' = ')
 93 
 94     bracket_chose = []                                                      #ѡ��������ŵ�λ��
 95     for i in range(bracket_nub):
 96         temp_sit = BRACKET_SIT[random.randint(0,int(termNub*float((termNub-1)/2))-2)]   #����ѡ������������֮������ۼӹ�ϵ
 97         bracket_flag = 1                                                    #��������Ƿ񽻲�
 98         for j in bracket_chose:                                             #�����ж�
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
111     if GRADED == '����':
112         last_flag = 0                                                       #����Ƿ��Ѿ�������ź�ƽ��
113         for i in range(len(outputDate)):
114             if i%2==0 and random.randint(0,1)==1:
115                 if random.randint(0,1) == 0:
116                     outputDate[i] = POWER_OPERATOR[0] +outputDate[i]    #�������
117                 else:
118                     outputDate[i] = outputDate[i]  + POWER_OPERATOR[1]    #����ƽ��
119                 last_flag = 1
120         if last_flag ==0:
121             outputDate[-2] = outputDate[-2] + POWER_OPERATOR[1]
122     if GRADED == '����':
123         last_flag = 0                                                       #����Ƿ��Ѿ��������Ǻ���
124         T_chose = random.randint(0, 2)
125         for i in range(len(outputDate)):
126             if i%2==0 and random.randint(0,1)==1:
127                 outputDate[i] = TRIGONOMETRIC[T_chose] + '(' +outputDate[i] + ')'   #�������Ǻ���
128                 last_flag = 1
129         if last_flag ==0:
130             outputDate[-2] = TRIGONOMETRIC[T_chose] + '(' + outputDate[-2] + ')'
131 
132     return outputDate                                                       #�����ַ����б�
133 
134 def file_output(Equation,tName):                                            #�ļ����
135     f = open(targetPath + '/' + tName +'.txt','a')                          #��������ڣ��½�txt���⣬��׷��д��
136     f.write(Equation+'nn')
137 
138 if __name__=="__main__":
139     main()