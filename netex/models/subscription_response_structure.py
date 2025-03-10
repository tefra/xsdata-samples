from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .extensions_1 import Extensions1
from .response_endpoint_structure import ResponseEndpointStructure
from .response_status import ResponseStatus

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass
class SubscriptionResponseStructure(ResponseEndpointStructure):
    response_status: Iterable[ResponseStatus] = field(
        default_factory=list,
        metadata={
            "name": "ResponseStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    subscription_manager_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "SubscriptionManagerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_started_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ServiceStartedTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
