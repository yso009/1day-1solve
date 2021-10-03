#
# 문자열 학습 01
#

#
# 기능 : 여러 포맷의 날짜 문자열을 yyyymmmdd 형태의 문자열로 변환
#  input : input_date (String, 여러 형태의 날짜 문자열)
# output : output_date (String, yyyymmdd 형태의 문자열)
#
def func(item):
    #    Write your code
    c = 0
    for i in range(len(item)):
        if item[i].isdigit() == True:
            c +=1
        else:
            c -=1
    if c == 8:
        return item

    r = ''  
    for i in range(len(item)):
        if item[i].isdigit() == True:  
            r += item[i]
        else:
            r += ' '
    r = r.lstrip() #왼쪽 공백 제거

    li = r.split(' ')

    result = []
    for i in range(len(li)):
        if li[i] != '':
            result.append(li[i])
    Y,M,D = 0, 1, 2
    year, month, day = '','',''

    if len(result[Y]) != 4:
        year += '20' + result[Y]
    else:
        year += result[Y]

    if len(result[M]) != 2:
        month = '0' + result[M]
    else:
        month += result[M]

    if len(result[D]) != 2:
        day += '0' + result[D]
    else:
        day += result[D]

    output_date = year+month+day
    return output_date


#
# 건들지 말 것
#
if __name__ == "__main__":
    sample_date_list = ["2021 9 30", "2021.09.30.", "21-9-30", "`21.09.30.", "21년 9월 30일", "2021-09-30", "2021-9-30", "2021년 9월 30일", "오늘은 2021년 9월 30일 입니다.","20210930", "2021.09.30."]

    for item in sample_date_list:
        result = func(item)
        
        item = item if len(item) >= 8 else item+"\t"
        print(f"{item}\t\t→\t{result}", end="\t")
        
        if result == "20210930":
            print("성공")
            
        else:
            print("실패")