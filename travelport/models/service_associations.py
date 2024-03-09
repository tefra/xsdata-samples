from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.optional_service_ref import OptionalServiceRef
from travelport.models.response_message_1 import ResponseMessage1

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class ServiceAssociations:
    """
    Parameters
    ----------
    applicable_segment
        Applicable air segment associated with this brand.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    applicable_segment: list[ServiceAssociations.ApplicableSegment] = field(
        default_factory=list,
        metadata={
            "name": "ApplicableSegment",
            "type": "Element",
            "min_occurs": 1,
            "max_occurs": 999,
        },
    )

    @dataclass
    class ApplicableSegment:
        """
        Parameters
        ----------
        response_message
        optional_service_ref
        key
            Applicable air segment key
        """

        response_message: None | ResponseMessage1 = field(
            default=None,
            metadata={
                "name": "ResponseMessage",
                "type": "Element",
                "namespace": "http://www.travelport.com/schema/common_v52_0",
            },
        )
        optional_service_ref: None | OptionalServiceRef = field(
            default=None,
            metadata={
                "name": "OptionalServiceRef",
                "type": "Element",
            },
        )
        key: None | str = field(
            default=None,
            metadata={
                "name": "Key",
                "type": "Attribute",
            },
        )
