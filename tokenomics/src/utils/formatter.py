def format_currency(val: float) -> str:
    """Formats raw floats cleanly into standard micro-dollar annotations."""
    return f"${val:.7f}"

def format_percentage(val: float) -> str:
    """Formats float fractions to clean percentage metrics."""
    return f"{val:.2f}%"