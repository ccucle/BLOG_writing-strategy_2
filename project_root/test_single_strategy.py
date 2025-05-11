# 💡 이 파일은 하나의 전략만 독립적으로 테스트할 때 사용하세요.
# 전략 파일을 아래에서 교체하며 사용 가능합니다.

from strategies.structure_formatter import StructureFormatter  # ⬅ 테스트할 전략을 여기에 설정

# 테스트 입력 예제
context = {
    "text": "무기력하고 집중이 안 돼요. 루틴을 세워야 하는데 자꾸 망가져요. 집중, 집중, 집중.",
    "keywords": ["무기력", "집중", "루틴"],
    "user_emotion": "무기력"
}

# 전략 적용
result = StructureFormatter.apply(context)

# 결과 출력
print("\n📄 적용 결과 (text):")
print(result["text"])

if "tail_keywords" in result:
    print("\n🔖 생성된 롱테일 키워드:")
    print(result["tail_keywords"])

if "clarity_tips" in result:
    print("\n🧠 초보자 용어 설명 제안:")
    for tip in result["clarity_tips"]:
        print(f"- {tip}")

if "smartblock_flagged" in result:
    print("\n🚫 스마트블록 위험 키워드:")
    print(result["smartblock_flagged"])
