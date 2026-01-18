from __future__ import annotations

from dataclasses import dataclass, field

from tpdb.models.comment import Comment
from tpdb.models.conditiontype import Conditiontype
from tpdb.models.higher_order_signature import HigherOrderSignature
from tpdb.models.rules import Rules
from tpdb.models.signature import Signature


@dataclass
class Trs:
    class Meta:
        name = "trs"

    rules: Rules | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    signature: Signature | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    higher_order_signature: HigherOrderSignature | None = field(
        default=None,
        metadata={
            "name": "higherOrderSignature",
            "type": "Element",
        },
    )
    comment: Comment | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    conditiontype: Conditiontype | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
