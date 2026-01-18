from __future__ import annotations

from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class Issue:
    """
    The issue number or name in which an article is published.

    The issue number takes precedence over any other name. For example, if
    an issue has only a seasonal name, then the season should be listed in
    issue.
    """

    class Meta:
        name = "issue"
        namespace = "http://www.crossref.org/schema/5.3.1"

    value: str = field(
        default="",
        metadata={
            "min_length": 1,
            "max_length": 32,
        },
    )
