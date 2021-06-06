from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from .alternative_texts_rel_structure import DataManagedObjectStructure
from .booking_access_enumeration import BookingAccessEnumeration
from .booking_method_enumeration import BookingMethodEnumeration
from .contact_structure import ContactStructure
from .dated_special_service_ref import DatedSpecialServiceRef
from .dated_vehicle_journey_ref import DatedVehicleJourneyRef
from .dead_run_ref import DeadRunRef
from .flexible_service_enumeration import FlexibleServiceEnumeration
from .journey_ref import JourneyRef
from .multilingual_string import MultilingualString
from .purchase_moment_enumeration import PurchaseMomentEnumeration
from .purchase_when_enumeration import PurchaseWhenEnumeration
from .service_journey_ref import ServiceJourneyRef
from .special_service_ref import SpecialServiceRef
from .template_service_journey_ref import TemplateServiceJourneyRef
from .type_of_flexible_service_ref import TypeOfFlexibleServiceRef
from .vehicle_journey_ref import VehicleJourneyRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class FlexibleServicePropertiesVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "FlexibleServiceProperties_VersionStructure"

    dated_vehicle_journey_ref: List[DatedVehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    dated_special_service_ref: List[DatedSpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "DatedSpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    special_service_ref: List[SpecialServiceRef] = field(
        default_factory=list,
        metadata={
            "name": "SpecialServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    template_service_journey_ref: List[TemplateServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "TemplateServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    service_journey_ref: List[ServiceJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    dead_run_ref: List[DeadRunRef] = field(
        default_factory=list,
        metadata={
            "name": "DeadRunRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 3,
            "sequential": True,
        }
    )
    vehicle_journey_ref: List[VehicleJourneyRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "max_occurs": 2,
            "sequential": True,
        }
    )
    journey_ref: Optional[JourneyRef] = field(
        default=None,
        metadata={
            "name": "JourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_flexible_service_ref: Optional[TypeOfFlexibleServiceRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFlexibleServiceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flexible_service_type: Optional[FlexibleServiceEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleServiceType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cancellation_possible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CancellationPossible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    change_of_time_possible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ChangeOfTimePossible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_contact: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "BookingContact",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_methods: List[BookingMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BookingMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    booking_access: Optional[BookingAccessEnumeration] = field(
        default=None,
        metadata={
            "name": "BookingAccess",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    book_when: Optional[PurchaseWhenEnumeration] = field(
        default=None,
        metadata={
            "name": "BookWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    buy_when: List[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "BuyWhen",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    latest_booking_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "LatestBookingTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_booking_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumBookingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "BookingUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    booking_note: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "BookingNote",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
