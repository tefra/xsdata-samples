from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class SplitTicketingSearch:
    """SplitTicketingSearch is optional.

    Used to return both One-Way and Roundtrip fares in a single search
    response. Applicable to 1G, 1V, 1P only, the price points results
    path, and a simple roundtrip search only. Cannot be used in
    combination with Flex options.

    Parameters
    ----------
    round_trip
        Percentage of Roundtrip price points to be returned in the search
        response. This should be an even number. The One-Way price points
        returned in the response would be evenly distributed between the
        outbound and the inbound.
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    round_trip: None | int = field(
        default=None,
        metadata={
            "name": "RoundTrip",
            "type": "Attribute",
        },
    )
