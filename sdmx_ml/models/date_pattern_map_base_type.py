from dataclasses import dataclass

from sdmx_ml.models.date_map_type import DateMapType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DatePatternMapBaseType(DateMapType):
    """
    DatePatternMapBaseType defines the base refinement of the
    DatePatternMapType.

    Its purpose is to retrict the urn attribute.
    """
