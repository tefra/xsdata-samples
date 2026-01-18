from __future__ import annotations

from dataclasses import dataclass, field

from npo.models.image_type_enum import ImageTypeEnum
from npo.models.license_enum import LicenseEnum

__NAMESPACE__ = "urn:vpro:pages:2013"


@dataclass(kw_only=True)
class ImageType2:
    class Meta:
        name = "imageType"

    title: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    description: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    credits: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    source: None | str = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    source_name: None | str = field(
        default=None,
        metadata={
            "name": "sourceName",
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    license: None | LicenseEnum = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "urn:vpro:pages:2013",
        },
    )
    type_value: None | ImageTypeEnum = field(
        default=None,
        metadata={
            "name": "type",
            "type": "Attribute",
        },
    )
    url: None | str = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
