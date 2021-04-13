from dataclasses import dataclass, field
from typing import List, Optional, Union
from xsdata.models.datatype import XmlDateTime


@dataclass
class Cores:
    class Meta:
        name = "cores"

    core_serial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    flight: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    block: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    gridfins: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    legs: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    reused: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    land_success: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    landing_intent: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    landing_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    landing_vehicle: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Fairings:
    class Meta:
        name = "fairings"

    reused: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recovery_attempt: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    recovered: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    ship: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class LaunchFailureDetails:
    class Meta:
        name = "launch_failure_details"

    time: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    altitude: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    reason: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class LaunchSite:
    class Meta:
        name = "launch_site"

    site_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    site_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    site_name_long: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Links:
    class Meta:
        name = "links"

    mission_patch: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mission_patch_small: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    reddit_campaign: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    reddit_launch: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    reddit_recovery: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    reddit_media: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    presskit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    article_link: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    wikipedia: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    video_link: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    youtube_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    flickr_images: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class OrbitParams:
    class Meta:
        name = "orbit_params"

    reference_system: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    regime: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    longitude: Optional[Union[float, int]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    semi_major_axis_km: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    eccentricity: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    periapsis_km: Optional[Union[int, float]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    apoapsis_km: Optional[Union[int, float]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    inclination_deg: Optional[Union[int, float]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    period_min: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    lifespan_years: Optional[Union[int, float]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    epoch: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mean_motion: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    raan: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    arg_of_pericenter: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mean_anomaly: Optional[float] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Reuse:
    class Meta:
        name = "reuse"

    core: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    side_core1: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    side_core2: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fairings: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    capsule: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Telemetry:
    class Meta:
        name = "telemetry"

    flight_club: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Timeline:
    class Meta:
        name = "timeline"

    webcast_liftoff: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    webcast_launch: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    go_for_prop_loading: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    stage1_rp1_loading: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    rp1_loading: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    stage1_lox_loading: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    stage2_rp1_loading: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    stage2_lox_loading: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    engine_chill: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    prelaunch_checks: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    propellant_pressurization: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    go_for_launch: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    ignition: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    liftoff: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    maxq: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    beco: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    stage_sep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    side_core_sep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    side_core_boostback: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    dragon_separation: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    first_stage_landing: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    first_stage_boostback_burn: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    meco: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    first_stage_entry_burn: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    center_stage_sep: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    dragon_solar_deploy: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    first_stage_landing_burn: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    second_stage_ignition: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    dragon_bay_door_deploy: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payload_deploy_1: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    center_core_boostback: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fairing_deploy: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payload_deploy_2: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    side_core_entry_burn: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    seco_1: Optional[int] = field(
        default=None,
        metadata={
            "name": "seco-1",
            "type": "Element",
        }
    )
    side_core_landing: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    center_core_entry_burn: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    center_core_landing: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payload_deploy: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    second_stage_restart: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    seco_2: Optional[int] = field(
        default=None,
        metadata={
            "name": "seco-2",
            "type": "Element",
        }
    )
    seco_3: Optional[int] = field(
        default=None,
        metadata={
            "name": "seco-3",
            "type": "Element",
        }
    )
    seco_4: Optional[int] = field(
        default=None,
        metadata={
            "name": "seco-4",
            "type": "Element",
        }
    )


@dataclass
class FirstStage:
    class Meta:
        name = "first_stage"

    cores: List[Cores] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Payloads:
    class Meta:
        name = "payloads"

    payload_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    norad_id: List[int] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    cap_serial: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    reused: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    customers: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    nationality: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    manufacturer: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payload_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payload_mass_kg: Optional[Union[int, float]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payload_mass_lbs: Optional[Union[int, float]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orbit: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    orbit_params: Optional[OrbitParams] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    uid: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mass_returned_kg: Optional[Union[int, float]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mass_returned_lbs: Optional[Union[int, float]] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    flight_time_sec: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    cargo_manifest: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class SecondStage:
    class Meta:
        name = "second_stage"

    block: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    payloads: List[Payloads] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Rocket:
    class Meta:
        name = "rocket"

    rocket_id: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    rocket_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    rocket_type: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    first_stage: Optional[FirstStage] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    second_stage: Optional[SecondStage] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    fairings: Optional[Fairings] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )


@dataclass
class Launches:
    class Meta:
        name = "launches"

    flight_number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mission_name: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    mission_id: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    launch_year: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    launch_date_unix: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    launch_date_utc: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    launch_date_local: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    is_tentative: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tentative_max_precision: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    tbd: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    launch_window: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    rocket: Optional[Rocket] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    ships: List[str] = field(
        default_factory=list,
        metadata={
            "type": "Element",
        }
    )
    telemetry: Optional[Telemetry] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    reuse: Optional[Reuse] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    launch_site: Optional[LaunchSite] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    launch_success: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    launch_failure_details: Optional[LaunchFailureDetails] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    links: Optional[Links] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    details: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    upcoming: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    static_fire_date_utc: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    static_fire_date_unix: Optional[int] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    timeline: Optional[Timeline] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    crew: Optional[object] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    last_date_update: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    last_ll_launch_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    last_ll_update: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    last_wiki_launch_date: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    last_wiki_revision: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    last_wiki_update: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
    launch_date_source: Optional[str] = field(
        default=None,
        metadata={
            "type": "Element",
        }
    )
