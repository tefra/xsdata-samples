from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class CrossmarkDomainExclusive:
    class Meta:
        name = "crossmark_domain_exclusive"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: bool = field(
        metadata={
            "required": True,
        }
    )
