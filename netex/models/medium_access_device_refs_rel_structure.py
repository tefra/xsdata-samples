from dataclasses import dataclass, field

from .emv_card_ref import EmvCardRef
from .mobile_device_ref import MobileDeviceRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure
from .smartcard_ref import SmartcardRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class MediumAccessDeviceRefsRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "mediumAccessDeviceRefs_RelStructure"

    medium_access_device_ref: (
        MobileDeviceRef | EmvCardRef | SmartcardRef | None
    ) = field(
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
