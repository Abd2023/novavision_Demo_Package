"""Executor entry points for the NovaVision demo package."""

from .image_compare_executor import ImageCompareExecutor
from .single_image_info_executor import SingleImageInfoExecutor

EXECUTORS = {
    "SingleImageInfoExecutor": SingleImageInfoExecutor,
    "ImageCompareExecutor": ImageCompareExecutor,
}

__all__ = ["EXECUTORS", "ImageCompareExecutor", "SingleImageInfoExecutor"]

