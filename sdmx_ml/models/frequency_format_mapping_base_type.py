from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.identifiable_type import IdentifiableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True, kw_only=True)
class FrequencyFormatMappingBaseType(IdentifiableType):
    """
    FrequencyFormatMappingBaseType defines the base refinement of the
    FrequencyFormatMappingType.

    Its purpose is to retrict the urn attribute.
    """
