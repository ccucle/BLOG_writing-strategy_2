class SeoKeywordOptimizer:
    strategy_name = "키워드 반복 최적화"
    trigger_keywords = ["무기력", "집중", "루틴", "감정"]

    @staticmethod
    def conditions(context: dict) -> bool:
        return "keywords" in context and isinstance(context["keywords"], list)

    @staticmethod
    def apply(context: dict) -> dict:
        max_repeats = 5
        text = context.get("text", "")
        for kw in context["keywords"]:
            count = text.count(kw)
            if count > max_repeats:
                print(f"⚠️ 키워드 '{kw}'가 {count}회 사용됨 → {max_repeats}회로 제한")
                # 초과 부분 제거 (가장 단순한 형태)
                split_text = text.split(kw)
                text = (kw.join(split_text[:max_repeats])) + "".join(split_text[max_repeats:])
        context["text"] = text
        return context