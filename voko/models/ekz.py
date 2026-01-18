from dataclasses import dataclass, field
from typing import ForwardRef

from voko.models.baz import Baz
from voko.models.ctl import Ctl
from voko.models.em import Em
from voko.models.esc import Esc
from voko.models.fnt import Fnt
from voko.models.frm import Frm
from voko.models.klr_tip import KlrTip
from voko.models.mis import Mis
from voko.models.mll_tip import MllTip
from voko.models.nac import Nac
from voko.models.nom import Nom
from voko.models.ofc import Ofc
from voko.models.ref_tip import RefTip
from voko.models.refgrp_tip import RefgrpTip
from voko.models.sncref import Sncref
from voko.models.sub import Sub
from voko.models.sup import Sup
from voko.models.tld import Tld
from voko.models.ts import Ts
from voko.models.uzo import Uzo


@dataclass(kw_only=True)
class Trdgrp:
    class Meta:
        name = "trdgrp"

    lng: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
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
                    "type": ForwardRef("Trd"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Ekz:
    class Meta:
        name = "ekz"

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
                    "name": "fnt",
                    "type": Fnt,
                },
                {
                    "name": "uzo",
                    "type": Uzo,
                },
                {
                    "name": "ref",
                    "type": ForwardRef("Ref"),
                },
                {
                    "name": "refgrp",
                    "type": ForwardRef("Refgrp"),
                },
                {
                    "name": "ind",
                    "type": ForwardRef("Ind"),
                },
                {
                    "name": "trd",
                    "type": ForwardRef("Trd"),
                },
                {
                    "name": "trdgrp",
                    "type": ForwardRef("Trdgrp"),
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
                    "type": ForwardRef("Klr"),
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
class Ref:
    class Meta:
        name = "ref"

    tip: RefTip | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    val: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lst: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    cel: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
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
                    "type": ForwardRef("Klr"),
                },
                {
                    "name": "sncref",
                    "type": Sncref,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Refgrp:
    class Meta:
        name = "refgrp"

    tip: RefgrpTip = field(
        default=RefgrpTip.VID,
        metadata={
            "type": "Attribute",
            "required": True,
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
                    "type": ForwardRef("Ref"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Trd:
    class Meta:
        name = "trd"

    lng: str | None = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fnt: str | None = field(
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
                    "name": "klr",
                    "type": ForwardRef("Klr"),
                },
                {
                    "name": "ind",
                    "type": ForwardRef("Ind"),
                },
                {
                    "name": "mll",
                    "type": ForwardRef("Mll"),
                },
                {
                    "name": "ofc",
                    "type": Ofc,
                },
                {
                    "name": "baz",
                    "type": Baz,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Klr:
    class Meta:
        name = "klr"

    tip: KlrTip | None = field(
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
                    "name": "ekz",
                    "type": Ekz,
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
                    "name": "tld",
                    "type": Tld,
                },
                {
                    "name": "sncref",
                    "type": Sncref,
                },
                {
                    "name": "klr",
                    "type": ForwardRef("Klr"),
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
class Ind:
    class Meta:
        name = "ind"

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
                    "name": "mll",
                    "type": ForwardRef("Mll"),
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Mll:
    class Meta:
        name = "mll"

    tip: MllTip | None = field(
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
                    "name": "ind",
                    "type": Ind,
                },
            ),
        },
    )
