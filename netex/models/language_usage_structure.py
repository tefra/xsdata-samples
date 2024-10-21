from collections.abc import Iterable
from dataclasses import dataclass, field
from typing import Optional

from .language_use_enumeration import LanguageUseEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass
class LanguageUsageStructure:
    language: Optional[str] = field(
        default=None,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        },
    )
    language_use: Iterable[LanguageUseEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "LanguageUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
