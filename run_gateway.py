from tokenomics.src.core.interceptor import TokenomicsGateway


def main():
    gateway = TokenomicsGateway()

    # Test payload utilizing our localized subject-oriented text
    test_phrase = "வணக்கம், எப்படி இருக்கிறீர்கள்? நான் இன்று ஒரு சிறந்த தொழில்நுட்ப AI பயன்பாட்டை உருவாக்க விரும்புகிறேன்."

    print("[*] Passing payload through Tokenomics Gateway...")

    # 1. Run Analysis Engine
    analysis = gateway.analyze_payload(test_phrase, "Tamil")

    # 2. Run Optimization Router
    routing_result = gateway.optimize_routing(analysis)

    print("\n" + "=" * 50)
    print("GATEWAY REAL-TIME LOGS")
    print("=" * 50)
    print(f"Language            : {routing_result['language']}")
    print(f"Strategy Applied    : {routing_result['strategy_applied']}")
    print(f"Before Token Count  : {routing_result['before_tokens']}")
    print(f"After Token Count   : {routing_result['after_tokens']}")
    print(f"Mitigated Tax Margin: {routing_result['economic_savings_formatted']}")
    print("=" * 50 + "\n")


if __name__ == "__main__":
    main()