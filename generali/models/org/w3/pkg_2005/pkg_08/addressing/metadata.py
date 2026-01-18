from __future__ import annotations

from dataclasses import dataclass

from generali.models.org.w3.pkg_2005.pkg_08.addressing.metadata_type import (
    MetadataType,
)

__NAMESPACE__ = "http://www.w3.org/2005/08/addressing"


@dataclass(kw_only=True)
class Metadata(MetadataType):
    class Meta:
        namespace = "http://www.w3.org/2005/08/addressing"
