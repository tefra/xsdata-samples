from __future__ import annotations

from dataclasses import dataclass, field

from .private_code import PrivateCode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AliasStructure:
    private_code: PrivateCode = field(
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    identifier_type: None | str = field(
        default=None,
        metadata={
            "name": "IdentifierType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
