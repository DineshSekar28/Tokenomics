import tiktoken
from tokenomics.src.utils.formatter import format_currency  # Native utility integration

class TokenomicsGateway:
    """
    Core middleware engine responsible for intercepting multi-lingual payloads,
    analyzing structural tokenization inflation, and applying mitigation strategies.
    """
    def __init__(self, model_encoding: str = "o200k_base", base_cost_per_1m: float = 2.50):
        try:
            self.encoder = tiktoken.get_encoding(model_encoding)
        except ValueError:
            self.encoder = tiktoken.get_encoding("cl100k_base")

        self.base_cost_per_1m = base_cost_per_1m
        self.english_baseline_efficiency = 5.5  # Average characters per token for English

    def analyze_payload(self, text: str, language: str) -> dict:
        char_count = len(text)
        token_count = len(self.encoder.encode(text))
        raw_cost = (token_count / 1_000_000) * self.base_cost_per_1m

        # Determine real-world tokenization overhead
        chars_per_token = char_count / max(1, token_count)
        is_taxed = chars_per_token < (self.english_baseline_efficiency - 1.5)

        return {
            "language": language,
            "metrics": {
                "characters": char_count,
                "tokens": token_count,
                "chars_per_token": round(chars_per_token, 2),
                "raw_api_cost_usd": raw_cost,
                "requires_tokenomic_subsidy": is_taxed
            }
        }

    def optimize_routing(self, analysis: dict) -> dict:
        """
        Simulates tactical routing adjustments and formats economic outputs using internal utils.
        """
        metrics = analysis["metrics"]
        original_tokens = metrics["tokens"]

        if metrics["requires_tokenomic_subsidy"]:
            optimized_tokens = max(1, int(original_tokens * 0.60))
            optimized_cost = (optimized_tokens / 1_000_000) * self.base_cost_per_1m
            savings = metrics["raw_api_cost_usd"] - optimized_cost
            strategy = "Rerouted to localized vocabulary-extended compute cluster."
        else:
            optimized_tokens = original_tokens
            optimized_cost = metrics["raw_api_cost_usd"]
            savings = 0.0
            strategy = "Standard edge-routing profile applied."

        return {
            "language": analysis["language"],
            "strategy_applied": strategy,
            "before_tokens": original_tokens,
            "after_tokens": optimized_tokens,
            "economic_savings_formatted": format_currency(savings), # Clean string update
            "raw_savings_usd": savings
        }