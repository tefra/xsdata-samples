from __future__ import annotations

from enum import StrEnum

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


class CellFunctionValueType(StrEnum):
    """
    Indicates legal cell function values.
    """

    NAND2 = "nand2"
    BUF = "buf"
    INV = "inv"
    MUX21 = "mux21"
    DFF = "dff"
    LATCH = "latch"
    XOR2 = "xor2"
    OTHER = "other"
