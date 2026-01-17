from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.exclude_root_type import ExcludeRootType
from sdmx_ml.models.simple_component_value_type import SimpleComponentValueType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class SimpleKeyValueType(SimpleComponentValueType):
    """
    SimpleKeyValueType derives from the SimpleValueType, but does not allow
    for the cascading of value in the hierarchy, as keys are meant to
    describe a distinct full or partial key.
    """

    cascade_values: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    lang: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    valid_from: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
    valid_to: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
