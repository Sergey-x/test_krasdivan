def capture_price(price_text: str) -> int:
    text_price_value: str = ""
    for ch in price_text:
        text_price_value += ch if ch.isdigit() else ""
    return int(text_price_value)
