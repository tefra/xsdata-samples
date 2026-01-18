from __future__ import annotations

from dataclasses import dataclass

from sdmx_ml.models.generic_metadata_type import GenericMetadataType

__NAMESPACE__ = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"


@dataclass(frozen=True, kw_only=True)
class GenericMetadata(GenericMetadataType):
    """
    GenericMetadata contains reported metadata in a format which supports
    any metadata structure definition.
    """

    class Meta:
        namespace = "http://www.sdmx.org/resources/sdmxml/schemas/v3_0/message"
