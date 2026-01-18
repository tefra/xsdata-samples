from __future__ import annotations

from dataclasses import dataclass, field

from typed_dataclass import typed_dataclass
from xsdata.models.datatype import XmlDateTime

from spacex.mixins import DictMixin


@dataclass(kw_only=True)
@typed_dataclass
class Cores(DictMixin):
    class Meta:
        name = "cores"

    core: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    flight: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    gridfins: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    legs: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reused: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    landing_attempt: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    landing_success: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    landing_type: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    landpad: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
@typed_dataclass
class Failures(DictMixin):
    class Meta:
        name = "failures"

    time: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    altitude: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    reason: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )


@dataclass(kw_only=True)
@typed_dataclass
class Fairings(DictMixin):
    class Meta:
        name = "fairings"

    reused: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    recovery_attempt: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    recovered: None | bool = field(
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


@dataclass(kw_only=True)
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


@dataclass(kw_only=True)
@typed_dataclass
class Patch(DictMixin):
    class Meta:
        name = "patch"

    small: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    large: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
@typed_dataclass
class Reddit(DictMixin):
    class Meta:
        name = "reddit"

    campaign: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    launch: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    media: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    recovery: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
@typed_dataclass
class Links(DictMixin):
    class Meta:
        name = "links"

    patch: Patch = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    reddit: Reddit = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    flickr: Flickr = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    presskit: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    webcast: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    youtube_id: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    article: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    wikipedia: None | str = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )


@dataclass(kw_only=True)
@typed_dataclass
class Launches(DictMixin):
    class Meta:
        name = "launches"

    fairings: None | Fairings = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    links: Links = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    static_fire_date_utc: None | XmlDateTime = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    static_fire_date_unix: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    tbd: bool = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    net: bool = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    window: None | int = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    rocket: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    success: None | bool = field(
        default=None,
        metadata={
            "type": "Element",
        },
    )
    details: None | str = field(
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
    launchpad: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    auto_update: bool = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    launch_library_id: None | str = field(
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
    flight_number: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    name: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    date_utc: XmlDateTime = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    date_unix: int = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    date_local: XmlDateTime = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    date_precision: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    upcoming: bool = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
    cores: list[Cores] = field(
        default_factory=list,
        metadata={
            "type": "Element",
            "min_occurs": 1,
        },
    )
    id: str = field(
        metadata={
            "type": "Element",
            "required": True,
        }
    )
