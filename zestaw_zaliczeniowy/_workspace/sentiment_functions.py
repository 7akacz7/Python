
import re

POS_WORDS = {"good","great","excellent","wonderful","love","best","amazing","brilliant","perfect"}
NEG_WORDS = {"bad","worst","awful","terrible","hate","boring","waste","poor","horrible"}

def sentiment_score_mp(text: str) -> int:
    words = re.findall(r"\b\w+\b", text.lower())
    positive_count = sum(1 for word in words if word in POS_WORDS)
    negative_count = sum(1 for word in words if word in NEG_WORDS)
    return positive_count - negative_count
