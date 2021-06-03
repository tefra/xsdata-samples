from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DataIdModeEnumSimple(Enum):
    """
    :cvar ALL_16_BIT: Two bytes are included in the CRC (double ID
        configuration).
    :cvar ALTERNATING_8_BIT: One of the two bytes byte is included,
        alternating high and low byte, depending on parity of the
        counter (alternating ID configuration). For even counter low
        byte is included; For odd counters the high byte is included.
    :cvar LOWER_12_BIT: The low byte is included in the implicit CRC
        calculation, the low nibble of the high byte is transmitted
        along with the data (i.e. it is explicitly included), the high
        nibble of the high byte is not used. This is applicable for the
        IDs up to 12 bits.
    :cvar LOWER_8_BIT: Only low byte is included, high byte is never
        used. This is applicable if the IDs in a particular system are 8
        bits.
    """
    ALL_16_BIT = "ALL-16-BIT"
    ALTERNATING_8_BIT = "ALTERNATING-8-BIT"
    LOWER_12_BIT = "LOWER-12-BIT"
    LOWER_8_BIT = "LOWER-8-BIT"
