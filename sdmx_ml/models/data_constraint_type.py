from __future__ import annotations

from dataclasses import dataclass, field

from sdmx_ml.models.cube_region_type import CubeRegionType
from sdmx_ml.models.data_constraint_base_type import DataConstraintBaseType
from sdmx_ml.models.data_key_set_type import DataKeySetType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure"


@dataclass(frozen=True, kw_only=True)
class DataConstraintType(DataConstraintBaseType):
    """
    DataConstraintType defines the structure of a data constraint.

    A data constraint contains the allowed values for the referencing
    artefact. These values are expressed either as sets of keys
    (DataKeySets) or sets of component values (CubeRegion) constructed from
    a data structure definition. Data constraints can be used, e.g., for
    validation or for defining a partial code list.

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
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
        },
    )
    cube_region: tuple[CubeRegionType, ...] = field(
        default_factory=tuple,
        metadata={
            "name": "CubeRegion",
            "type": "Element",
            "namespace": "http://www.sdmx.org/resources/sdmxml/schemas/v3_1/structure",
            "max_occurs": 2,
        },
    )
