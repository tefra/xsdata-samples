from dataclasses import dataclass, field
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime
from .alternative_texts_rel_structure import (
    AvailabilityCondition,
    SimpleAvailabilityCondition,
    ValidDuring,
    ValidityCondition1,
    ValidityCondition2,
    ValidityRuleParameter,
    ValidityTrigger,
)
from .closed_timestamp_range_structure import ClosedTimestampRangeStructure
from .composite_frame_ref import CompositeFrameRef
from .driver_schedule_frame_ref import DriverScheduleFrameRef
from .empty_type_2 import EmptyType2
from .fare_frame_ref import FareFrameRef
from .general_frame_ref import GeneralFrameRef
from .infrastructure_frame_ref import InfrastructureFrameRef
from .network_filter_by_value_structure import NetworkFilterByValueStructure
from .resource_frame_ref import ResourceFrameRef
from .sales_transaction_frame_ref import SalesTransactionFrameRef
from .service_calendar_frame_ref import ServiceCalendarFrameRef
from .service_frame_ref import ServiceFrameRef
from .site_frame_ref import SiteFrameRef
from .timetable_frame_ref import TimetableFrameRef
from .topic_structure import TopicStructure
from .type_of_frame_ref import TypeOfFrameRef
from .vehicle_schedule_frame_ref import VehicleScheduleFrameRef
from .version_frame_ref import VersionFrameRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class NetworkFrameTopicStructure(TopicStructure):
    current: Optional[EmptyType2] = field(
        default=None,
        metadata={
            "name": "Current",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    changed_since: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ChangedSince",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    current_at: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "CurrentAt",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    historic_between: Optional[ClosedTimestampRangeStructure] = field(
        default=None,
        metadata={
            "name": "HistoricBetween",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    selection_validity_conditions: Optional["NetworkFrameTopicStructure.SelectionValidityConditions"] = field(
        default=None,
        metadata={
            "name": "selectionValidityConditions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_frame_ref: Optional[TypeOfFrameRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_transaction_frame_ref: List[SalesTransactionFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "SalesTransactionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_frame_ref: List[FareFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "FareFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_frame_ref: List[ServiceFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    driver_schedule_frame_ref: List[DriverScheduleFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "DriverScheduleFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_schedule_frame_ref: List[VehicleScheduleFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "VehicleScheduleFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    timetable_frame_ref: List[TimetableFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "TimetableFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    site_frame_ref: List[SiteFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "SiteFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    infrastructure_frame_ref: List[InfrastructureFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "InfrastructureFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    general_frame_ref: List[GeneralFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "GeneralFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    resource_frame_ref: List[ResourceFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ResourceFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    service_calendar_frame_ref: List[ServiceCalendarFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceCalendarFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    composite_frame_ref: List[CompositeFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "CompositeFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    version_frame_ref: List[VersionFrameRef] = field(
        default_factory=list,
        metadata={
            "name": "VersionFrameRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    network_filter_by_value: Optional[NetworkFilterByValueStructure] = field(
        default=None,
        metadata={
            "name": "NetworkFilterByValue",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )

    @dataclass
    class SelectionValidityConditions:
        simple_availability_condition: List[SimpleAvailabilityCondition] = field(
            default_factory=list,
            metadata={
                "name": "SimpleAvailabilityCondition",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        valid_during: List[ValidDuring] = field(
            default_factory=list,
            metadata={
                "name": "ValidDuring",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        availability_condition: List[AvailabilityCondition] = field(
            default_factory=list,
            metadata={
                "name": "AvailabilityCondition",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        validity_rule_parameter: List[ValidityRuleParameter] = field(
            default_factory=list,
            metadata={
                "name": "ValidityRuleParameter",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        validity_trigger: List[ValidityTrigger] = field(
            default_factory=list,
            metadata={
                "name": "ValidityTrigger",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        validity_condition: List[ValidityCondition1] = field(
            default_factory=list,
            metadata={
                "name": "ValidityCondition",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
        netex_org_uk_netex_validity_condition: List[ValidityCondition2] = field(
            default_factory=list,
            metadata={
                "name": "ValidityCondition_",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )
