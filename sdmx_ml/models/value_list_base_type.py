from dataclasses import dataclass

from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ValueListBaseType(MaintainableType):
    """
    ValueListBaseType defines the base refinement of the ValueListType.

    Its purpose is to retrict the urn attribute.
    """
