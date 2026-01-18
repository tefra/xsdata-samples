from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass
class ShortDescription:
    """
    Brief description suitable for titles, software comments and pop-up
    windows.

    Being a SystemVerilog expression the text can be constructed using
    parameters, e.g, by concatentation or $sformatf().
    """

    class Meta:
        name = "shortDescription"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
