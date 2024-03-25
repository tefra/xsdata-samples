from dataclasses import dataclass

from sdmx_ml.models.maintainable_type import MaintainableType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class ConstraintBaseType(MaintainableType):
    """ConstraintBaseType is an abstract base type that forms the basis of the main
    abstract ConstraintType.

    It requires that a name be provided.
    """
