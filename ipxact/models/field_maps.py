from dataclasses import dataclass, field

from ipxact.models.field_map import FieldMap

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class FieldMaps:
    """
    Listing of maps between component port slices and field slices.
    """

    class Meta:
        name = "fieldMaps"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    field_map: list[FieldMap] = field(
        default_factory=list,
        metadata={
            "name": "fieldMap",
            "type": "Element",
            "min_occurs": 1,
        },
    )
