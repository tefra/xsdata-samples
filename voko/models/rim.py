from __future__ import annotations

from dataclasses import dataclass, field

from voko.models.aut import Aut
from voko.models.ctl import Ctl
from voko.models.ekz import (
    Ekz,
    Klr,
    Ref,
    Refgrp,
)
from voko.models.em import Em
from voko.models.esc import Esc
from voko.models.fnt import Fnt
from voko.models.frm import Frm
from voko.models.mis import Mis
from voko.models.nac import Nac
from voko.models.nom import Nom
from voko.models.sncref import Sncref
from voko.models.sub import Sub
from voko.models.sup import Sup
from voko.models.tld import Tld
from voko.models.ts import Ts


@dataclass(kw_only=True)
class Rim:
    class Meta:
        name = "rim"

    num: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    mrk: None | str = field(
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
                    "type": Aut,
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
                    "type": Nom,
                },
                {
                    "name": "nac",
                    "type": Nac,
                },
                {
                    "name": "esc",
                    "type": Esc,
                },
            ),
        },
    )
