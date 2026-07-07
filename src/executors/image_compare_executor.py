from __future__ import annotations

from typing import Any

from src.models import ImageCompareRequest, ImageCompareResponse
from src.models.package_model import ComparisonSummary, ImageCompareOutputs, MatchScore


class ImageCompareExecutor:
    """Demo executor with two image inputs and two outputs."""

    def __init__(self, request: Any, bootstrap: dict[str, Any] | None = None) -> None:
        self.request = self._parse_request(request)
        self.bootstrap_data = bootstrap or {}

    @staticmethod
    def bootstrap() -> dict[str, str]:
        return {"executor": "ImageCompareExecutor", "status": "ready"}

    def run(self) -> ImageCompareResponse:
        first = self.request.inputs.first_image.value
        second = self.request.inputs.second_image.value
        mode = self.request.configs.Mode.value.name

        score = self._score_images(first.uID, first.base64, second.uID, second.base64)
        summary = (
            f"Compared first image '{first.uID or 'inline-or-empty'}' with second image "
            f"'{second.uID or 'inline-or-empty'}' using {mode}."
        )

        return ImageCompareResponse(
            outputs=ImageCompareOutputs(
                comparison_summary=ComparisonSummary(value=summary),
                match_score=MatchScore(value=score),
            )
        )

    @staticmethod
    def _parse_request(request: Any) -> ImageCompareRequest:
        if isinstance(request, ImageCompareRequest):
            return request
        if hasattr(ImageCompareRequest, "model_validate"):
            return ImageCompareRequest.model_validate(request)
        return ImageCompareRequest.parse_obj(request)

    @staticmethod
    def _score_images(first_uid: str, first_base64: str, second_uid: str, second_base64: str) -> float:
        if first_uid and second_uid and first_uid == second_uid:
            return 1.0
        if first_base64 and second_base64 and first_base64 == second_base64:
            return 1.0
        if first_uid or first_base64 or second_uid or second_base64:
            return 0.5
        return 0.0
