# 🧠 콘텐츠 품질 향상 전략 시스템 (SEO + 가독성 최적화용)

이 프로젝트는 **GPT가 작성한 블로그 글을 더 잘 읽히고, 더 검색되도록**  
자동으로 품질을 보정하는 전략 기반 시스템입니다.

> ❌ 애드센스 승인용 시스템이 아닙니다.  
> ✅ 일반 블로그 글의 품질 향상과 사용자 경험(UX) 최적화에 중점을 둡니다.

---

## 📂 프로젝트 구조

project_root/
├── harmony_strategy_hub.py # 전략 허브: 전략을 불러오고 실행 순서를 판단
├── apply_strategy.py # 전략을 불러와 글에 일괄 적용하는 실행 예제
├── test_single_strategy.py # 전략 하나만 개별 적용해보는 테스트 스크립트
├── strategies/ # ⬇ 전략 모듈 폴더
│ ├── init.py
│ ├── seo_keyword_optimizer.py # 키워드 반복 과다 감지 및 정리
│ ├── structure_formatter.py # 글의 서론-본론-결론 구조 정리
│ ├── tail_keyword_generator.py # 롱테일 키워드 하단 삽입
│ ├── smart_block_avoider.py # 광고 차단 유발 키워드 감지
│ ├── beginner_clarity_checker.py # 초보자도 이해할 수 있는 문장 가이드


---

## 🧠 적용 전략 요약

| 전략명 | 설명 |
|--------|------|
| **SeoKeywordOptimizer** | 키워드 반복 도배 방지 (SEO 최적화) |
| **StructureFormatter** | 서론-본론-결론 구조 정리로 가독성 향상 |
| **TailKeywordGenerator** | 하단에 연관 검색 유입 키워드 자동 삽입 |
| **SmartBlockAvoider** | 네이버 스마트블록 키워드 사전 감지 및 치환 제안 |
| **BeginnerClarityChecker** | 초보자 눈높이에 맞춘 용어 설명 삽입 유도 |

---

## ✅ 전략 모듈 작성 규칙

모든 전략은 다음 네 가지 요소를 포함해야 합니다:

```python
class ExampleStrategy:
    strategy_name = "전략 이름"
    trigger_keywords = ["맛집", "루틴", "검색"]

    @staticmethod
    def conditions(context) -> bool:
        return "맛집" in context.get("text", "")

    @staticmethod
    def apply(context) -> dict:
        context["text"] = context["text"].replace("맛집", "식당")
        return context

▶️ 사용 예시

from harmony_strategy_hub import apply_selected_strategy

context = {
    "text": "서울 맛집 추천 맛집 맛집...",
    "keywords": ["서울 맛집"],
    "user_level": "초보자"
}

result = apply_selected_strategy(context)
print(result["text"])

🔧 실행 순서 예시
키워드 반복 → 제한

스마트블록 키워드 → 교체

글 구조 → 서론-본론-결론 재정리

초보자 → 설명 문장 삽입

롱테일 키워드 → 글 끝에 삽입

💡 이 시스템이 필요한 사람
GPT가 작성한 글을 블로그에 그대로 쓰기엔 뭔가 부족한 사람

스마트블록, 검색 누락 등 블로그 운영 문제를 겪는 사람

가독성 높은 콘텐츠를 자동으로 만들고 싶은 사람

전략은 자동입니다.
하나하나 고를 필요 없이 순서대로 모두 적용됩니다.
여러분은 “글만 넣으면 됩니다.” ✨

