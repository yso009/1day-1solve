#
# 문자열 학습 01
#
#
# 기능 : 여러 포맷의 날짜 문자열을 yyyymmmdd 형태의 문자열로 변환
#  input : input_date (String, 여러 형태의 날짜 문자열)
# output : output_date (String, yyyymmdd 형태의 문자열)
#
def func(input_date):
    #    Write your code
    li = []
    for i in sample_date_list:
        r= ''
        for j in range(len(i)):
            if i[j].isdigit() == True:
                r += (i[j])
            else:
                r += '/'
        li.append(r)
    for i in sample_date_list:
        c = 0
        for j in range(len(i)-1):
            if i[j].isdigit() == True and i[j+1].isdigit() == False:
                if j < 3:
                    print(i[:j+1])
                    
    output_date =''
    return output_date




#
# 건들지 말 것
#
if __name__ == "__main__":
    sample_date_list = ["2021 1 30", "2021.02.30.", "21-3-30", "`21.04.30.", "21년 5월 30일", "2021-06-30", "2021-7-30", "2021년 8월 30일", "오늘은 2021년 9월 30일 입니다."]

    for item in sample_date_list:
        result = func(item)
        
        item = item if len(item) >= 8 else item+"\t"
        print(f"{item}\t\t→\t{result}", end="\t")
        
        if result == "20210930":
            print("성공")
            
        else:
            print("실패")