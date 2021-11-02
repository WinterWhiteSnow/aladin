from book_list_split import book_list_split

# -*- coding: utf-8 -*-
string_list = """
[중고] 투로 1-6 완결. 별도 신무협
[중고] 용무쌍 1-8 완결. 신무협
[중고] 영웅 1~9 (완결)
[중고] [중고] 유아독존1-4(완)
[중고] 평지풍파 1-16 완결. 신무협 
[중고] 십몽무존 1~8 (완결)
[중고] 신마강림 1~6 (완결)
[중고] 절대검천. 1~11 완결. 신무협 
[중고] 강호제일 해결사 1~9 
[중고] 대소림사 (상,하) 
[중고] 검황도제 1~7 (완결)
[중고] 남궁전생 1~12
[중고] 달마삼검 1~8 (완결)
[중고] 월백1-7완
[중고] 병검무림1-6권(완결)
[중고] [중고] 흑천1-5(완결)
[중고] [중고] 청검1-7
[중고] 혈야천록1-3완
[중고] 절대맹주 1-11
[중고] 북명신공 1-7 완결 . 신무협 
[중고] 십만마도 1-7 완결. 신무협
[중고] 비정자객사1-6 완결. 신무협
[중고] 사도신검 1-5 완결 ☆북앤스토리☆ 
[중고] 흑룡 (黑龍) [작은책] 1~8 (완결) [상태양호]
[중고] 강호1-6완
[중고] 자명1-6완
[중고] 구범기 1-5 완결
[중고] 자승자박 1-7완결
[중고] 용맹마도 1~6 완결
[중고] 영약사 금오 1-7 완결-북유통-
[중고] 공간참 1-7 완결
[중고] [중고] 노는 칼1-7(완결) 
[중고] [중고] 귀환전기1-4(완결)
[중고] 질풍가 1-5완결
[중고] [중고] 반선 反仙 1-7(완결)
[중고] 천마조종 1-8완결
[중고] 용아십병 (龍牙十兵) [작은책] 1~7 (완결) [상태양호]
[중고] 풍현운기 1-5 완결
[중고] 소천악 1-5완결 
[중고] 낙화루 1-5완결-손병규 신무협
[중고] 남궁검존 1-6 완결
[중고] 심법 1-5(완결) /이원효
[중고] [중고] 불살사신 1-5(완결)
[중고] [중고] 나는 칼입니다1-6(완)
[중고] 용문쟁천 1-6 완결
[중고] 풍주 1-5 (완결)
[중고] 효우 1-5(완결) /김한승
[중고] 빙공의 대가(1~9완) 작은책
[중고] 묵검질풍록 1-6완결
[중고] [중고] 환희밀공 1-5(완결) 
[중고] 용사 1-9완결 -현민 신무협
[중고] 홍천 1~8(완결)
[중고] 면왕백리휴1-6
[중고] 호접지몽 (胡蝶之夢) 1-9 (완) 세트
[중고] 진호전기 1-8(완결)
[중고] 철혈의 선 1-7권 (완결) 
[중고] 생사신 1-7[전7권 완결]
[중고] 의검신화 1~6 완결
[중고] [중고] 무한진인 (無限眞人)1-6(완결)
[중고] 연단가 煉丹家 1~8 완결
[중고] 진조무쌍 1-7 (완결)
[중고] 용병불패 1-7(완결)
[중고] 혈존무적1-8완결
[중고] [중고] 혼원무벽1-6(완)
[중고] [중고] 폭류신공1-6(완)
[중고] [중고] 엄절고-엄마는 절대고수1-4(완)
[중고] [중고] 그의여행 1-5(완) 
[중고] 황룡전설 (黃龍傳說) 1-6 (완) 세트
[중고] 시공천마 1-5 완결
[중고] 진한열전1-6
[중고] 진삼 1-7 완결
[중고] [중고] 창판협기 1-11 완결
[중고] 시공열제 1-5 완결
[중고] [중고] 천년용왕1-6(완) 
[중고] 천뢰무한 (天雷無限) 1-8 (완) 세트 => 작은 판형
[중고] [중고] 흡정마공 1-6(완)
[중고] 패왕전설 1-6(완결)/천기성
[중고] [중고] 공갈검 (空竭劍) 1-7 (완) 세트
[중고] [중고] 잠룡물용1-7
[중고] 잡조행 1-7완결 
[중고] 호열지도 (號熱之道) 1-15 (완) 세트
[중고] [중고] 황제1-6(완결)
[중고] [중고] 철혈태제 1-6완결
[중고] 투한 1-6 완결
[중고] 은거기인 1-6완결 
[중고] [중고] 창천일성1-6(완)
[중고] [중고] 불사검존 (不死劍尊) 1-7 (완) 세트 => 작은 판형
[중고] 청천백일 (靑天白日) 1-7 (완) 세트
[중고] 장강 1-8 (완결)
[중고] 흑첨향 (黑甛鄕) 1-7 (완) 세트
[중고] 일검쟁천 1-7
[중고] [중고] 패왕초이1-7(완)
[중고] 파계 (破戒) 1-9 (완) 세트
[중고] 구천무제 1-4 완결
[중고] 현월비화1-6(완결)
[중고] 검명무명 (劍名無名) 1-8 (완) 세트
[중고] 한영전기 1-7완결
[중고] [중고] 무색의 참살자 1-5(완) 
[중고] [중고] 이것이나의복수다 1-7(완)
[중고] 군림가 1-9완결
[중고] [중고] 혈왕 (血王) 1-7 (완) 세트
[중고] 천지군림 1-6완결
[중고] 유가삼웅전 1-8 완결
[중고] [중고] 보법무적 1-6 (완결)
[중고] [중고] 검선 1-8(완)
[중고] [중고] 무소불위 1-5 (완결) 
[중고] 천하대란 (天下大亂) 1-8 (완) 세트
[중고] 금강야차 1-7 완결
[중고] 일검진천 (一劍震天) 1-6 (완) 세트 
[중고] 신룡전설 (神龍傳說) 1-6 (완) 세트
[중고] 무림대사부 1-6 완결
[중고] 영약사금오(1-7완)
[중고] [중고] 황제의귀환1-5(완결)
[중고] [중고] 총표두1-7(완결)
[중고] 운룡대팔식 1-7(완결)
[중고] 신룡의 후예 1-8 완결-북유통-
[중고] 이원연공 1-8 완결-북유통-
[중고] 금강무적 1-7 완결-북유통-
[중고] 대군룡회 1-10 완결-북유통-
[중고] 천하제패 1-6 완결-북유통-
[중고] 대형 설서린 1-10 완결 -북유통-
[중고] 무소불위 1-5 완결-북유통-
[중고] 현월비도 1-5 완결-북유통-
[중고] 신병이기 1-5 완결-북유통-
[중고] 천괴 1-7 완결-북유통-
[중고] 대천마 1-10 완결-북유통-
[중고] 뇌신전설 1-5 완결-북유통-
[중고] 서역유기 1-4 완결/춘객 신무협/1019
[중고] 무결검로 1-5 완결/마초 신무협/1020
[중고] 나는 칼입니다 1-6 완결/소소 신무협/263
[중고] 철혈마제 1-5 완결/광명 신무협/60
[중고] 마제 1-6 완결/뇌전검 신무협/1035
[중고] 단천붕지 1-7 완결/운룡 신무협/339
[중고] 무인지로 1~6 (완결)
[중고] 군사무적 1~6 (완결) 
[중고] 풍류운산. 1~5 (완결)
[중고] 천하제일 악인 1~6 (완결)
[중고] 마병자 1~5 (완결)
[중고] 월풍 (1~9 완결 ) (전혁 신무협 장편소설)
[중고] 신마강림 1~6 (완결)
[중고] 금강동인 1-7완결 이훈영 (지은이)
[중고] 암천제 1-10 - 제왕대전,완결 장담 (지은이) 
[중고] 환동무적 1~7완결 트웰브 (지은이)
[중고] 군왕번 1~8 완결 / 중걸 (지은이)
[중고] 마왕의 표국. 1~8 (완결) 천봉 (지은이) |
[중고] 취적취무 1~9 (완결) 설봉(雪峰) (지은이)
[중고] 반생무제 (1~7 완결)
[중고] 세 번째 삶 1~7 (완결)
[중고] 빙마전설 (1~7 완결)
[중고] 군림무적 (1~7 완결)
[중고] 북명신공(1~7 완결)
[중고] 용병불패 1~7 (완결)
[중고] 운해금룡 1~7 (완결)
[중고] 절대마제1-8완 남운 (지은이) 상태양호
[중고] 학사무림1-15완 봉황송 (지은이) 
[중고] 도사강호. 1-17완결 기공흑마 (지은이) 
[중고] 태극신무1-8완 사도연 (지은이) 


"""
def title_list():
	aaa = book_list_split(string_list)
	return aaa