from dataclasses import dataclass, field
from typing import Tuple

from sdmx_ml.models.codelist_type import CodelistType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class CodelistsType:
    """CodelistsType describes the structure of the codelists container.

    It contains one or more codelist, which can be explicitly detailed
    or referenced from an external structure document or registry
    service.

    :ivar codelist: Codelist provides the details of a codelist, which
        is defined as a list from which some statistical concepts (coded
        concepts) take their values.
    """

    codelist: Tuple[CodelistType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "Codelist",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "min_occurs": 1,
        },
    )
