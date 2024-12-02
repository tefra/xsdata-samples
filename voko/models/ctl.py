from dataclasses import dataclass, field

from voko.models.em import Em
from voko.models.esc import Esc
from voko.models.frm import Frm
from voko.models.nac import Nac
from voko.models.nom import Nom
from voko.models.tld import Tld
from voko.models.ts import Ts


@dataclass(kw_only=True)
class Ctl:
    class Meta:
        name = "ctl"

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
                    "name": "em",
                    "type": Em,
                },
                {
                    "name": "ts",
                    "type": Ts,
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
