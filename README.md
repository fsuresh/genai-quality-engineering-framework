# GenAI Quality Engineering Framework

A Python-based automation framework for evaluating the quality, reliability, and safety of Generative AI and Large Language Model (LLM) applications.

## Project Overview

This project demonstrates an automated quality engineering approach for GenAI applications using Python and Pytest.

The framework is designed with reusable evaluation components, data-driven test scenarios, and automated execution reports.

## Current Features

- Reusable response quality evaluator
- Rule-based response validation
- Expected keyword validation
- Minimum response length validation
- Data-driven test execution using JSON
- Reusable Pytest fixtures
- HTML test execution reports

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Framework development |
| Pytest | Test automation |
| pytest-html | HTML reporting |
| JSON | Test data management |
| Pydantic | Data validation |
| Requests | API communication |
| python-dotenv | Environment configuration |

## Project Structure

```text
genai-quality-engineering-framework/
├── src/
│   └── genai_testing/
│       ├── __init__.py
│       ├── config.py
│       ├── evaluators.py
│       └── llm_client.py
├── tests/
│   ├── test_quality/
│   ├── test_safety/
│   └── conftest.py
├── test_data/
│   └── quality_test_cases.json
├── reports/
├── .github/
│   └── workflows/
├── requirements.txt
├── .env.example
├── README.md
└── LICENSE
```

## Installation

Clone the repository:

```bash
git clone https://github.com/fsuresh/genai-quality-engineering-framework.git
cd genai-quality-engineering-framework
```

Create and activate a virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Execute Tests

Run the complete test suite:

```bash
python -m pytest tests/ -v
```

## Generate HTML Reports

```bash
python -m pytest tests/ -v \
--html=reports/quality-report.html \
--self-contained-html
```

Open the generated report:

```bash
open reports/quality-report.html
```

## Planned Enhancements

- LLM API integration
- Semantic response evaluation
- Hallucination detection
- LLM-as-a-Judge evaluation
- Prompt injection testing
- Sensitive information leakage testing
- RAG evaluation
- AI agent testing
- CI/CD integration using GitHub Actions

## Project Goal

To demonstrate practical AI Quality Engineering capabilities by applying established software testing principles to Generative AI and LLM-based applications.

---

**Author:** Fredrick  
**Focus:** AI Quality Engineering | GenAI Testing | Python | Pytest | Automation Architecture