from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.comment import Comment
from tpdb.models.conditiontype import Conditiontype
from tpdb.models.higher_order_signature import HigherOrderSignature
from tpdb.models.rules import Rules
from tpdb.models.signature import Signature


@dataclass(kw_only=True)
class Trs:
    class Meta:
        name = "trs"

    rules: Rules = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    signature: None | Signature = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    higher_order_signature: None | HigherOrderSignature = field(
        default=None,
        metadata={
            "name": "higherOrderSignature",
            "type": "Element",
        },
    )
    comment: None | Comment = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conditiontype: None | Conditiontype = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
