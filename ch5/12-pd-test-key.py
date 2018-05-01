import pandas as pd
# 키, 몸무게, 유형 데이터 프레임 생성하기
tbl = pd.DataFrame({
     "weight": [80.0, 70.4, 65.5, 45.9, 51.2, 72.5],
     "height": [170, 180, 155, 143, 154, 160],
     "type": ["f", "n", "n", "t", "t", "f"],
     "gender": ["f", "m", "m", "f", "f", "m"]
})
# 몸무게 목록 추출하기
print("몸무게 목록")
print(tbl["weight"])
# 몸무게와 키 목록 추출하기
print("몸무게와 키 목록")
print(tbl[["weight", "height"]])

# (0 부터 세었을 때 2~3번쨰 데이터 출력
print("tbl[2:4]\n", tbl[2:4])
# 3번쨰 이후 데이터 출력학;
print("tbl[3:]\n", tbl[3:])

print("--height rk 160 이상")
print(tbl[tbl.height >= 160])
print("--gender 가 m인 것")
print(tbl[tbl.gender == "m"])

