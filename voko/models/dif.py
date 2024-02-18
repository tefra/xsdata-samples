from dataclasses import dataclass, field
from typing import List, Optional, Type
from voko.models.adm import Adm
from voko.models.bld import Bld
from voko.models.ctl import Ctl
from voko.models.em import Em
from voko.models.esc import Esc
from voko.models.fnt import Fnt
from voko.models.frm import Frm
from voko.models.gra import Gra
from voko.models.lstref import Lstref
from voko.models.mis import Mis
from voko.models.mlg import Mlg
from voko.models.mll import (
    Ekz,
    Klr,
    Ref,
    Refgrp,
    Trd,
    Trdgrp,
)
from voko.models.nac import Nac
from voko.models.nom import Nom
from voko.models.rim import Rim
from voko.models.sncref import Sncref
from voko.models.sub import Sub
from voko.models.sup import Sup
from voko.models.tezrad import Tezrad
from voko.models.tld import Tld
from voko.models.ts import Ts
from voko.models.url import Url
from voko.models.uzo import Uzo


@dataclass(kw_only=True)
class Dif:
    class Meta:
        name = "dif"

    lng: Optional[str] = field(
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
                    "name": "trd",
                    "type": Trd,
                },
                {
                    "name": "trdgrp",
                    "type": Trdgrp,
                },
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
                    "name": "snc",
                    "type": Type["Snc"],
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


@dataclass(kw_only=True)
class Subsnc:
    class Meta:
        name = "subsnc"

    mrk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "ref",
            "type": "Attribute",
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


@dataclass(kw_only=True)
class Snc:
    class Meta:
        name = "snc"

    mrk: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref_attribute: Optional[str] = field(
        default=None,
        metadata={
            "name": "ref",
            "type": "Attribute",
        },
    )
    num: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    subsnc: List[Subsnc] = field(
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
