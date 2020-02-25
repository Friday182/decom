# coding=utf-8
import random
import re
import os
import pandas
import decimal
import numpy

FOUR_OPERATOR = [' + ',' - ',' * ',' / ']                                   #+-*x符号
BRACKET_SIT = [[0,2],[2,4]  ,[4,6],[0,4],[2,6]  ,[0,6],[2,8],[4,8],[6,8]]   #操作数为3-5时括号的组合情况，操作数小于3括号无意义
QUESTION_NUB = 200
targetFile = 'math_lesson_mathquestion.csv' 
#fieldnames = ['id', 'level', 'question_type', 'question_text', 'option_1', 'option_2', 'option_3', 'option_4', 'answer', 'lesson_id',]
current_level = 1
lesson_id = 1
offset_grade_1 = [0.1, 0.2]
myfd = pandas.DataFrame()

def main():
    # Build questions
    generate_grade(1)
    generate_grade(7)
    
    myfd.to_csv('math_lesson_mathquestion.csv', sep=',')
    
'''
# For level 1:
# make equation like a.b + c.d =
# a,b,c,d should be 0 to 9, operator only +
# Generate 200 equations
'''
'''
# For grade 2:
# make equation like a.b - c.d =
# a,b,c,d should be 0 to 9, operator only -
# Generate 200 equations
'''

'''
# For grade 3:
# make equation like a.b - c.d =
# a,b,c,d should be 0 to 20, two decimals, operator both + and -
# Generate 200 equations
'''
    
'''
# For grade 4:
# make equation like a.b +- c.d +- e.f =
# a,b,c,d should be 0 to 20, operator both + & -
# Generate 200 equations
'''
'''
# For grade 5:
# make equation like a.b x c.d =
# a,b,c,d should be 0 to 9, operator only x
# Generate 200 equations
'''
'''
# For grade 6:
# make equation like a.b / c.d =
# a,b,c,d should be 0 to 9, operator only /
# Generate 200 equations
'''
'''
# For grade 7:
# make equation like a.b OP c.d =
# a,b,c,d should be 0 to 9, operator for all
# Generate 200 equations
'''
'''
# For grade 8:
# make equation like a.b OP c.d OP e.f =
# a,b,c,d should be 0 to 20, operator all
# Generate 200 equations
'''
'''
# For grade 9:
# make equation like a.b OP c.d OP e.f =
# a,b,c,d should be 0 to 100, operator all with bracket
# Generate 200 equations
'''
def generate_grade(current_grade):
    global myfd
    index = 0
    equation = []
    option = [0.1, 0.1, 0.1, 0.1]
    
    for i in range(QUESTION_NUB-1):
        if current_grade == 1:
            a = decimal.Decimal(random.randrange(0, 100))/10
            b = decimal.Decimal(random.randrange(0, 100))/10
            if "." not in str(a) and "." not in str(b):
                continue
            equation = str(a) + ' + ' + str(b)
            answer = decimal.Decimal(eval(equation))
            equation = equation + ' = '
        elif current_grade == 2:
            pass
        elif current_grade == 3:
            pass
        elif current_grade == 4:
            pass
        elif current_grade == 5:
            pass
        elif current_grade == 6:
            pass
        elif current_grade == 7:
            a = decimal.Decimal(random.randrange(0, 100))/10
            b = decimal.Decimal(random.randrange(0, 100))/10
            if "." not in str(a) and "." not in str(b):
                continue
            if b == 0: continue
            
            equation = str(a) + FOUR_OPERATOR[random.randint(0,3)] + str(b)
            answer = decimal.Decimal(round(eval(equation),2))
            equation = equation + ' = '
            if answer < 0.1: continue
            
        elif current_grade == 8:
            pass
        elif current_grade == 9:
            pass
        # Set options
        option1 = decimal.Decimal(0.1)
        option2 = decimal.Decimal(0.1)
        option3 = decimal.Decimal(0.1)
        option4 = decimal.Decimal(0.1)
        
        ans_idx = random.randint(1, 4)
        if ans_idx == 1:
            option1 = answer
            option2 = answer + decimal.Decimal(0.1)
            option3 = answer + decimal.Decimal(0.2)
            option4 = answer - decimal.Decimal(0.1)
        if ans_idx == 2:
            option1 = answer + decimal.Decimal(0.1)
            option2 = answer
            option3 = answer + decimal.Decimal(0.2)
            option4 = answer - decimal.Decimal(0.1)
        if ans_idx == 3:
            option1 = answer + decimal.Decimal(0.1)
            option2 = answer + decimal.Decimal(0.2)
            option3 = answer
            option4 = answer - decimal.Decimal(0.1)
        if ans_idx == 4:
            option1 = answer + decimal.Decimal(0.1)
            option2 = answer - decimal.Decimal(0.1)
            option3 = answer + decimal.Decimal(0.2)
            option4 = answer
        #print(a, b, ans_idx, option1, option2, option3)		
        insert = pandas.DataFrame({'id': str(index+1), 'grade': current_grade, 'question_type': 'SC', 'question_text': str(equation), 'option_1': str(option1), 'option_2': str(option2), 'option_3': str(option3), 'option_4': str(option4), 'answer': str(ans_idx), 'lesson_id':1, 'question_img':'na'}, index=[index])
        myfd = myfd.append(insert,sort=True)
        index += 1
    #print (myfd)

if __name__=="__main__":
    main()