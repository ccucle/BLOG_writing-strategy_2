from harmony_strategy_hub import StrategyLoader, StrategyDecider

# 1. 전략 불러오기
loader = StrategyLoader()
loader.load_from_directory("strategies")

# 2. 적용기 초기화
decider = StrategyDecider(loader.get_all())

# 3. 샘플 문맥 입력
test_context = {
    "text": "서울 맛집 시제석 예약이 어려워요. 집중이 안 될 땐 루틴이 필요하죠. 맛집, 맛집, 맛집, 맛집, 맛집, 맛집.",
    "keywords": ["서울 맛집", "집중", "루틴"],
    "user_emotion": "무기력"
}

# 4. 전략 적용
final_context = decider.apply_all(test_context)

# 5. 결과 출력
print("\n📦 최종 적용된 컨텍스트 결과:")
for key, value in final_context.items():
    print(f"\n🔹 {key}:")
    print(value)
