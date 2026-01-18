from __future__ import annotations

from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .response_structure import ResponseStructure
from .service_delivery_error_condition_structure import (
    ServiceDeliveryErrorConditionStructure,
)
from .status import Status

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractDiscoveryDeliveryStructure(ResponseStructure):
    status: None | Status = field(
        default=None,
        metadata={
            "name": "Status",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    error_condition: None | ServiceDeliveryErrorConditionStructure = field(
        default=None,
        metadata={
            "name": "ErrorCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    valid_until: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "ValidUntil",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    shortest_possible_cycle: None | XmlDuration = field(
        default=None,
        metadata={
            "name": "ShortestPossibleCycle",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
