
from src.genai_testing.evaluators import ResponseQualityEvaluator


def test_valid_genai_response():
    evaluator = ResponseQualityEvaluator()

    response = (
        "Python is a programming language used for "
        "automation, artificial intelligence and testing."
    )

    result = evaluator.evaluate(
        response=response,
        expected_keywords=["Python", "automation", "testing"],
        min_length=20
    )

    assert result.passed is True
    assert result.score == 100.0


def test_empty_genai_response():
    evaluator = ResponseQualityEvaluator()

    result = evaluator.evaluate(response="")

    assert result.passed is False
    assert result.score == 0.0


def test_response_with_missing_keywords():
    evaluator = ResponseQualityEvaluator()

    result = evaluator.evaluate(
        response="Python is a useful programming language.",
        expected_keywords=["Python", "automation", "testing"]
    )

    assert result.passed is False
    assert "Missing expected keywords" in result.reasons[0]


def test_json_driven_quality_cases(evaluator, quality_test_cases):
    """
    Executes multiple quality scenarios using external JSON test data.
    """

    for test_case in quality_test_cases:

        result = evaluator.evaluate(
            response=test_case["response"],
            expected_keywords=test_case["expected_keywords"],
            min_length=test_case["min_length"]
        )

        assert result.passed == test_case["expected_pass"], (
            f"Test case failed: {test_case['name']}. "
            f"Reasons: {result.reasons}"
        )

