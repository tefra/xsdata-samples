from dataclasses import dataclass, field

from voko.models.bld_tip import BldTip
from voko.models.ekz import (
    Ind,
    Klr,
    Trd,
    Trdgrp,
)
from voko.models.fnt import Fnt
from voko.models.tld import Tld


@dataclass(kw_only=True)
class Bld:
    class Meta:
        name = "bld"

    lok: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    prm: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lrg: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    alt: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    tip: BldTip = field(
        default=BldTip.IMG,
        metadata={
            "type": "Attribute",
            "required": True,
        },
    )
    mrk: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "tld",
                    "type": Tld,
                },
                {
                    "name": "klr",
                    "type": Klr,
                },
                {
                    "name": "fnt",
                    "type": Fnt,
                },
                {
                    "name": "ind",
                    "type": Ind,
                },
                {
                    "name": "trd",
                    "type": Trd,
                },
                {
                    "name": "trdgrp",
                    "type": Trdgrp,
                },
            ),
        },
    )
