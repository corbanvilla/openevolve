from __future__ import annotations

from typing import Any, Mapping


class EvaluationResult:
    metrics: Mapping[str, Any]
    artifacts: Mapping[str, Any]

    def __init__(
        self, *, metrics: Mapping[str, Any], artifacts: Mapping[str, Any]
    ) -> None: ...

    @classmethod
    def from_dict(cls, metrics: Mapping[str, Any]) -> EvaluationResult: ...

    def to_dict(self) -> Mapping[str, Any]: ...

    def has_artifacts(self) -> bool: ...

    def get_artifact_keys(self) -> list[str]: ...

    def get_artifact_size(self, key: str) -> int: ...

    def get_total_artifact_size(self) -> int: ...
