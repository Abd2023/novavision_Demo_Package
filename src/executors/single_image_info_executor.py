from __future__ import annotations

from typing import Any

from src.models import SingleImageInfoRequest, SingleImageInfoResponse
from src.models.package_model import ImageSummary, SingleImageInfoOutputs


class SingleImageInfoExecutor:
    """Demo executor with one image input and one text output."""

    def __init__(self, request: Any, bootstrap: dict[str, Any] | None = None) -> None:
        self.request = self._parse_request(request)
        self.bootstrap_data = bootstrap or {}

    @staticmethod
    def bootstrap() -> dict[str, str]:
        return {"executor": "SingleImageInfoExecutor", "status": "ready"}

    def run(self) -> SingleImageInfoResponse:
        image = self.request.inputs.input_image.value
        image_reference = image.uID or ("inline-base64" if image.base64 else "empty")
        mode = self.request.configs.Mode.value.name
        summary = (
            f"Received image reference '{image_reference}' with MIME type "
            f"'{image.mimeType}' using {mode}."
        )

        return SingleImageInfoResponse(
            outputs=SingleImageInfoOutputs(image_summary=ImageSummary(value=summary))
        )

    @staticmethod
    def _parse_request(request: Any) -> SingleImageInfoRequest:
        if isinstance(request, SingleImageInfoRequest):
            return request
        if hasattr(SingleImageInfoRequest, "model_validate"):
            return SingleImageInfoRequest.model_validate(request)
        return SingleImageInfoRequest.parse_obj(request)
