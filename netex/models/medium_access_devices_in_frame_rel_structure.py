from __future__ import annotations

from collections.abc import Sequence
from dataclasses import dataclass, field

from .emv_card import EmvCard
from .frame_containment_structure import FrameContainmentStructure
from .mobile_device import MobileDevice
from .smartcard import Smartcard

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MediumAccessDevicesInFrameRelStructure(FrameContainmentStructure):
    class Meta:
        name = "mediumAccessDevicesInFrame_RelStructure"

    emv_card_or_smartcard_or_mobile_device: Sequence[
        EmvCard | Smartcard | MobileDevice
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "EmvCard",
                    "type": EmvCard,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Smartcard",
                    "type": Smartcard,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MobileDevice",
                    "type": MobileDevice,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
