from __future__ import annotations

from dataclasses import dataclass, field

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


@dataclass(kw_only=True)
class CoctMt440001UvValuedItem:
    class Meta:
        name = "COCT_MT440001UV.ValuedItem"

    realm_code: list[Cs] = field(
        default_factory=list,
        metadata={
            "name": "realmCode",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    type_id: None | Ii = field(
        default=None,
        metadata={
            "name": "typeId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    template_id: list[Ii] = field(
        default_factory=list,
        metadata={
            "name": "templateId",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    id: list[Ii] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    code: None | Cd = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    effective_time: None | IvlTsExplicit = field(
        default=None,
        metadata={
            "name": "effectiveTime",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    unit_quantity: None | RtoPqPq = field(
        default=None,
        metadata={
            "name": "unitQuantity",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    unit_price_amt: RtoMoPq = field(
        metadata={
            "name": "unitPriceAmt",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
            "required": True,
        }
    )
    net_amt: None | Mo = field(
        default=None,
        metadata={
            "name": "netAmt",
            "type": "Element",
            "namespace": "urn:hl7-org:v3",
        },
    )
    null_flavor: None | NullFlavor = field(
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
