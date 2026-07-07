# NovaVision Demo Package

This repository contains a lightweight NovaVision-style demo package for the `GNL - 03 Demo Package` task.

## What The Package Does

This demo package provides two image utility executors:

- `SingleImageInfoExecutor` receives one image-like input and returns one image summary output.
- `ImageCompareExecutor` receives two image-like inputs and returns two outputs: a comparison summary and a match score.

Both executors include a `dependentDropdownlist` configuration. The dropdown has two options:

- `BasicMode`, which exposes `textInput` and `dropdownlist` fields.
- `AdvancedMode`, which exposes `selectBox` and `textInput` fields.

## Trello Answers

`Package Github Repo's = https://github.com/Abd2023/novavision_Demo_Package.git`

`What does your package do = This demo package provides two image utility executors: one summarizes a single image input, and one compares two image inputs while demonstrating dynamic dependent dropdown configuration.`

## Checklist Coverage

- First executor: 1 input, 1 output.
- Second executor: 2 inputs, 2 outputs.
- Common feature: both executors have a `dependentDropdownlist`.
- First option: exposes 2 different field types, `textInput` and `dropdownlist`.
- Second option: exposes 2 different field types, `selectBox` and `textInput`.

## Project Structure

```text
apps/                 Example request payloads
notebooks/            Reserved for notebooks
resources/            Reserved for sample resources
src/executors/        Executor runtime classes
src/models/           Pydantic PackageModel and request/response models
tests/                Pytest validation for the Trello checklist
service.py            Lightweight executor lookup entrypoint
```

## Validate

```powershell
python -m pip install -r requirements.dev.txt
python -m pytest
```

