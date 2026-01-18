from __future__ import annotations

from dataclasses import dataclass

from generali.models.org.w3.pkg_2005.pkg_08.addressing.attributed_uritype import (
    AttributedUritype,
)

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class Action(AttributedUritype):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"
