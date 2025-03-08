from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.baggage_information_type import BaggageInformationType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass
class BaggageInformationListType:
    """
    Baggage information list.
    """

    baggage_information: list[BaggageInformationType] = field(
        default_factory=list,
        metadata={
            "name": "BaggageInformation",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
        },
    )
