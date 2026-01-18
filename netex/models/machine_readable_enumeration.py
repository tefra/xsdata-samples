from __future__ import annotations

from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class MachineReadableEnumeration(Enum):
    NONE = "none"
    MAGNETIC_STRIP = "magneticStrip"
    CHIP = "chip"
    OCR = "ocr"
    APNR = "apnr"
    BAR_CODE = "barCode"
    SHOT_CODE = "shotCode"
    NFC = "nfc"
    OTHER = "other"
