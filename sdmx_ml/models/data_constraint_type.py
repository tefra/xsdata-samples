from dataclasses import dataclass, field

from sdmx_ml.models.cube_region_type import CubeRegionType
from sdmx_ml.models.data_constraint_base_type import DataConstraintBaseType
from sdmx_ml.models.data_key_set_type import DataKeySetType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure"


@dataclass(frozen=True)
class DataConstraintType(DataConstraintBaseType):
    """DataConstraintType defines the structure of a data constraint.

    A data constraint can specify either the available set of keys
    (DataKeySet) or set of component values (CubeRegion) in a data
    source, or the allowable keys that can be constructed from a data
    structure definition. Multiple such constraints may be present for a
    constrained artefact. For instance, there may be a constraing that
    specifies the values allowed for the data source (role is "Allowed")
    which can be used for validation or for constructing a partial code
    list, whilst another constraing can specify the actual content of a
    data source (role is "Actual").

    :ivar data_key_set: DataKeySet defines a full, distinct set of
        dimension values and the attribute values associated with the
        key.
    :ivar cube_region: CubeRegion defines a slice of the data set
        (dimensions and attribute values) for the constrained artefact.
        A set of included or excluded regions can be described.
    """

    data_key_set: tuple[DataKeySetType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "DataKeySet",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
        },
    )
    cube_region: tuple[CubeRegionType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CubeRegion",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/structure",
            "max_occurs": 2,
        },
    )
