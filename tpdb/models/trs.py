from dataclasses import dataclass, field
from typing import Optional

from tpdb.models.comment import Comment
from tpdb.models.conditiontype import Conditiontype
from tpdb.models.higher_order_signature import HigherOrderSignature
from tpdb.models.rules import Rules
from tpdb.models.signature import Signature


@dataclass
class Trs:
    class Meta:
        name = "trs"

    rules: Optional[Rules] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Optional[Signature] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    higher_order_signature: Optional[HigherOrderSignature] = field(
        default=None,
        metadata={
            "name": "higherOrderSignature",
            "type": "Element",
        },
    )
    comment: Optional[Comment] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conditiontype: Optional[Conditiontype] = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
