import os, json

def load_c_from_json(week, day):
    """json 파일을 불러와서 dict로 반환"""
    base = os.path.dirname(__file__)
    path = os.path.join(base, f'words/Week {week}_Day {day}.json')
    
    # 파일이 존재하는지 확인
    if not os.path.exists(path):
        print(f"⚠️ 파일이 존재하지 않습니다: {path}")
        return None
    
    # 파일 열기
    with open(path, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return data

def test():
    week, day = input("시험 볼 week와 day를 입력해 주세요: ").split()
    words = load_c_from_json(week, day)
    
    if words is None:
        return
    
    score = 0
    print("단어의 뜻을 입력해 주세요")

    for word in words:
        answer = input(f"{word['read']}: ")
        if answer == word['mean']:
            score += 1
    
    print(f"시험이 끝났습니다! 당신의 점수는 {score}/20 입니다.")

if __name__ == '__main__':
	test()