from dataclasses import dataclass, field
from typing import Optional, Union
from xsdata.models.datatype import XmlDateTime, XmlDuration
from .class_of_use_ref import ClassOfUseRef
from .companion_profile_ref import CompanionProfileRef
from .fare_class_enumeration import FareClassEnumeration
from .group_of_operators_ref import GroupOfOperatorsRef
from .group_ticket_ref import GroupTicketRef
from .operator_ref import OperatorRef
from .passenger_seat_ref import PassengerSeatRef
from .series_constraint_refs_rel_structure import SeriesConstraintRefsRelStructure
from .service_facility_set import ServiceFacilitySet
from .train_component_label_assignment_ref import TrainComponentLabelAssignmentRef
from .train_element_ref import TrainElementRef
from .travel_specification_journey_refs_rel_structure import TravelSpecificationJourneyRefsRelStructure
from .travel_specification_summary_endpoint_structure import TravelSpecificationSummaryEndpointStructure
from .type_of_fare_product_ref import TypeOfFareProductRef
from .type_of_product_category_ref import TypeOfProductCategoryRef
from .user_profile_ref import UserProfileRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class TravelSpecificationSummaryViewStructure:
    origin: Optional[TravelSpecificationSummaryEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Origin",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    destination: Optional[TravelSpecificationSummaryEndpointStructure] = field(
        default=None,
        metadata={
            "name": "Destination",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "Start",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "End",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "Duration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journeys: Optional[TravelSpecificationJourneyRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    series_constraints: Optional[SeriesConstraintRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "seriesConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operator_ref_or_group_of_operators_ref: Optional[Union[OperatorRef, GroupOfOperatorsRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GroupOfOperatorsRef",
                    "type": GroupOfOperatorsRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    type_of_product_category_ref: Optional[TypeOfProductCategoryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_fare_product_ref: Optional[TypeOfFareProductRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFareProductRef",
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
    companion_profile_ref_or_user_profile_ref: Optional[Union[CompanionProfileRef, UserProfileRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompanionProfileRef",
                    "type": CompanionProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UserProfileRef",
                    "type": UserProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    group_ticket_ref: Optional[GroupTicketRef] = field(
        default=None,
        metadata={
            "name": "GroupTicketRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_users: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfUsers",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_element_ref: Optional[TrainElementRef] = field(
        default=None,
        metadata={
            "name": "TrainElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_component_label_assignment_ref: Optional[TrainComponentLabelAssignmentRef] = field(
        default=None,
        metadata={
            "name": "TrainComponentLabelAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passenger_seat_ref: Optional[PassengerSeatRef] = field(
        default=None,
        metadata={
            "name": "PassengerSeatRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_facility_set: Optional[ServiceFacilitySet] = field(
        default=None,
        metadata={
            "name": "ServiceFacilitySet",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
