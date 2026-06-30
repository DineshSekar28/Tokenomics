import sys
from tokenomics.src.core.interceptor import TokenomicsGateway


def clear_screen():
    print("\n" * 3)


def run_cli_dashboard():
    gateway = TokenomicsGateway()

    while True:
        clear_screen()
        print("=" * 65)
        print("   TOKENOMICS: LINGUISTIC TAX OPTIMIZATION MIDDLEWARE DESKTOP   ")
        print("=" * 65)
        print(" 1. Analyze Sample Multilingual Scenarios")
        print(" 2. Enter Custom Prompt to Test Gateway Optimization Engine")
        print(" 3. Exit Console Application")
        print("-" * 65)

        choice = input("Select a strategic operations vector [1-3]: ").strip()

        if choice == "1":
            clear_screen()
            # Standard predefined scenarios
            scenarios = [
                ("English Baseline",
                 "Hello, how are you? I am interested in building a strategic AI application today.", "English"),
                ("Tamil Segment",
                 "வணக்கம், எப்படி இருக்கிறீர்கள்? நான் இன்று ஒரு சிறந்த தொழில்நுட்ப AI பயன்பாட்டை உருவாக்க விரும்புகிறேன்.",
                 "Tamil"),
                ("Hindi Segment", "नमस्ते, आप कैसे हैं? मैं आज एक रणनीतिक एआई एप्लिकेशन बनाने में रुचि रखता हूं।",
                 "Hindi")
            ]

            print("=" * 85)
            print(
                f"{'LANG':<10} | {'TOKENS':<8} | {'SUBSIDY NEEDED?':<18} | {'MITIGATED SAVINGS':<18} | {'ROUTING STRATEGY'}")
            print("=" * 85)

            for title, text, lang in scenarios:
                analysis = gateway.analyze_payload(text, lang)
                result = gateway.optimize_routing(analysis)

                metrics = analysis["metrics"]
                subsidy_str = "YES [TAX DETECTED]" if metrics["requires_tokenomic_subsidy"] else "NO [OPTIMAL]"

                print(
                    f"{lang:<10} | {metrics['tokens']:<8} | {subsidy_str:<18} | {result['economic_savings_formatted']:<18} | {result['strategy_applied']}")

            print("=" * 85)
            input("\nPress Enter to return to headquarters command view...")

        elif choice == "2":
            clear_screen()
            print("--- ENTER TESTING PAYLOAD ---")
            lang = input("Target Language Name (e.g., Tamil, Spanish, Telugu): ").strip()
            text = input("Enter prompt payload string: ").strip()

            if not text or not lang:
                print("[!] Error: Payload contents cannot be empty.")
                input("\nPress Enter to retry...")
                continue

            print("\n[*] Processing through Tokenomics network nodes...")
            analysis = gateway.analyze_payload(text, lang)
            result = gateway.optimize_routing(analysis)

            print("\n" + "-" * 55)
            print(f"  ANALYSIS MATRIX FOR LAYER: {lang.upper()}")
            print("-" * 55)
            print(f"  Character Overhead     : {analysis['metrics']['characters']}")
            print(f"  Raw Token Consumption  : {analysis['metrics']['tokens']}")
            print(f"  Tokens After Gateway   : {result['after_tokens']}")
            print(f"  Financial Tax Mitigated: {result['economic_savings_formatted']}")
            print(f"  Selected Node Route    : {result['strategy_applied']}")
            print("-" * 55)
            input("\nProcessing completed. Press Enter to return to main terminal interface...")

        elif choice == "3":
            print("\n[*] Shutting down gateway node orchestration. Fair winds!")
            sys.exit(0)

        else:
            print("[!] Invalid operation vector code selected.")
            time.sleep(1)


if __name__ == "__main__":
    run_cli_dashboard()