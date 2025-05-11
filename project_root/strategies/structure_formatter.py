class StructureFormatter:
    strategy_name = "본문 5단계 구조 자동 정리"
    trigger_keywords = ["가이드", "방법", "루틴", "무기력"]

    @staticmethod
    def conditions(context: dict) -> bool:
        return "text" in context and len(context["text"]) > 500

    @staticmethod
    def apply(context: dict) -> dict:
        text = context["text"]
        sentences = text.split(".")
        sections = {
            "서론": [],
            "본론1": [],
            "본론2": [],
            "본론3": [],
            "결론": []
        }

        # 문장을 나눠 각 파트에 균등 분배 (기초 로직)
        chunk = len(sentences) // 5 or 1
        keys = list(sections.keys())
        for i, key in enumerate(keys):
            sections[key] = ".".join(sentences[i*chunk:(i+1)*chunk]).strip()

        # 재조합
        formatted_text = "\n\n".join([f"🧩 {key}\n{body}" for key, body in sections.items()])
        context["text"] = formatted_text
        return context