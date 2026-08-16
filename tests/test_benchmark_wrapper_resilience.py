from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_benchmark_wrapper_reports_errors_and_uses_fallback_commit_identity():
    text = (ROOT / "scripts/run_retrieval_benchmark.sh").read_text()
    assert "report_retrieval_benchmark_errors" in text
    assert 'git -c user.name=' in text
    assert 'user.email=' in text
    assert 'git config --global' not in text
