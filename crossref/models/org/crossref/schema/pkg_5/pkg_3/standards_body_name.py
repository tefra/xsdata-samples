from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.crossref.org/schema/5.3.1"


@dataclass(kw_only=True)
class StandardsBodyName:
    """
    Name of the standards organization / publisher.
    """

    class Meta:
        name = "standards_body_name"
        namespace = "http://www.crossref.org/schema/5.3.1"
