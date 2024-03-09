from dataclasses import dataclass, field
from typing import List, Optional
from voko.models.adm import Adm
from voko.models.bld import Bld
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
class Subdrv:
    class Meta:
        name = "subdrv"

    mrk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    snc: List[Snc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    fnt: List[Fnt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    gra: List[Gra] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    uzo: List[Uzo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    dif: List[Dif] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ekz: List[Ekz] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    rim: List[Rim] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ref: List[Ref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    refgrp: List[Refgrp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    trd: List[Trd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    trdgrp: List[Trdgrp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    bld: List[Bld] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    adm: List[Adm] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    url: List[Url] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    mlg: List[Mlg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    lstref: List[Lstref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    tezrad: List[Tezrad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
