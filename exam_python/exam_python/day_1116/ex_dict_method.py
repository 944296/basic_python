#dict 데이터 타입 전용 메서드
#-------------------------------------------------
jumsu={"kor":[98,99,78], "art":[100,92,99]}
print(type(jumsu))
#키만 알고 싶어요~ 메서드 => dict.keys()
#키만 보여주는 형식으로 view객체
jumsukeys=jumsu.keys()
print(f"type: {type(jumsukeys)}, {jumsukeys}")
#print(f"jumsukeys[0]=> {jumsukeys[0]}")

#값만 알고 싶어요~ 메서드 => dict.values()
jumsuvalues=jumsu.values()
print(f"type: {type(jumsuvalues)}, {jumsuvalues}")

#키-값을 묶어서 보여주는 메서드 => dict.items()
#(키,값) 튜플로 묶어줌
jumsuitems=jumsu.items()
print(f"type: {type(jumsuitems)}, {jumsuitems}")

# 과목별 최고점수, 최저점수, 합계 알고 싶어요~
#jumsu={"kor":[98,99,78], "art":[100,92,99]}

jumsu={"kor":[98,99,78], "art":[100,92,99]}

# 1) 국어과목의 최고점수/최저점수/합계 
korjumsu=jumsu["kor"]
print(korjumsu)
print(f"합계: {sum(korjumsu)}, 최고: {max(korjumsu)}, 최저: {min(korjumsu)}")

# 2) 아트과목의 최고점수/최저점수/합계
artjumsu=jumsu["art"]
print(artjumsu)
print(f"합계: {sum(artjumsu)}, 최고: {max(artjumsu)}, 최저: {min(artjumsu)}")