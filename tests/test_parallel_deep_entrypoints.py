import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def test_parallel_deep_python_entrypoint_compiles():
    subprocess.run(
        [sys.executable, "-m", "py_compile", str(ROOT / "scripts/run_parallel_deep_research.py")],
        check=True,
        cwd=ROOT,
    )


def test_parallel_deep_shell_wrapper_has_valid_syntax():
    subprocess.run(
        ["bash", "-n", str(ROOT / "scripts/run_parallel_deep_benchmark.sh")],
        check=True,
        cwd=ROOT,
    )
