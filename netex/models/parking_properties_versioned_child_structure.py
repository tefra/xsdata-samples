from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .bay_geometry_enumeration import BayGeometryEnumeration
from .entity_in_version_structure import VersionedChildStructure
from .multilingual_string import MultilingualString
from .parking_area_refs_rel_structure import ParkingAreaRefsRelStructure
from .parking_capacities_rel_structure import ParkingCapacitiesRelStructure
from .parking_ref import ParkingRef
from .parking_stay_enumeration import ParkingStayEnumeration
from .parking_user_enumeration import ParkingUserEnumeration
from .parking_vehicle_enumeration import ParkingVehicleEnumeration
from .parking_visibility_enumeration import ParkingVisibilityEnumeration
from .transport_type_refs_rel_structure import TransportTypeRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ParkingPropertiesVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "ParkingProperties_VersionedChildStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_ref: None | ParkingRef = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_user_types: Iterable[ParkingUserEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingUserTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    parking_vehicle_types: Iterable[ParkingVehicleEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingVehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    vehicle_types: None | TransportTypeRefsRelStructure = field(
        default=None,
        metadata={
            "name": "vehicleTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_stay_list: Iterable[ParkingStayEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "ParkingStayList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    maximum_stay: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "MaximumStay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    secure_parking: None | bool = field(
        default=None,
        metadata={
            "name": "SecureParking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bay_geometry: None | BayGeometryEnumeration = field(
        default=None,
        metadata={
            "name": "BayGeometry",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parking_visibility: None | ParkingVisibilityEnumeration = field(
        default=None,
        metadata={
            "name": "ParkingVisibility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    areas: None | ParkingAreaRefsRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    spaces: None | ParkingCapacitiesRelStructure = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
