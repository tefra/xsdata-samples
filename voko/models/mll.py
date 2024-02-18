from dataclasses import dataclass, field
from typing import List, Optional, Type
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
class Mll:
    class Meta:
        name = "mll"

    tip: Optional[MllTip] = field(
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
                    "name": "tld",
                    "type": Tld,
                },
                {
                    "name": "klr",
                    "type": Type["Klr"],
                },
                {
                    "name": "ind",
                    "type": Type["Ind"],
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Ref:
    class Meta:
        name = "ref"

    tip: Optional[RefTip] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    val: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    lst: Optional[str] = field(
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
    content: List[object] = field(
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
                    "type": Type["Klr"],
                },
                {
                    "name": "sncref",
                    "type": Sncref,
                },
            ),
        },
    )


@dataclass(kw_only=True)
class Ind:
    class Meta:
        name = "ind"

    content: List[object] = field(
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
                    "type": Type["Klr"],
                },
                {
                    "name": "mll",
                    "type": Mll,
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
            ),
        },
    )


@dataclass(kw_only=True)
class Trd:
    class Meta:
        name = "trd"

    lng: Optional[str] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
    fnt: Optional[str] = field(
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
                    "name": "klr",
                    "type": Type["Klr"],
                },
                {
                    "name": "ind",
                    "type": Ind,
                },
                {
                    "name": "mll",
                    "type": Mll,
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
class Trdgrp:
    class Meta:
        name = "trdgrp"

    lng: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
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
            ),
        },
    )


@dataclass(kw_only=True)
class Ekz:
    class Meta:
        name = "ekz"

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
                    "name": "fnt",
                    "type": Fnt,
                },
                {
                    "name": "uzo",
                    "type": Uzo,
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
                    "type": Type["Klr"],
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
class Klr:
    class Meta:
        name = "klr"

    tip: Optional[KlrTip] = field(
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
                    "type": Type["Klr"],
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
