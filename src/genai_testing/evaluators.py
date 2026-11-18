
from dataclasses import dataclass
from typing import List


@dataclass
class EvaluationResult:
    passed: bool
    score: float
    reasons: List[str]


class ResponseQualityEvaluator:
    """
    Basic rule-based evaluator for GenAI responses.
    """

    def evaluate(
        self,
        response: str,
        expected_keywords: List[str] | None = None,
        min_length: int = 20
    ) -> EvaluationResult:

        reasons = []
        score = 100.0

        if not response or not response.strip():
            return EvaluationResult(
                passed=False,
                score=0.0,
                reasons=["Response is empty"]
            )

        if len(response.strip()) < min_length:
            score -= 30
            reasons.append("Response is shorter than minimum length")

        if expected_keywords:
            response_lower = response.lower()

            missing_keywords = [
                keyword
                for keyword in expected_keywords
                if keyword.lower() not in response_lower
            ]

            if missing_keywords:
                score -= 40
                reasons.append(
                    f"Missing expected keywords: {missing_keywords}"
                )

        if not reasons:
            reasons.append("All basic quality checks passed")

        return EvaluationResult(
            passed=score >= 70,
            score=max(score, 0.0),
            reasons=reasons
        )
