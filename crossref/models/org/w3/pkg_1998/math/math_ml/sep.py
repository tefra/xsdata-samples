from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.w3.org/1998/Math/MathML"


@dataclass(kw_only=True)
class Sep:
    class Meta:
        name = "sep"
        namespace = "http://www.w3.org/1998/Math/MathML"
