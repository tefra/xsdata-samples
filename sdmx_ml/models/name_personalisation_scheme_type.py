from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.vtl_definition_scheme_type import VtlDefinitionSchemeType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class NamePersonalisationSchemeType(VtlDefinitionSchemeType):
    """
    NamePersonalisationSchemeType defines a set of personalisations of VTL standard
    names that are used in a set of transformations.
    """

    choice_1: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
