import json
import os

def save_c_to_json(words, week, day):
	"""json 파일로 저장"""
	base = os.path.dirname(__file__)
	path = os.path.join(base, f'words/Week {week}_Day {day}.json')
	os.makedirs(os.path.dirname(path), exist_ok=True)
	with open(path, 'w', encoding='utf-8') as f:
		json.dump(words, f, ensure_ascii=False, indent=2)


def add():
	week, day = input("week와 day를 입력해 주세요").split()
	print("20개의 단어의 발음과 뜻을 입력해 주세요 (예: 우에 위)")
	words = []
	for _ in range(20):
		read, mean = input().split()
		word = {"read": read, "mean": mean}
		words.append(word)
	save_c_to_json(words, week, day)
	return week, day
		
if __name__ == '__main__':
	week, day = add()
	print(f'Week {week} Day {day} 단어 20개가 Week {week}_Day {day}.json 파일로 저장되었습니다.')