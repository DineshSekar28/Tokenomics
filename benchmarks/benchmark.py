import tiktoken

# Define standard pricing per million tokens
COST_PER_1M_INPUT = 2.50

LANGUAGES = {
    "English": "Hello, how are you? I am interested in building a strategic AI application today.",
    "Tamil": "வணக்கம், எப்படி இருக்கிறீர்கள்? நான் இன்று ஒரு சிறந்த தொழில்நுட்ப AI பயன்பாட்டை உருவாக்க விரும்புகிறேன்.",
    "Hindi": "नमस्ते, आप कैसे हैं? मैं आज एक रणनीतिक एआई एप्लिकेशन बनाने में रुचि रखता हूं।",
    "Spanish": "Hola, ¿cómo estás? Estoy interesado en construir una aplicación de IA estratégica hoy.",
    "Arabic": "مرحباً، كيف حالك؟ أنا مهتم ببناء تطبيق ذكاء اصطناعي استراتيجي اليوم."
}


def calculate_linguistic_tax():
    try:
        encoding = tiktoken.get_encoding("o200k_base")
    except ValueError:
        encoding = tiktoken.get_encoding("cl100k_base")

    print("\n" + "=" * 80)
    print("I am presenting you the difference in the cost per token for the same statement")
    print("in different languages to expose the structural 'Linguistic Tax' in global AI.")
    print("=" * 80)
    print(
        f"{'LANGUAGE':<12} | {'CHAR COUNT':<12} | {'TOKEN COUNT':<12} | {'EST. COST / 1M REQS':<20} | {'TAX MULTIPLIER'}")
    print("=" * 80)

    # Use English as the baseline
    base_tokens = len(encoding.encode(LANGUAGES["English"]))

    for lang, text in LANGUAGES.items():
        char_count = len(text)
        token_count = len(encoding.encode(text))

        # Calculate raw cost for 1,000,000 iterations of this specific prompt
        estimated_cost = (token_count / 1_000_000) * COST_PER_1M_INPUT * 1_000_000

        # Tax multiplier relative to English token efficiency
        tax_multiplier = token_count / base_tokens

        print(f"{lang:<12} | {char_count:<12} | {token_count:<12} | ${estimated_cost:<18.2f} | {tax_multiplier:.2f}x")

    print("=" * 80)


if __name__ == "__main__":
    calculate_linguistic_tax()