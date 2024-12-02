from dataclasses import dataclass, field
from typing import Optional

from voko.models.adm import Adm
from voko.models.bld import Bld
from voko.models.drv import Drv
from voko.models.ekz import (
    Ekz,
    Ref,
    Refgrp,
    Trd,
    Trdgrp,
)
from voko.models.fnt import Fnt
from voko.models.gra import Gra
from voko.models.lstref import Lstref
from voko.models.mlg import Mlg
from voko.models.rim import Rim
from voko.models.snc import (
    Dif,
    Snc,
)
from voko.models.tezrad import Tezrad
from voko.models.url import Url
from voko.models.uzo import Uzo


@dataclass(kw_only=True)
class Subart:
    class Meta:
        name = "subart"

    mrk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    drv: list[Drv] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    snc: list[Snc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fnt: list[Fnt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    gra: list[Gra] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    uzo: list[Uzo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    dif: list[Dif] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ekz: list[Ekz] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    rim: list[Rim] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref: list[Ref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    refgrp: list[Refgrp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    trd: list[Trd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    trdgrp: list[Trdgrp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    bld: list[Bld] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    adm: list[Adm] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    url: list[Url] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mlg: list[Mlg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lstref: list[Lstref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tezrad: list[Tezrad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
