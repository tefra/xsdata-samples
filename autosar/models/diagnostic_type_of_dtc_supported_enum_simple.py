from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://autosar.org/schema/r4.0"


class DiagnosticTypeOfDtcSupportedEnumSimple(Enum):
    """
    :cvar ISO_11992_4: ISO11992-4 DTC format
    :cvar ISO_14229_1: ISO14229-1 DTC format (3 byte format)
    :cvar ISO_15031_6: ISO15031-6 DTC format (2 byte format)
    :cvar SAE_J_1939_73: SAEJ1939-73 DTC format
    :cvar SAE_J_2012_DA: SAE_J2012-DA_DTCFormat_00 (3 byte format)
    """

    ISO_11992_4 = "ISO-11992--4"
    ISO_14229_1 = "ISO-14229--1"
    ISO_15031_6 = "ISO-15031--6"
    SAE_J_1939_73 = "SAE-J-1939--73"
    SAE_J_2012_DA = "SAE-J-2012--DA"
