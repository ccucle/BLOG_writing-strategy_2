class TailKeywordGenerator:
    strategy_name = "체급 맞춤 롱테일 키워드 생성기"
    trigger_keywords = ["맛집", "여행", "리뷰", "후기", "체험"]

    @staticmethod
    def conditions(context: dict) -> bool:
        return "keywords" in context and len(context["keywords"]) > 0

    @staticmethod
    def apply(context: dict) -> dict:
        new_keywords = []
        for kw in context["keywords"]:
            # 간단한 롱테일 확장 규칙
            new_keywords.append(f"{kw} 추천")
            new_keywords.append(f"{kw} 후기")
            new_keywords.append(f"{kw} 꿀팁")
            new_keywords.append(f"{kw} 잘하는 법")
        context["tail_keywords"] = new_keywords
        return context