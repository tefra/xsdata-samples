from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from .alternative_texts_rel_structure import VersionedChildStructure
from .boarding_permission_enumeration import BoardingPermissionEnumeration
from .class_of_use_ref import ClassOfUseRef
from .fare_class_enumeration import FareClassEnumeration
from .multilingual_string import MultilingualString
from .service_facility_set_ref import ServiceFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class OnboardStayVersionedChlldStructure(VersionedChildStructure):
    class Meta:
        name = "OnboardStay_VersionedChlldStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    service_facility_set_ref: Optional[ServiceFacilitySetRef] = field(
        default=None,
        metadata={
            "name": "ServiceFacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    boarding_permission: Optional[BoardingPermissionEnumeration] = field(
        default=None,
        metadata={
            "name": "BoardingPermission",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Period",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
