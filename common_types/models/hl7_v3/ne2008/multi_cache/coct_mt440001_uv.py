from dataclasses import dataclass, field
from typing import List, Optional

from ..core.datatypes import (
    RtoMoPq,
    RtoPqPq,
)
from ..core.datatypes_base import (
    Cd,
    Cs,
    Ii,
    IvlTsExplicit,
    Mo,
)
from ..core.voc import (
    ActClass,
    ActMood,
    NullFlavor,
)

__NAMESPACE__ = "urn:hl7-org:v3"


@dataclass
class CoctMt440001UvValuedItem:
    class Meta:
        name = "COCT_MT440001UV.ValuedItem"

    realm_code: List[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: Optional[Ii] = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: List[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: List[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: Optional[Cd] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: Optional[IvlTsExplicit] = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    unit_quantity: Optional[RtoPqPq] = field(
        default=None,
        metadata={
            "name": "unitQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    unit_price_amt: Optional[RtoMoPq] = field(
        default=None,
        metadata={
            "name": "unitPriceAmt",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        },
    )
    net_amt: Optional[Mo] = field(
        default=None,
        metadata={
            "name": "netAmt",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: Optional[NullFlavor] = field(
        default=None,
        metadata={
            "name": "nullFlavor",
            "type": "Attribute",
        },
    )
    class_code: ActClass = field(
        init=False,
        default=ActClass.INVE,
        metadata={
            "name": "classCode",
            "type": "Attribute",
            "required": True,
        },
    )
    mood_code: ActMood = field(
        init=False,
        default=ActMood.DEF,
        metadata={
            "name": "moodCode",
            "type": "Attribute",
            "required": True,
        },
    )
