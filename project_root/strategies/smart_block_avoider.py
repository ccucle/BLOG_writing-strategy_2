class SmartBlockAvoider:
    strategy_name = "스마트블록 회피 전략"
    trigger_keywords = ["맛집", "카페", "검색어"]

    @staticmethod
    def conditions(context: dict) -> bool:
        return "keywords" in context and len(context["keywords"]) > 0

    @staticmethod
    def apply(context: dict) -> dict:
        flagged = []
        safe_keywords = []

        # 예시 스마트블록 키워드 (하드코딩, 추후 API 연동 가능)
        smartblock_keywords = ["서울 맛집", "베스트 맛집", "핫플"]

        for kw in context["keywords"]:
            if kw in smartblock_keywords:
                flagged.append(kw)
                # 예: 회피 키워드 제안
                safe_keywords.append(f"{kw} 후기")
                safe_keywords.append(f"{kw} 사용자 경험")
            else:
                safe_keywords.append(kw)

        context["smartblock_flagged"] = flagged
        context["keywords"] = safe_keywords
        return context
