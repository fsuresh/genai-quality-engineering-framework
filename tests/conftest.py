import json
from pathlib import Path

import pytest

from src.genai_testing.evaluators import ResponseQualityEvaluator


@pytest.fixture
def evaluator():
    """Provides a reusable response quality evaluator."""
    return ResponseQualityEvaluator()


@pytest.fixture
def quality_test_cases():
    """Loads quality scenarios from the JSON test data file."""

    project_root = Path(__file__).resolve().parent.parent
    test_data_path = project_root / "test_data" / "quality_test_cases.json"

    with open(test_data_path, "r", encoding="utf-8") as file:
        return json.load(file)
