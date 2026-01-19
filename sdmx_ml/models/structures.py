from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.structures_type import StructuresType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class Structures(StructuresType):
    """
    Structures contains constructs for all structural metadata components.
    """

    class Meta:
        namespace = (
            "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"
        )
