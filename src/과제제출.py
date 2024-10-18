import pandas as pd
import numpy as np # 사용할 pandas, numpy 라이브러리 불러오기 

data = pd.read_csv('/Users/kwonyeojoon0221/Desktop/숭실대학교/과제 자료/data.csv') # 저장된 경로를 통해 data.csv 불러오기
df = np.array(data) # pandas DataFrame을 numpy 배열로 변환

# 각 과목별 점수를 numpy 배열로 추출
df_math = df[:5, 1]
df_eng = df[:5, 2]
df_py = df[:5, 3]

# 수학 점수의 평균, 표준 편차, 최대값, 최소값 계산
math_mean = df_math.mean()
math_std = df_math.std()
math_max = df_math.max()
math_min = df_math.min()

# 수학 점수가 가장 높은 학생의 이름 찾기
math_high = data.loc[data['수학'] >= math_max, '이름'].values[0]
print(f'수학 - Mean: {math_mean}, Std Dev: {math_std}, Max: {math_max}, Min: {math_min}\n수학에서 가장 높은 학생: {math_high}')

# 영어 점수의 평균, 표준 편차, 최대값, 최소값 계산
eng_mean = df_eng.mean()
eng_std = df_eng.std()
eng_max = df_eng.max()
eng_min = df_eng.min()

# 영어 점수가 가장 높은 학생의 이름 찾기
eng_high = data.loc[data['영어'] >= eng_max, '이름'].values[0]
print(f'영어 - Mean: {eng_mean}, Std Dev: {eng_std}, Max: {eng_max}, Min: {eng_min}\n영어에서 가장 높은 학생: {eng_high}')

# 파이썬 점수의 평균, 표준 편차, 최대값, 최소값 계산
py_mean = df_py.mean()
py_std = df_py.std()
py_max = df_py.max()
py_min = df_py.min()

# 파이썬 점수가 가장 높은 학생의 이름 찾기
py_high = data.loc[data['파이썬'] >= py_max, '이름'].values[0]
print(f'파이썬 - Mean: {py_mean}, Std Dev: {py_std}, Max: {py_max}, Min: {py_min}\n파이썬에서 가장 높은 학생: {py_high}')

#자신의 3과목 평균 점수가 전체 학생들의 평균 점수 이상인 학생 찾기 
mean_all=np.sum(data.sum(axis=0).values[1:4])/(data.iloc[:, 1:].count()).sum() #전체 평균
upto_mean=data.loc[data.iloc[:, 1:].mean(axis=1)>=mean_all, '이름'].values[:5]
print(f'평균 점수가 전체 학생들의 평균 점수 이상인 학생: {upto_mean}')

# 특정 과목 (예: Python)에서 80점 이상을 받은 학생 찾기
print(f'특정 과목 (예: Python)에서 80점 이상을 받은 학생 \n 수학: \n{data.loc[data['수학'] >= 80, ["이름", "수학"]].values[:5]} \n 영어: \n{data.loc[data['영어'] >= 80, ["이름", "영어"]].values[:5]} \n 파이썬: \n{data.loc[data['파이썬'] >= 80, ["이름", "파이썬"]].values[:5]}')

# 각 학생의 총점 계산
data['total'] = data['수학'] + data['영어'] + data['파이썬']

# 총점 기준으로 데이터 정렬
sorted_data = data.sort_values(by=['total'], ascending=False)
print(sorted_data)

# 정렬된 데이터를 CSV 파일로 저장
sorted_data.to_csv('sorted_data.csv', index=False, encoding='UTF-8')
print('"sorted_data.csv"파일에 저장됨')