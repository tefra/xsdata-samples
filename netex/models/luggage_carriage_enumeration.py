from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class LuggageCarriageEnumeration(Enum):
    UNKNOWN = "unknown"
    NO_BAGGAGE_STORAGE = "noBaggageStorage"
    BAGGAGE_STORAGE = "baggageStorage"
    LUGGAGE_RACKS = "luggageRacks"
    EXTRA_LARGE_LUGGAGE_RACKS = "extraLargeLuggageRacks"
    BAGGAGE_VAN = "baggageVan"
    NO_CYCLES = "noCycles"
    CYCLES_ALLOWED = "cyclesAllowed"
    CYCLES_ALLOWED_IN_VAN = "cyclesAllowedInVan"
    CYCLES_ALLOWED_IN_CARRIAGE = "cyclesAllowedInCarriage"
    CYCLES_ALLOWED_WITH_RESERVATION = "cyclesAllowedWithReservation"
    VEHICLE_TRANSPORT = "vehicleTransport"
