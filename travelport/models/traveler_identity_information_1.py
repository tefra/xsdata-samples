from __future__ import annotations
from dataclasses import dataclass, field
from travelport.models.type_key_element_1 import TypeKeyElement1
from travelport.models.type_masked_1 import TypeMasked1

__NAMESPACE__ = "http://www.travelport.com/schema/sharedUprofile_v20_0"


@dataclass
class TravelerIdentityInformation1(TypeKeyElement1):
    """An additional means to identify or verify a travelers profile when then are
    duplicate traveler names.

    Security Questions and answers must come in pairs.

    Parameters
    ----------
    secondary_id_code
        A Secondary Identification Code could be used to further
        verification of a Traveler’s profile when there are duplicate names.
        The Secondary Identification Code could be partially masked and case
        sensitive. If masking is requested, Secondary identification code is
        required.
    mask_secondary_id_code
        Indicator to specify if the secondary ID code is to be masked or not
        and if so how.
    security_question1
        If the Security Question is transmitted then the Corresponding
        Security Answer is required.
    security_answer1
        If the Security Answer is transmitted then the corresponding
        Security Question is required.
    security_question2
        If the Security Question is transmitted then the Corresponding
        Security Answer is required.
    security_answer2
        If the Security Answer is transmitted then the corresponding
        Security Question is required.
    """

    class Meta:
        name = "TravelerIdentityInformation"
        namespace = "http://www.travelport.com/schema/sharedUprofile_v20_0"

    secondary_id_code: None | str = field(
        default=None,
        metadata={
            "name": "SecondaryIdCode",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 50,
        },
    )
    mask_secondary_id_code: None | TypeMasked1 = field(
        default=None,
        metadata={
            "name": "MaskSecondaryIdCode",
            "type": "Attribute",
        },
    )
    security_question1: None | str = field(
        default=None,
        metadata={
            "name": "SecurityQuestion1",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    security_answer1: None | str = field(
        default=None,
        metadata={
            "name": "SecurityAnswer1",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    security_question2: None | str = field(
        default=None,
        metadata={
            "name": "SecurityQuestion2",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
    security_answer2: None | str = field(
        default=None,
        metadata={
            "name": "SecurityAnswer2",
            "type": "Attribute",
            "min_length": 1,
            "max_length": 128,
        },
    )
