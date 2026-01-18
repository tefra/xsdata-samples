from __future__ import annotations

from collections.abc import Iterable
from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .response_status import ResponseStatus

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SubscriptionResponseBodyStructure:
    response_status: Iterable[ResponseStatus] = field(
        default_factory=list,
        metadata={
            "name": "ResponseStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
        },
    )
    subscription_manager_address: None | str = field(
        default=None,
        metadata={
            "name": "SubscriptionManagerAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_started_time: None | XmlDateTime = field(
        default=None,
        metadata={
            "name": "ServiceStartedTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
