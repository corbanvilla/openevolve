from __future__ import annotations

from collections.abc import Callable
from os import PathLike

from .config import OpenEvolveConfig
from .evaluation_result import EvaluationResult


__all__: list[str]
__version__: str


class OpenEvolve:
    ...


def run_evolution(
    *,
    initial_program: str | PathLike[str],
    evaluator: Callable[[str], EvaluationResult],
    config: OpenEvolveConfig,
    iterations: int,
    output_dir: str | PathLike[str],
    target_score: float,
) -> None: ...
