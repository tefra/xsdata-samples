from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDuration

from .boarding_permission import BoardingPermission
from .class_of_use_ref import ClassOfUseRef
from .entity_in_version_structure import VersionedChildStructure
from .fare_class import FareClass
from .multilingual_string import MultilingualString
from .service_facility_set_ref import ServiceFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnboardStayVersionedChlldStructure(VersionedChildStructure):
    class Meta:
        name = "OnboardStay_VersionedChlldStructure"

    name: None | MultilingualString = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_facility_set_ref: None | ServiceFacilitySetRef = field(
        default=None,
        metadata={
            "name": "ServiceFacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_class: None | FareClass = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: None | ClassOfUseRef = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_permission: None | BoardingPermission = field(
        default=None,
        metadata={
            "name": "BoardingPermission",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    period: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
