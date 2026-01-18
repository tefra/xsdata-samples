from __future__ import annotations

from dataclasses import dataclass, field

from ipxact.models.signal_type_def import SignalTypeDef

__NAMESPACE__ = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"


@dataclass(kw_only=True)
class SignalTypeDefs:
    """
    The group of signal type definitions.
    """

    class Meta:
        name = "signalTypeDefs"
        namespace = "http://www.accellera.org/XMLSchema/IPXACT/1685-2022"

    signal_type_def: list[SignalTypeDef] = field(
        default_factory=list,
        metadata={
            "name": "signalTypeDef",
            "type": "Element",
            "min_occurs": 1,
        },
    )
