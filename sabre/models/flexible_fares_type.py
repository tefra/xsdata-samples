from __future__ import annotations

from dataclasses import dataclass, field

from sabre.models.cabin_type import CabinType
from sabre.models.jump_cabin_logic_type import JumpCabinLogicType
from sabre.models.keep_same_cabin_type import KeepSameCabinType
from sabre.models.passenger_type_quantity_type import PassengerTypeQuantityType

__NAMESPACE__ = "http://www.opentravel.org/OTA/2003/05"


@dataclass(kw_only=True)
class FlexibleFaresType:
    """
    Attributes:
        fare_parameters: This element specifies parameters for desired
            fare.
    """

    fare_parameters: list[FlexibleFaresType.FareParameters] = field(
        default_factory=list,
        metadata={
            "name": "FareParameters",
            "type": "Element",
            "namespace": "http://www.opentravel.org/OTA/2003/05",
            "min_occurs": 1,
            "max_occurs": 10,
        },
    )

    @dataclass(kw_only=True)
    class FareParameters:
        """
        Attributes:
            exclude_restricted: Setting this to true means the same as
                setting ResTicketing, MinMaxStay and RefundPenalty to
                false.
            res_ticketing: If set to true, fares that have a
                reservation/ticketing can be included in the responses.
                If set to false, then no fares that include
                reservation/ticketing requirement will be included in
                the response. This is negation of XA qualifier.
            min_max_stay: If set to true, fares that have a min/max stay
                can be included in the responses. If set to false, then
                no fares that include a min/max stay requirement will be
                included in the response. This is negation of XS
                qualifier.
            refund_penalty: If set to true, fares that have a refund
                penalty can be included in the responses. If set to
                false, then no fares that include a refund penalty
                requirement will be included in the response. This is
                negation of XP qualifier.
            public_fare: This element finds only public fares.
            private_fare: This element finds only private fares.
            cabin: This element specifies preffered cabin type.
            passenger_type: This element specifies PTC used to find this
                fare.
            negotiated_fares_only: If set to true then returned fares
                need to match AcccountCode/CorpID specified in Fare
                Group definition on all fare components.
            xofares: If set to true only fares matching PTC specified in
                the Flex Fare Group will be returned on all fare
                components.
            passenger_type_quantity: Define information on the number of
                passengers of a specific type.
            jump_cabin_logic:
            keep_same_cabin:
            corporate_id:
            account_code:
        """

        exclude_restricted: (
            None | FlexibleFaresType.FareParameters.ExcludeRestricted
        ) = field(
            default=None,
            metadata={
                "name": "ExcludeRestricted",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        res_ticketing: None | FlexibleFaresType.FareParameters.ResTicketing = (
            field(
                default=None,
                metadata={
                    "name": "ResTicketing",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        min_max_stay: None | FlexibleFaresType.FareParameters.MinMaxStay = (
            field(
                default=None,
                metadata={
                    "name": "MinMaxStay",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        refund_penalty: (
            None | FlexibleFaresType.FareParameters.RefundPenalty
        ) = field(
            default=None,
            metadata={
                "name": "RefundPenalty",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        public_fare: None | FlexibleFaresType.FareParameters.PublicFare = (
            field(
                default=None,
                metadata={
                    "name": "PublicFare",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        private_fare: None | FlexibleFaresType.FareParameters.PrivateFare = (
            field(
                default=None,
                metadata={
                    "name": "PrivateFare",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        cabin: None | FlexibleFaresType.FareParameters.Cabin = field(
            default=None,
            metadata={
                "name": "Cabin",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        passenger_type: (
            None | FlexibleFaresType.FareParameters.PassengerType
        ) = field(
            default=None,
            metadata={
                "name": "PassengerType",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        negotiated_fares_only: (
            None | FlexibleFaresType.FareParameters.NegotiatedFaresOnly
        ) = field(
            default=None,
            metadata={
                "name": "NegotiatedFaresOnly",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        xofares: None | FlexibleFaresType.FareParameters.Xofares = field(
            default=None,
            metadata={
                "name": "XOFares",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        passenger_type_quantity: list[PassengerTypeQuantityType] = field(
            default_factory=list,
            metadata={
                "name": "PassengerTypeQuantity",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
                "max_occurs": 4,
            },
        )
        jump_cabin_logic: None | JumpCabinLogicType = field(
            default=None,
            metadata={
                "name": "JumpCabinLogic",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        keep_same_cabin: None | KeepSameCabinType = field(
            default=None,
            metadata={
                "name": "KeepSameCabin",
                "type": "Element",
                "namespace": "http://www.opentravel.org/OTA/2003/05",
            },
        )
        corporate_id: list[FlexibleFaresType.FareParameters.CorporateId] = (
            field(
                default_factory=list,
                metadata={
                    "name": "CorporateID",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )
        account_code: list[FlexibleFaresType.FareParameters.AccountCode] = (
            field(
                default_factory=list,
                metadata={
                    "name": "AccountCode",
                    "type": "Element",
                    "namespace": "http://www.opentravel.org/OTA/2003/05",
                },
            )
        )

        @dataclass(kw_only=True)
        class ExcludeRestricted:
            ind: bool = field(
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class ResTicketing:
            ind: bool = field(
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class MinMaxStay:
            ind: bool = field(
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class RefundPenalty:
            ind: bool = field(
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class PublicFare:
            ind: bool = field(
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class PrivateFare:
            ind: bool = field(
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class Cabin:
            type_value: CabinType = field(
                metadata={
                    "name": "Type",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class PassengerType:
            """
            Attributes:
                code: Specify traveler type code.
            """

            code: str = field(
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 8,
                }
            )

        @dataclass(kw_only=True)
        class NegotiatedFaresOnly:
            ind: bool = field(
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class Xofares:
            ind: bool = field(
                metadata={
                    "name": "Ind",
                    "type": "Attribute",
                    "required": True,
                }
            )

        @dataclass(kw_only=True)
        class CorporateId:
            code: str = field(
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "pattern": r"[A-Za-z]{3}[0-9]{2}",
                }
            )

        @dataclass(kw_only=True)
        class AccountCode:
            code: str = field(
                metadata={
                    "name": "Code",
                    "type": "Attribute",
                    "required": True,
                    "min_length": 1,
                    "max_length": 20,
                }
            )
