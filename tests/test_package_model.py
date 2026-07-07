from typing import get_args

from src.executors import ImageCompareExecutor, SingleImageInfoExecutor
from src.models import ImageCompareRequest, PackageModel, SingleImageInfoRequest
from src.models.package_model import AdvancedMode, BasicMode, ImageCompareModeConfig, SingleImageModeConfig


def model_fields(model_class):
    if hasattr(model_class, "model_fields"):
        return model_class.model_fields
    return model_class.__fields__


def option_field_types(option):
    fields = model_fields(option.__class__)
    return {
        getattr(getattr(option, field_name), "field")
        for field_name in fields
        if field_name not in {"name", "value", "type", "field"}
    }


def test_package_model_imports_and_instantiates():
    package = PackageModel()

    assert package.name == "NovaVisionDemoPackage"
    assert package.type == "capsule"
    assert package.configs.executor.field == "dropdownlist"


def test_first_executor_has_one_input_and_one_output():
    request = SingleImageInfoRequest()
    response = SingleImageInfoExecutor(request).run()

    assert len(model_fields(request.inputs.__class__)) == 1
    assert len(model_fields(response.outputs.__class__)) == 1
    assert "Received image reference" in response.outputs.image_summary.value


def test_second_executor_has_two_inputs_and_two_outputs():
    request = ImageCompareRequest()
    response = ImageCompareExecutor(request).run()

    assert len(model_fields(request.inputs.__class__)) == 2
    assert len(model_fields(response.outputs.__class__)) == 2
    assert response.outputs.comparison_summary.value.startswith("Compared first image")
    assert 0.0 <= response.outputs.match_score.value <= 1.0


def test_both_executor_configs_include_dependent_dropdown():
    single_request = SingleImageInfoRequest()
    compare_request = ImageCompareRequest()

    assert single_request.configs.Mode.field == "dependentDropdownlist"
    assert compare_request.configs.Mode.field == "dependentDropdownlist"


def test_dependent_dropdowns_have_at_least_two_options():
    single_options = get_args(model_fields(SingleImageModeConfig)["value"].annotation)
    compare_options = get_args(model_fields(ImageCompareModeConfig)["value"].annotation)

    assert {option.__name__ for option in single_options} >= {"BasicMode", "AdvancedMode"}
    assert {option.__name__ for option in compare_options} >= {"BasicMode", "AdvancedMode"}


def test_each_dropdown_option_exposes_two_different_field_types():
    assert option_field_types(BasicMode()) == {"textInput", "dropdownlist"}
    assert option_field_types(AdvancedMode()) == {"selectBox", "textInput"}
