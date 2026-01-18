from dataclasses import dataclass, field

from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString
from .type_of_equipment_ref import TypeOfEquipmentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class VehicleEquipmentProfileMemberVersionStructure(VersionedChildStructure):
    class Meta:
        name = "VehicleEquipmentProfileMember_VersionStructure"

    name: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: MultilingualString | None = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_units: int | None = field(
        default=None,
        metadata={
            "name": "MinimumUnits",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_equipment_ref: TypeOfEquipmentRef | None = field(
        default=None,
        metadata={
            "name": "TypeOfEquipmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
