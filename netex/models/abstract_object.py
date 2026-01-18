from __future__ import annotations

from dataclasses import dataclass

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AbstractObject:
    class Meta:
        namespace = "http://www.opengis.net/gml/3.2"
