from __future__ import annotations

from dataclasses import dataclass, field

from .air_submode import AirSubmode
from .bus_submode import BusSubmode
from .coach_submode import CoachSubmode
from .funicular_submode import FunicularSubmode
from .metro_submode import MetroSubmode
from .rail_submode import RailSubmode
from .self_drive_submode import SelfDriveSubmode
from .snow_and_ice_submode import SnowAndIceSubmode
from .taxi_submode import TaxiSubmode
from .telecabin_submode import TelecabinSubmode
from .tram_submode import TramSubmode
from .water_submode import WaterSubmode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportSubmodeStructure:
    choice: (
        None
        | AirSubmode
        | BusSubmode
        | CoachSubmode
        | FunicularSubmode
        | MetroSubmode
        | TramSubmode
        | TelecabinSubmode
        | RailSubmode
        | WaterSubmode
        | SnowAndIceSubmode
        | TaxiSubmode
        | SelfDriveSubmode
    ) = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AirSubmode",
                    "type": AirSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BusSubmode",
                    "type": BusSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CoachSubmode",
                    "type": CoachSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FunicularSubmode",
                    "type": FunicularSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MetroSubmode",
                    "type": MetroSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TramSubmode",
                    "type": TramSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TelecabinSubmode",
                    "type": TelecabinSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "RailSubmode",
                    "type": RailSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "WaterSubmode",
                    "type": WaterSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SnowAndIceSubmode",
                    "type": SnowAndIceSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiSubmode",
                    "type": TaxiSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SelfDriveSubmode",
                    "type": SelfDriveSubmode,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
