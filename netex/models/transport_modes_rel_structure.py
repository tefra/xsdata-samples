from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .containment_aggregation_structure import ContainmentAggregationStructure
from .open_transport_mode_ref import OpenTransportModeRef
from .transport_mode_structure import TransportModeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransportModesRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "transportModes_RelStructure"

    open_transport_mode_ref_or_transport_mode: Sequence[
        OpenTransportModeRef | TransportModeStructure
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OpenTransportModeRef",
                    "type": OpenTransportModeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TransportMode",
                    "type": TransportModeStructure,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
