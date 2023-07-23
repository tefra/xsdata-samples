from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class AirSearchAsynchModifiers:
    """
    Controls and switches for the Air Search request for Asynch Request.
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    initial_asynch_result: None | AirSearchAsynchModifiers.InitialAsynchResult = field(
        default=None,
        metadata={
            "name": "InitialAsynchResult",
            "type": "Element",
        }
    )

    @dataclass
    class InitialAsynchResult:
        """
        Parameters
        ----------
        max_wait
            Max wait time in seconds.
        """
        max_wait: None | int = field(
            default=None,
            metadata={
                "name": "MaxWait",
                "type": "Attribute",
            }
        )
