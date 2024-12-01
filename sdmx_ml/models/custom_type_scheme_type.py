from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.vtl_definition_scheme_type import VtlDefinitionSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CustomTypeSchemeType(VtlDefinitionSchemeType):
    """
    CustomTypeSchemeType defines a collection of custom types that are used in
    transformations.
    """

    choice_1: Any = field(
        init=False,
        default=None,
        metadata={
            "type": "Ignore",
        },
    )
