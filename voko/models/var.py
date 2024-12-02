from dataclasses import dataclass, field

from voko.models.ekz import (
    Ekz,
    Klr,
)
from voko.models.fnt import Fnt
from voko.models.ofc import Ofc
from voko.models.rad import Rad
from voko.models.rim import Rim
from voko.models.tld import Tld
from voko.models.uzo import Uzo


@dataclass(kw_only=True)
class Var:
    class Meta:
        name = "var"

    kap: "Kap" = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    uzo: list[Uzo] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    klr: list[Klr] = field(
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


@dataclass(kw_only=True)
class Kap:
    class Meta:
        name = "kap"

    content: list[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
            "mixed": True,
            "choices": (
                {
                    "name": "rad",
                    "type": Rad,
                },
                {
                    "name": "ofc",
                    "type": Ofc,
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
                    "name": "var",
                    "type": Var,
                },
            ),
        },
    )
