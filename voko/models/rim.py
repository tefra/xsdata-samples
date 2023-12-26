from dataclasses import dataclass, field
from typing import List, Optional
from voko.models.ctl import Ctl
from voko.models.em import Em
from voko.models.fnt import Fnt
from voko.models.frm import Frm
from voko.models.mis import Mis
from voko.models.mll import (
    Ekz,
    Klr,
    Ref,
    Refgrp,
)
from voko.models.sncref import Sncref
from voko.models.sub import Sub
from voko.models.sup import Sup
from voko.models.tld import Tld
from voko.models.ts import Ts


@dataclass(kw_only=True)
class Rim:
    class Meta:
        name = "rim"

    num: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mrk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    content: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "ref",
                    "type": Ref,
                },
                {
                    "name": "refgrp",
                    "type": Refgrp,
                },
                {
                    "name": "ekz",
                    "type": Ekz,
                },
                {
                    "name": "aut",
                    "type": str,
                },
                {
                    "name": "fnt",
                    "type": Fnt,
                },
                {
                    "name": "tld",
                    "type": Tld,
                },
                {
                    "name": "sncref",
                    "type": Sncref,
                },
                {
                    "name": "klr",
                    "type": Klr,
                },
                {
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "ts",
                    "type": Ts,
                },
                {
                    "name": "sup",
                    "type": Sup,
                },
                {
                    "name": "sub",
                    "type": Sub,
                },
                {
                    "name": "ctl",
                    "type": Ctl,
                },
                {
                    "name": "mis",
                    "type": Mis,
                },
                {
                    "name": "frm",
                    "type": Frm,
                },
                {
                    "name": "nom",
                    "type": str,
                },
                {
                    "name": "nac",
                    "type": str,
                },
                {
                    "name": "esc",
                    "type": str,
                },
            ),
        },
    )
