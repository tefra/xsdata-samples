from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.date_map_type import DateMapType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class EpochMapBaseType(DateMapType):
    """
    EpochMapBaseType defines the base refinement of the EpochMapType.

    Its purpose is to restrict the urn attribute.
    """
