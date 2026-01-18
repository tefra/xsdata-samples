from dataclasses import dataclass, field
from typing import Optional

from typed_dataclass import typed_dataclass
from xsdata.models.datatype import XmlDateTime

from spacex.mixins import DictMixin


@dataclass
@typed_dataclass
class Cores(DictMixin):
    class Meta:
        name = "cores"

    core: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    flight: int | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gridfins: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    legs: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reused: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    landing_attempt: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    landing_success: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    landing_type: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    landpad: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
@typed_dataclass
class Failures(DictMixin):
    class Meta:
        name = "failures"

    time: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    altitude: int | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reason: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )


@dataclass
@typed_dataclass
class Fairings(DictMixin):
    class Meta:
        name = "fairings"

    reused: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    recovery_attempt: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    recovered: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    ships: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
@typed_dataclass
class Flickr(DictMixin):
    class Meta:
        name = "flickr"

    small: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    original: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )


@dataclass
@typed_dataclass
class Patch(DictMixin):
    class Meta:
        name = "patch"

    small: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    large: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
@typed_dataclass
class Reddit(DictMixin):
    class Meta:
        name = "reddit"

    campaign: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    launch: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    media: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    recovery: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
@typed_dataclass
class Links(DictMixin):
    class Meta:
        name = "links"

    patch: Patch | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    reddit: Reddit | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    flickr: Flickr | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    presskit: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    webcast: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    youtube_id: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    article: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    wikipedia: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass
@typed_dataclass
class Launches(DictMixin):
    class Meta:
        name = "launches"

    fairings: Fairings | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    links: Links | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    static_fire_date_utc: XmlDateTime | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    static_fire_date_unix: int | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tbd: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    net: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    window: int | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rocket: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    success: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    details: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    crew: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    ships: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    capsules: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    payloads: list[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    launchpad: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    auto_update: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    launch_library_id: str | None = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    failures: list[Failures] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        },
    )
    flight_number: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    name: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    date_utc: XmlDateTime | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    date_unix: int | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    date_local: XmlDateTime | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    date_precision: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    upcoming: bool | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
    cores: list[Cores] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: str | None = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        },
    )
