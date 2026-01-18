from __future__ import annotations

from dataclasses import dataclass, field

from travelport.models.flight_spec import FlightSpec

__NAMESPACE__ = "http://www.travelport.com/schema/util_v52_0"


@dataclass(kw_only=True)
class FareFamily:
    """
    It is a branded Fare for a carrier and given fare basis code.

    Parameters
    ----------
    flight_spec
        Flight number range or specific flight number for which this fare
        family would qualify.
    carrier
    label
    fare_basis
    key
    version
    """

    class Meta:
        namespace = "http://www.travelport.com/schema/util_v52_0"

    flight_spec: None | FlightSpec = field(
        default=None,
        metadata={
            "name": "FlightSpec",
            "type": "Element",
        },
    )
    carrier: str = field(
        metadata={
            "name": "Carrier",
            "type": "Attribute",
            "required": True,
            "length": 2,
        }
    )
    label: str = field(
        metadata={
            "name": "Label",
            "type": "Attribute",
            "required": True,
            "min_length": 0,
            "max_length": 32,
        }
    )
    fare_basis: str = field(
        metadata={
            "name": "FareBasis",
            "type": "Attribute",
            "required": True,
            "max_length": 20,
        }
    )
    key: None | str = field(
        default=None,
        metadata={
            "name": "Key",
            "type": "Attribute",
        },
    )
    version: int = field(
        metadata={
            "name": "Version",
            "type": "Attribute",
            "required": True,
        }
    )
