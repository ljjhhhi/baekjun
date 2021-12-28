import math
from collections import Counter

number=input('통계값을 구할 수를 컴마로 구분하여 입력하시오:')
num_list=number.split(',')
num_list = list(map(int, num_list))
num_list.sort()

#산술평균
mean=sum(num_list)/len(num_list)
#중앙값
if len(num_list)%2==0:
    first=int(len(num_list)/2)
    second=int(len(num_list)/2+1)
    median=(num_list[first-1]+num_list[second-1])/2
else:
    indx=math.ceil(len(num_list)/2)
    median=num_list[indx-1]

#최빈값
cnt = Counter(num_list).most_common(2) 
if len(cnt)>1:
    if cnt[0][1] == cnt[1][1]:
        mode=cnt[1][0]
else:
    mode=cnt[0][0]

#범위
rang=max(num_list)-min(num_list)

print('산술평균:{0:.0f}, 중앙값:{1}, 최빈값:{2}, 범위:{3}'.format(mean,median,mode,rang))
