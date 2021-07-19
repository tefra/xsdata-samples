from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass
class AssociationName:
    class Meta:
        name = "associationName"
        namespace = "http://www.opengis.net/gml/3.2"

    value: Optional[str] = field(
        default=None
    )
