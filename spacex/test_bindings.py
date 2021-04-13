from pathlib import Path
from typing import List

from xsdata.formats.dataclass.parsers import JsonParser
from xsdata.formats.dataclass.serializers import JsonSerializer
from xsdata.models.datatype import XmlDateTime

from spacex.models import Cores
from spacex.models import Fairings
from spacex.models import FirstStage
from spacex.models import Launches
from spacex.models import LaunchFailureDetails
from spacex.models import LaunchSite
from spacex.models import Links
from spacex.models import OrbitParams
from spacex.models import Payloads
from spacex.models import Reuse
from spacex.models import Rocket
from spacex.models import SecondStage
from spacex.models import Telemetry
from spacex.models import Timeline

parser = JsonParser()
serializer = JsonSerializer(indent=4)
here = Path(__file__).parent


def test_parser():
    sample = here.joinpath("launches.json")
    launches = parser.from_path(sample, List[Launches])

    assert 109 == len(launches)

    expected = Launches(
        flight_number=1,
        mission_name="FalconSat",
        mission_id=[],
        launch_year=2006,
        launch_date_unix=1143239400,
        launch_date_utc=XmlDateTime(2006, 3, 24, 22, 30, 0, 0, 0),
        launch_date_local=XmlDateTime(2006, 3, 25, 10, 30, 0, 0, 720),
        is_tentative=False,
        tentative_max_precision="hour",
        tbd=False,
        launch_window=0,
        rocket=Rocket(
            rocket_id="falcon1",
            rocket_name="Falcon 1",
            rocket_type="Merlin A",
            first_stage=FirstStage(
                cores=[
                    Cores(
                        core_serial="Merlin1A",
                        flight=1,
                        gridfins=False,
                        legs=False,
                        reused=False,
                        landing_intent=False,
                    )
                ]
            ),
            second_stage=SecondStage(
                block=1,
                payloads=[
                    Payloads(
                        payload_id="FalconSAT-2",
                        norad_id=[],
                        reused=False,
                        customers=["DARPA"],
                        nationality="United States",
                        manufacturer="SSTL",
                        payload_type="Satellite",
                        payload_mass_kg=20,
                        payload_mass_lbs=43,
                        orbit="LEO",
                        orbit_params=OrbitParams(
                            reference_system="geocentric",
                            regime="low-earth",
                            periapsis_km=400,
                            apoapsis_km=500,
                            inclination_deg=39,
                        ),
                    )
                ],
            ),
            fairings=Fairings(reused=False, recovery_attempt=False, recovered=False),
        ),
        ships=[],
        telemetry=Telemetry(flight_club=None),
        reuse=Reuse(
            core=False,
            side_core1=False,
            side_core2=False,
            fairings=False,
            capsule=False,
        ),
        launch_site=LaunchSite(
            site_id="kwajalein_atoll",
            site_name="Kwajalein Atoll",
            site_name_long="Kwajalein Atoll Omelek Island",
        ),
        launch_success=False,
        launch_failure_details=LaunchFailureDetails(
            time=33, reason="merlin engine failure"
        ),
        links=Links(
            mission_patch="https://images2.imgbox.com/40/e3/GypSkayF_o.png",
            mission_patch_small="https://images2.imgbox.com/3c/0e/T8iJcSN3_o.png",
            article_link="https://www.space.com/2196-spacex-inaugural-falcon-1-rocket-lost-launch.html",
            wikipedia="https://en.wikipedia.org/wiki/DemoSat",
            video_link="https://www.youtube.com/watch?v=0a_00nJ_Y88",
            youtube_id="0a_00nJ_Y88",
            flickr_images=[],
        ),
        details="Engine failure at 33 seconds and loss of vehicle",
        upcoming=False,
        static_fire_date_utc=XmlDateTime(2006, 3, 17, 0, 0, 0, 0, 0),
        static_fire_date_unix=1142553600,
        timeline=Timeline(
            webcast_liftoff=54,
        ),
    )

    assert expected == launches[0]
