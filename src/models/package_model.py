from __future__ import annotations

from typing import List, Literal, Union

from pydantic import BaseModel, Field


class NovaVisionModel(BaseModel):
    """Small base model compatible with the current Pydantic test runtime."""

    class Config:
        extra = "forbid"
        allow_population_by_field_name = True
        populate_by_name = True


class ImageValue(NovaVisionModel):
    uID: str = ""
    mimeType: Literal["image/png", "image/jpg", "image/jpeg"] = "image/png"
    base64: str = ""


class InputImage(NovaVisionModel):
    name: Literal["InputImage"] = "InputImage"
    value: ImageValue = Field(default_factory=ImageValue)
    type: Literal["Image"] = "Image"
    field: Literal["img"] = "img"

    class Config:
        title = "Input Image"


class FirstImage(NovaVisionModel):
    name: Literal["FirstImage"] = "FirstImage"
    value: ImageValue = Field(default_factory=ImageValue)
    type: Literal["Image"] = "Image"
    field: Literal["img"] = "img"

    class Config:
        title = "First Image"


class SecondImage(NovaVisionModel):
    name: Literal["SecondImage"] = "SecondImage"
    value: ImageValue = Field(default_factory=ImageValue)
    type: Literal["Image"] = "Image"
    field: Literal["img"] = "img"

    class Config:
        title = "Second Image"


class ImageSummary(NovaVisionModel):
    name: Literal["ImageSummary"] = "ImageSummary"
    value: str = "No image processed yet."
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Image Summary"


class ComparisonSummary(NovaVisionModel):
    name: Literal["ComparisonSummary"] = "ComparisonSummary"
    value: str = "No comparison processed yet."
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Comparison Summary"


