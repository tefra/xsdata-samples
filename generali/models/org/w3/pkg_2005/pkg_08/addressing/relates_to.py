from dataclasses import dataclass

from generali.models.org.w3.pkg_2005.pkg_08.addressing.relates_to_type import (
    RelatesToType,
)

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass
class RelatesTo(RelatesToType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"
