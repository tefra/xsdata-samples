from __future__ import annotations

from dataclasses import dataclass, field

from voko.models.adm import Adm
from voko.models.bld import Bld
from voko.models.ctl import Ctl
from voko.models.ekz import (
    Ekz,
    Klr,
    Ref,
    Refgrp,
    Trd,
    Trdgrp,
)
from voko.models.em import Em
from voko.models.esc import Esc
from voko.models.fnt import Fnt
from voko.models.frm import Frm
from voko.models.gra import Gra
from voko.models.lstref import Lstref
from voko.models.mis import Mis
from voko.models.mlg import Mlg
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
class Snc:
    class Meta:
        name = "snc"

    mrk: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref_attribute: str | None = field(
        default=None,
        metadata={
            "name": "ref",
            "type": "Attribute",
        },
    )
    num: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    subsnc: list[Subsnc] = field(
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


@dataclass(kw_only=True)
class Dif:
    class Meta:
        name = "dif"

    lng: str | None = field(
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
                    "type": Snc,
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

    mrk: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    ref_attribute: str | None = field(
        default=None,
        metadata={
            "name": "ref",
            "type": "Attribute",
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
