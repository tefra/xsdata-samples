from dataclasses import dataclass, field
from typing import Any

from sdmx_ml.models.codelist_type import CodelistType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class GeoCodelistBaseType(CodelistType):
    """
    GeoCodelistBaseType is an abstract base refinement of a codelist that restricts
    the cods to be derived from the abstract GeoRefCode.
    """

    choice_2: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
