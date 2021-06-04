from dataclasses import dataclass, field
from typing import List, Optional
from netex.models.accommodation_facility_enumeration import AccommodationFacilityEnumeration
from netex.models.alternative_texts_rel_structure import VersionedChildStructure
from netex.models.berth_facility_enumeration import BerthFacilityEnumeration
from netex.models.class_of_use_ref import ClassOfUseRef
from netex.models.couchette_facility_enumeration import CouchetteFacilityEnumeration
from netex.models.fare_class_enumeration import FareClassEnumeration
from netex.models.gender_limitation_enumeration import GenderLimitationEnumeration
from netex.models.multilingual_string import MultilingualString
from netex.models.nuisance_facility_enumeration import NuisanceFacilityEnumeration
from netex.models.passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration
from netex.models.sanitary_facility_enumeration import SanitaryFacilityEnumeration
from netex.models.service_facility_set_ref import ServiceFacilitySetRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class AccommodationVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "Accommodation_VersionedChildStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_facility_set_ref: Optional[ServiceFacilitySetRef] = field(
        default=None,
        metadata={
            "name": "ServiceFacilitySetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_class: Optional[FareClassEnumeration] = field(
        default=None,
        metadata={
            "name": "FareClass",
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
    accommodation_facility: Optional[AccommodationFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "AccommodationFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    couchette_facility: Optional[CouchetteFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "CouchetteFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_berths: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfBerths",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    berth_facility: Optional[BerthFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "BerthFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    shower_facility: Optional[SanitaryFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ShowerFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    toilet_facility: Optional[SanitaryFacilityEnumeration] = field(
        default=None,
        metadata={
            "name": "ToiletFacility",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gender_limitation: Optional[GenderLimitationEnumeration] = field(
        default=None,
        metadata={
            "name": "GenderLimitation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    nuisance_facility_list: List[NuisanceFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "NuisanceFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    passenger_comms_facility_list: List[PassengerCommsFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PassengerCommsFacilityList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
