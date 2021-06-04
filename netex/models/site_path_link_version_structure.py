from dataclasses import dataclass, field
from typing import Optional
from netex.models.check_constraints_rel_structure import CheckConstraintsRelStructure
from netex.models.class_of_use_ref import ClassOfUseRef
from netex.models.equipment_places_rel_structure import EquipmentPlacesRelStructure
from netex.models.level_ref import LevelRef
from netex.models.local_services_rel_structure import LocalServicesRelStructure
from netex.models.multilingual_string import MultilingualString
from netex.models.path_link_version_structure import PathLinkVersionStructure
from netex.models.place_equipments_rel_structure import PlaceEquipmentsRelStructure
from netex.models.site_ref_structure import SiteRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class SitePathLinkVersionStructure(PathLinkVersionStructure):
    class Meta:
        name = "SitePathLink_VersionStructure"

    site_ref: Optional[SiteRefStructure] = field(
        default=None,
        metadata={
            "name": "SiteRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    level_ref: Optional[LevelRef] = field(
        default=None,
        metadata={
            "name": "LevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    check_constraints: Optional[CheckConstraintsRelStructure] = field(
        default=None,
        metadata={
            "name": "checkConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    equipment_places: Optional[EquipmentPlacesRelStructure] = field(
        default=None,
        metadata={
            "name": "equipmentPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    place_equipments: Optional[PlaceEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    local_services: Optional[LocalServicesRelStructure] = field(
        default=None,
        metadata={
            "name": "localServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
