import importlib.util
import os

class BaseStrategy:
    strategy_name = "Base Strategy"
    trigger_keywords = []

    @staticmethod
    def conditions(context: dict) -> bool:
        return True  # always applies by default

    @staticmethod
    def apply(context: dict) -> dict:
        return context  # default: no change


class StrategyLoader:
    def __init__(self):
        self.strategies = []

    def load_from_file(self, filepath: str):
        spec = importlib.util.spec_from_file_location("strategy_module", filepath)
        strategy_module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(strategy_module)
        for attr in dir(strategy_module):
            obj = getattr(strategy_module, attr)
            if isinstance(obj, type) and hasattr(obj, 'apply') and hasattr(obj, 'trigger_keywords'):
                self.strategies.append(obj())

    def load_from_directory(self, directory: str):
        for filename in os.listdir(directory):
            if filename.endswith(".py"):
                self.load_from_file(os.path.join(directory, filename))

    def get_all(self):
        return self.strategies


class StrategyDecider:
    def __init__(self, strategies):
        self.strategies = strategies

    def decide(self, context):
        return [s for s in self.strategies if any(k in context.get('text', '') for k in s.trigger_keywords)
                and s.conditions(context)]

    def apply_all(self, context):
        for strategy in self.decide(context):
            print(f"[Harmony] 전략 적용: {strategy.strategy_name}")
            context = strategy.apply(context)
        return context

    def list_strategies(self):
        print("\n🧠 등록된 전략 목록:")
        for s in self.strategies:
            print(f"• {s.strategy_name} (키워드: {s.trigger_keywords})")
