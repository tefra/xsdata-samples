from dataclasses import dataclass

from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class HierarchyBaseType(MaintainableType):
    """
    HierarchyBaseType is an abstract base class that is the basis for the
    HierarchyType.

    It requires that a name be supplied.
    """
