# [SDMX-ML](https://github.com/sdmx-twg/sdmx-ml) messages specifications

## Notes

- The suite is using (abusing) restrictions extensively
- The default structure style is causing circular imports errors, switched to `clusters`
- Enumerations extensions are not really supported in python, passing mypy for now is
  impossible
- It suffers from
  [variance](https://mypy.readthedocs.io/en/stable/common_issues.html#variance) issues
  but enabling frozen dataclasses resolves this
- A few of the original samples don't the schema validations

```console
❯ inv sdmx-ml.mypy
mypy sdmx_ml/models
sdmx_ml/models/basic_component_text_format_type.py:17: error: Incompatible types in assignment (expression has type "BasicComponentDataType", base class "TextFormatType" defined the type as "DataType")  [assignment]
sdmx_ml/models/simple_component_text_format_type.py:19: error: Incompatible types in assignment (expression has type "SimpleDataType", base class "BasicComponentTextFormatType" defined the type as "BasicComponentDataType")  [assignment]
sdmx_ml/models/time_text_format_type.py:20: error: Incompatible types in assignment (expression has type "TimeDataType", base class "SimpleComponentTextFormatType" defined the type as "SimpleDataType")  [assignment]
sdmx_ml/models/non_faceted_text_format_type.py:43: error: Incompatible types in assignment (expression has type "SimpleDataType | None", base class "SimpleComponentTextFormatType" defined the type as "SimpleDataType")  [assignment]
sdmx_ml/models/coding_text_format_type.py:31: error: Incompatible types in assignment (expression has type "SimpleCodeDataType | None", base class "SimpleComponentTextFormatType" defined the type as "SimpleDataType")  [assignment]
sdmx_ml/models/coded_text_format_type.py:35: error: Incompatible types in assignment (expression has type "CodeDataType | None", base class "SimpleComponentTextFormatType" defined the type as "SimpleDataType")  [assignment]
Found 6 errors in 6 files (checked 359 source files)
```

```console
============================================================================= short test summary info =============================================================================
SKIPPED [1] sdmx_ml/test_bindings.py:43: Original xml fails validation: Data - Complex Data Attributes/ECB_EXR_CA.xml
SKIPPED [1] sdmx_ml/test_bindings.py:43: Original xml fails validation: Data - Simple Data Attributes/ECB_EXR.xml
```

## Invoke Commands

```console
$ inv sdmx-ml.build
$ inv sdmx-ml.test
$ inv sdmx-ml.mypy
```
