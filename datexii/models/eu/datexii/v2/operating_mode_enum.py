from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class OperatingModeEnum(Enum):
    """
    Modes of operation of the exchange.

    :cvar OPERATING_MODE0: "Subscription Management Mechanism" - a
        specialized operating mode to handle subscriptions.
    :cvar OPERATING_MODE1: "Publisher Push on Occurrence" operating
        mode.
    :cvar OPERATING_MODE2: "Publisher Push Periodic" operating mode.
    :cvar OPERATING_MODE3: "Client Pull" operating mode.
    """
    OPERATING_MODE0 = "operatingMode0"
    OPERATING_MODE1 = "operatingMode1"
    OPERATING_MODE2 = "operatingMode2"
    OPERATING_MODE3 = "operatingMode3"
