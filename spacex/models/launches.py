from dataclasses import dataclass, field
from dataclasses_jsonschema import JsonSchemaMixin
from typed_dataclass import typed_dataclass
from typing import List, Optional
from xsdata.models.datatype import XmlDateTime


@dataclass
@typed_dataclass
class Cores(JsonSchemaMixin):
    class Meta:
        name = "cores"

    core: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    flight: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    gridfins: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    legs: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    reused: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    landing_attempt: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    landing_success: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    landing_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    landpad: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
@typed_dataclass
class Failures(JsonSchemaMixin):
    class Meta:
        name = "failures"

    time: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    altitude: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
@typed_dataclass
class Fairings(JsonSchemaMixin):
    class Meta:
        name = "fairings"

    reused: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    recovery_attempt: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    recovered: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    ships: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
@typed_dataclass
class Flickr(JsonSchemaMixin):
    class Meta:
        name = "flickr"

    small: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    original: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )


@dataclass
@typed_dataclass
class Patch(JsonSchemaMixin):
    class Meta:
        name = "patch"

    small: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    large: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
@typed_dataclass
class Reddit(JsonSchemaMixin):
    class Meta:
        name = "reddit"

    campaign: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    launch: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    media: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    recovery: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
@typed_dataclass
class Links(JsonSchemaMixin):
    class Meta:
        name = "links"

    patch: Optional[Patch] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    reddit: Optional[Reddit] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    flickr: Optional[Flickr] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    presskit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    webcast: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    youtube_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    article: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    wikipedia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass
@typed_dataclass
class Launches(JsonSchemaMixin):
    class Meta:
        name = "launches"

    fairings: Optional[Fairings] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    links: Optional[Links] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    static_fire_date_utc: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    static_fire_date_unix: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    tbd: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    net: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    window: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    rocket: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    success: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    details: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    crew: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    ships: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    capsules: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    payloads: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    launchpad: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    auto_update: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    launch_library_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    failures: List[Failures] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    flight_number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    date_utc: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    date_unix: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    date_local: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    date_precision: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    upcoming: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    cores: List[Cores] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        }
    )
    id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
            "required": True,
        }
    )