class MatchScore(NovaVisionModel):
    name: Literal["MatchScore"] = "MatchScore"
    value: float = Field(default=0.0, ge=0.0, le=1.0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Match Score"


class FastMethodOption(NovaVisionModel):
    name: Literal["FastMethod"] = "FastMethod"
    value: Literal[1] = 1
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Fast Method"


class DetailedMethodOption(NovaVisionModel):
    name: Literal["DetailedMethod"] = "DetailedMethod"
    value: Literal[2] = 2
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Detailed Method"


class BrightnessFeatureOption(NovaVisionModel):
    name: Literal["BrightnessFeature"] = "BrightnessFeature"
    value: Literal[1] = 1
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Brightness Feature"


class ContrastFeatureOption(NovaVisionModel):
    name: Literal["ContrastFeature"] = "ContrastFeature"
    value: Literal[2] = 2
    type: Literal["string"] = "string"
    field: Literal["option"] = "option"

    class Config:
        title = "Contrast Feature"


class BasicThreshold(NovaVisionModel):
    name: Literal["BasicThreshold"] = "BasicThreshold"
    value: float = Field(default=0.5, ge=0.0, le=1.0)
    type: Literal["number"] = "number"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Basic Threshold"


class BasicMethod(NovaVisionModel):
    name: Literal["BasicMethod"] = "BasicMethod"
    value: Union[FastMethodOption, DetailedMethodOption] = Field(default_factory=FastMethodOption)
    type: Literal["object"] = "object"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Basic Method"


class AdvancedFeatures(NovaVisionModel):
    name: Literal["AdvancedFeatures"] = "AdvancedFeatures"
    value: List[Union[BrightnessFeatureOption, ContrastFeatureOption]] = Field(
        default_factory=lambda: [BrightnessFeatureOption()]
    )
    type: Literal["list"] = "list"
    field: Literal["selectBox"] = "selectBox"

    class Config:
        title = "Advanced Features"


class AdvancedLabel(NovaVisionModel):
    name: Literal["AdvancedLabel"] = "AdvancedLabel"
    value: str = "demo"
    type: Literal["string"] = "string"
    field: Literal["textInput"] = "textInput"

    class Config:
        title = "Advanced Label"


class BasicMode(NovaVisionModel):
    name: Literal["BasicMode"] = "BasicMode"
    value: Literal[1] = 1
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    threshold: BasicThreshold = Field(default_factory=BasicThreshold)
    method: BasicMethod = Field(default_factory=BasicMethod)

    class Config:
        title = "Basic Mode"


class AdvancedMode(NovaVisionModel):
    name: Literal["AdvancedMode"] = "AdvancedMode"
    value: Literal[2] = 2
    type: Literal["object"] = "object"
    field: Literal["option"] = "option"
    features: AdvancedFeatures = Field(default_factory=AdvancedFeatures)
    label: AdvancedLabel = Field(default_factory=AdvancedLabel)

    class Config:
        title = "Advanced Mode"


class SingleImageModeConfig(NovaVisionModel):
    name: Literal["SingleImageMode"] = "SingleImageMode"
    value: Union[BasicMode, AdvancedMode] = Field(default_factory=BasicMode)
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Single Image Mode"


class ImageCompareModeConfig(NovaVisionModel):
    name: Literal["ImageCompareMode"] = "ImageCompareMode"
    value: Union[BasicMode, AdvancedMode] = Field(default_factory=BasicMode)
    type: Literal["object"] = "object"
    field: Literal["dependentDropdownlist"] = "dependentDropdownlist"

    class Config:
        title = "Image Compare Mode"


class SingleImageInfoInputs(NovaVisionModel):
    input_image: InputImage = Field(default_factory=InputImage, alias="InputImage")


class SingleImageInfoConfigs(NovaVisionModel):
    Mode: SingleImageModeConfig = Field(default_factory=SingleImageModeConfig)


class SingleImageInfoOutputs(NovaVisionModel):
    image_summary: ImageSummary = Field(default_factory=ImageSummary, alias="ImageSummary")


class ImageCompareInputs(NovaVisionModel):
    first_image: FirstImage = Field(default_factory=FirstImage, alias="FirstImage")
    second_image: SecondImage = Field(default_factory=SecondImage, alias="SecondImage")


class ImageCompareConfigs(NovaVisionModel):
    Mode: ImageCompareModeConfig = Field(default_factory=ImageCompareModeConfig)


class ImageCompareOutputs(NovaVisionModel):
    comparison_summary: ComparisonSummary = Field(
        default_factory=ComparisonSummary, alias="ComparisonSummary"
    )
    match_score: MatchScore = Field(default_factory=MatchScore, alias="MatchScore")


class SingleImageInfoRequest(NovaVisionModel):
    name: Literal["SingleImageInfoExecutor"] = "SingleImageInfoExecutor"
    type: Literal["Request"] = "Request"
    inputs: SingleImageInfoInputs = Field(default_factory=SingleImageInfoInputs)
    configs: SingleImageInfoConfigs = Field(default_factory=SingleImageInfoConfigs)

    class Config:
        title = "Single Image Info Request"
        schema_extra = {"target": "configs"}
        json_schema_extra = {"target": "configs"}


class SingleImageInfoResponse(NovaVisionModel):
    name: Literal["SingleImageInfoExecutor"] = "SingleImageInfoExecutor"
    type: Literal["Response"] = "Response"
    outputs: SingleImageInfoOutputs = Field(default_factory=SingleImageInfoOutputs)

    class Config:
        title = "Single Image Info Response"


class ImageCompareRequest(NovaVisionModel):
    name: Literal["ImageCompareExecutor"] = "ImageCompareExecutor"
    type: Literal["Request"] = "Request"
    inputs: ImageCompareInputs = Field(default_factory=ImageCompareInputs)
    configs: ImageCompareConfigs = Field(default_factory=ImageCompareConfigs)

    class Config:
        title = "Image Compare Request"
        schema_extra = {"target": "configs"}
        json_schema_extra = {"target": "configs"}


class ImageCompareResponse(NovaVisionModel):
    name: Literal["ImageCompareExecutor"] = "ImageCompareExecutor"
    type: Literal["Response"] = "Response"
    outputs: ImageCompareOutputs = Field(default_factory=ImageCompareOutputs)

    class Config:
        title = "Image Compare Response"


class SingleImageInfoExecutorOption(NovaVisionModel):
    name: Literal["SingleImageInfoExecutor"] = "SingleImageInfoExecutor"
    value: Union[SingleImageInfoRequest, SingleImageInfoResponse] = Field(
        default_factory=SingleImageInfoRequest
    )
    type: Literal["Executor"] = "Executor"
    field: Literal["option"] = "option"

    class Config:
        title = "Single Image Info Executor"
        schema_extra = {"target": {"value": 0}}
        json_schema_extra = {"target": {"value": 0}}


class ImageCompareExecutorOption(NovaVisionModel):
    name: Literal["ImageCompareExecutor"] = "ImageCompareExecutor"
    value: Union[ImageCompareRequest, ImageCompareResponse] = Field(default_factory=ImageCompareRequest)
    type: Literal["Executor"] = "Executor"
    field: Literal["option"] = "option"

    class Config:
        title = "Image Compare Executor"
        schema_extra = {"target": {"value": 0}}
        json_schema_extra = {"target": {"value": 0}}


class ConfigExecutor(NovaVisionModel):
    name: Literal["Executor"] = "Executor"
    value: Union[SingleImageInfoExecutorOption, ImageCompareExecutorOption] = Field(
        default_factory=SingleImageInfoExecutorOption
    )
    type: Literal["Executor"] = "Executor"
    field: Literal["dropdownlist"] = "dropdownlist"

    class Config:
        title = "Executor"


class PackageConfigs(NovaVisionModel):
    executor: ConfigExecutor = Field(default_factory=ConfigExecutor, alias="Executor")


class PackageModel(NovaVisionModel):
    name: Literal["NovaVisionDemoPackage"] = "NovaVisionDemoPackage"
    type: Literal["capsule"] = "capsule"
    configs: PackageConfigs = Field(default_factory=PackageConfigs)

    class Config:
        title = "NovaVision Demo Package"
