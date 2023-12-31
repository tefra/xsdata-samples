from dataclasses import dataclass, field
from typing import Optional, Union
from .emv_card_ref import EmvCardRef
from .mobile_device_ref import MobileDeviceRef
from .security_listing_versioned_child_structure import (
    SecurityListingVersionedChildStructure,
)
from .smartcard_ref import SmartcardRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MediumAccessDeviceSecurityListingVersionedChildStructure(
    SecurityListingVersionedChildStructure
):
    class Meta:
        name = "MediumAccessDeviceSecurityListing_VersionedChildStructure"

    medium_access_device_ref: Optional[
        Union[MobileDeviceRef, EmvCardRef, SmartcardRef]
    ] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "MobileDeviceRef",
                    "type": MobileDeviceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "EmvCardRef",
                    "type": EmvCardRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SmartcardRef",
                    "type": SmartcardRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
