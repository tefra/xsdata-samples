from __future__ import annotations

from dataclasses import dataclass, field

from generali.models.org.w3.pkg_2005.pkg_08.addressing.action import Action

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class ProblemActionType:
    action: None | Action = field(
        default=None,
        metadata={
            "name": "Action",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
        },
    )
    soap_action: None | str = field(
        default=None,
        metadata={
            "name": "SoapAction",
            "type": "Element",
            "namespace": "http://www.w3.org/2005/08/addressing",
        },
    )
    other_attributes: dict[str, str] = field(
        default_factory=dict,
        metadata={
            "type": "Attributes",
            "namespace": "##other",
        },
    )
