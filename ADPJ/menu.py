class Menu:

    def __init__(self):

        self.menu = [{"트러플 리치 포테이토 버거": ["난류", "우유", "대두", "밀", "토마토", "아황산류", "쇠고기", "굴"]},
                {"빅맥": ["난류", "우유", "대두", "밀", "소고기"]},
                {"에그 불고기 버거": ["난류", "대두", "밀", "돼지고기", "조개", "굴"]},
                {"1955 버거": ["난류", "우유", "대두", "밀", "돼지고기", "토마토", "쇠고기"]},
                {"슈비 버거": ["난류", "우유", "대두", "밀", "토마토", "새우", "쇠고기", "굴"]},
                {"베이컨 토마토 에그 머핀": ["난류", "대두", "밀", "돼지고기", "토마토"]},
                {"상하이 치킨 스낵랩": ["난류", "대두", "밀", "돼지고기", "닭고기"]},
                {"후렌치 후라이": ["대두"]},
                {"맥너겟": ["대두", "밀", "닭고기"]},
                {"골든 모짜렐라 치즈스틱": ["우유", "대두", "밀"]},
                {"츄러스": ["우유", "대두", "밀"]},
                {"베리스트로베리 맥플러리": ["우유", "대두", "밀"]},
                {"오레오 맥플러리": ["우유", "대두", "밀"]}]

        self.components_list = [] # 각 음식에 들어가는 모든 성분 담는 list
        self.food_key = [] # 음식 이름
        self.food_value = [] # 음식에 들어가는 성분

        # 한 곳에 담긴 음식 이름과 성분을 각각의 list로 바꾸어 줌
        for i in range(len(self.menu)):
            self.food_key += self.menu[i].keys()
            self.food_value += self.menu[i].values()

        # 모든 성분을 하나의 list에 담기 위함
        for j in range(len(self.food_value)):
            self.components_list += self.food_value[j]

        # 모든 성분을 하나의 list에 담은 후 set()을 이용한 중복 제거
        components_set = set(self.components_list)
        self.components_list = list(components_set)

        #사전순 정렬
        self.components_list.sort()