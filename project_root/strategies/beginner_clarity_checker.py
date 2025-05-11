class BeginnerClarityChecker:
    strategy_name = "초보자 이해도 점검기"
    trigger_keywords = ["전문용어", "리뷰", "설명", "정보"]

    @staticmethod
    def conditions(context: dict) -> bool:
        return "text" in context and len(context["text"]) > 300

    @staticmethod
    def apply(context: dict) -> dict:
        unclear_terms = []
        beginner_hints = []

        # 예시 전문 용어 (실제로는 외부 DB나 사용자 등록 가능)
        jargon_list = ["시제석", "객실 등급", "도슨트", "뷰카페"]

        for term in jargon_list:
            if term in context["text"]:
                unclear_terms.append(term)
                beginner_hints.append(f"'{term}'은 초보자에게 생소할 수 있어요. 간단히 설명을 추가하세요.")

        context["unclear_terms"] = unclear_terms
        context["clarity_tips"] = beginner_hints
        return context