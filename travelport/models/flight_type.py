from __future__ import annotations
from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.travelport.com/schema/air_v52_0"


@dataclass
class FlightType:
    """
    Modifier to request flight type options example non-stop only, non-stop and
    direct only, include single online connection etc.

    Parameters
    ----------
    require_single_carrier
    max_connections
        The maximum number of connections within a segment group.
    max_stops
        The maximum number of stops within a connection.
    non_stop_directs
    stop_directs
    single_online_con
    double_online_con
    triple_online_con
    single_interline_con
    double_interline_con
    triple_interline_con
    """
    class Meta:
        namespace = "http://www.travelport.com/schema/air_v52_0"

    require_single_carrier: bool = field(
        default=False,
        metadata={
            "name": "RequireSingleCarrier",
            "type": "Attribute",
        }
    )
    max_connections: int = field(
        default=-1,
        metadata={
            "name": "MaxConnections",
            "type": "Attribute",
            "min_inclusive": -1,
            "max_inclusive": 3,
        }
    )
    max_stops: int = field(
        default=-1,
        metadata={
            "name": "MaxStops",
            "type": "Attribute",
            "min_inclusive": -1,
            "max_inclusive": 3,
        }
    )
    non_stop_directs: None | bool = field(
        default=None,
        metadata={
            "name": "NonStopDirects",
            "type": "Attribute",
        }
    )
    stop_directs: None | bool = field(
        default=None,
        metadata={
            "name": "StopDirects",
            "type": "Attribute",
        }
    )
    single_online_con: None | bool = field(
        default=None,
        metadata={
            "name": "SingleOnlineCon",
            "type": "Attribute",
        }
    )
    double_online_con: None | bool = field(
        default=None,
        metadata={
            "name": "DoubleOnlineCon",
            "type": "Attribute",
        }
    )
    triple_online_con: None | bool = field(
        default=None,
        metadata={
            "name": "TripleOnlineCon",
            "type": "Attribute",
        }
    )
    single_interline_con: None | bool = field(
        default=None,
        metadata={
            "name": "SingleInterlineCon",
            "type": "Attribute",
        }
    )
    double_interline_con: None | bool = field(
        default=None,
        metadata={
            "name": "DoubleInterlineCon",
            "type": "Attribute",
        }
    )
    triple_interline_con: None | bool = field(
        default=None,
        metadata={
            "name": "TripleInterlineCon",
            "type": "Attribute",
        }
    )
