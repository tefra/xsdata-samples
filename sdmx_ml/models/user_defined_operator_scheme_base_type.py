from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.vtl_definition_scheme_type import VtlDefinitionSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class UserDefinedOperatorSchemeBaseType(VtlDefinitionSchemeType):
    """UserDefinedOperatorSchemeBaseType is an abstract base type for the
    UserDefinedOperatorSchemeType.

    It restricts the item types to be only user defined operators.
    """

    choice_1: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
