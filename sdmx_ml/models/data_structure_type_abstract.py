from dataclasses import dataclass

from sdmx_ml.models.payload_structure_type import PayloadStructureType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/common"


@dataclass(frozen=True)
class DataStructureTypeAbstract(PayloadStructureType):
    """
    DataStructureType is an abstract base type the forms the basis for the
    structural information for a data set.
    """

    class Meta:
        name = "DataStructureType"
