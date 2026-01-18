from dataclasses import dataclass, field

from .check_constraints_rel_structure import CheckConstraintsRelStructure
from .class_of_use_ref import ClassOfUseRef
from .equipment_places_rel_structure import EquipmentPlacesRelStructure
from .level_ref import LevelRef
from .local_services_rel_structure import LocalServicesRelStructure
from .place_equipments_rel_structure import PlaceEquipmentsRelStructure
from .site_element_version_structure import SiteElementVersionStructure
from .site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SiteComponentVersionStructure(SiteElementVersionStructure):
    class Meta:
        name = "SiteComponent_VersionStructure"

    site_ref: SiteRefStructure | None = field(
        default=None,
        metadata={
            "name": "SiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    level_ref: LevelRef | None = field(
        default=None,
        metadata={
            "name": "LevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: ClassOfUseRef | None = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraints: CheckConstraintsRelStructure | None = field(
        default=None,
        metadata={
            "name": "checkConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipment_places: EquipmentPlacesRelStructure | None = field(
        default=None,
        metadata={
            "name": "equipmentPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_equipments: PlaceEquipmentsRelStructure | None = field(
        default=None,
        metadata={
            "name": "placeEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    local_services: LocalServicesRelStructure | None = field(
        default=None,
        metadata={
            "name": "localServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
