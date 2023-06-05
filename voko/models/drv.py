from dataclasses import dataclass, field
from typing import List
from voko.models.adm import Adm
from voko.models.bld import Bld
from voko.models.dif import (
    Dif,
    Snc,
)
from voko.models.fnt import Fnt
from voko.models.gra import Gra
from voko.models.lstref import Lstref
from voko.models.mlg import Mlg
from voko.models.mll import (
    Ekz,
    Ref,
    Refgrp,
    Trd,
    Trdgrp,
)
from voko.models.rim import Rim
from voko.models.subdrv import Subdrv
from voko.models.tezrad import Tezrad
from voko.models.url import Url
from voko.models.uzo import Uzo
from voko.models.var import Kap


@dataclass(kw_only=True)
class Drv:
    class Meta:
        name = "drv"

    mrk: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    kap: Kap = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    subdrv: List[Subdrv] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    snc: List[Snc] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    fnt: List[Fnt] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    gra: List[Gra] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    uzo: List[Uzo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    dif: List[Dif] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ekz: List[Ekz] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    rim: List[Rim] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    ref: List[Ref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    refgrp: List[Refgrp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    trd: List[Trd] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    trdgrp: List[Trdgrp] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    bld: List[Bld] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    adm: List[Adm] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    url: List[Url] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    mlg: List[Mlg] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    lstref: List[Lstref] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    tezrad: List[Tezrad] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
