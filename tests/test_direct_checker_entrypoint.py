from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_capability_wrapper_runs_checker_as_module_from_repo_root():
    text = (ROOT / "scripts/check_retrieval_capabilities.sh").read_text()
    assert 'cd "$ROOT"' in text
    assert '-m scripts.check_direct_retrieval_capabilities' in text


def test_setup_instructions_use_module_entrypoint():
    text = (ROOT / "scripts/setup_direct_retrieval_runner.sh").read_text()
    assert 'python -m scripts.check_direct_retrieval_capabilities' in text
    assert 'python scripts/check_direct_retrieval_capabilities.py' not in text
