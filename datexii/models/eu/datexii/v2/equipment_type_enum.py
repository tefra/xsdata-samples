from enum import Enum

__NAMESPACE__ = "http://datex2.eu/schema/2/2_0"


class EquipmentTypeEnum(Enum):
    """
    Equipment available on the parking or parking space or grouped parking spaces.

    :cvar TOILET: Indicates, whether there are toilets available.
    :cvar SHOWER: Indicates, whether there are shower facilities
        available.
    :cvar INFORMATION_POINT: An information point with employees.
    :cvar INFORMATON_STELE: An unmanned information point.
    :cvar INTERNET_TERMINAL: Public internet terminal. Charges may be
        specified using the TariffsAndPayment section.
    :cvar INTERNET_WIRELESS: Public wireless internet. Specifying an
        amount would be the number of hotspots/access points. Charges
        may be specified using the TariffsAndPayment section.
    :cvar PAY_DESK: A possibility to pay for parking (with employees).
    :cvar PAYMENT_MACHINE: A parking ticket machine.
    :cvar CASH_MACHINE: Cash machine.
    :cvar VENDING_MACHINE: A vending machine for snacks, coffee etc.
        (without manpower).
    :cvar FAX_MACHINE_OR_SERVICE: A possibility to send and/or receive
        faxes.
    :cvar COPY_MACHINE_OR_SERVICE: A possibility to create copies of
        documents.
    :cvar SAFE_DEPOSIT: A possibility to store valuable possession in a
        safe way.
    :cvar LUGGAGE_LOCKER: Possibility to deposit luggage in a safe way.
    :cvar PUBLIC_PHONE: Indicates, whether there's a public telephone
        available.
    :cvar PUBLIC_COIN_PHONE: Indicates, whether there's a public
        telephone available that can be used with coins.
    :cvar PUBLIC_CARD_PHONE: Indicates, whether there's a public
        telephone available that can be used with a card.
    :cvar ELEVATOR: Indication of the availability of elevators.
    :cvar PICNIC_FACILITIES: Indication of whether any picnicking
        facilities, such as tables, chairs and shaded areas, are
        available.
    :cvar DUMPING_STATION: Possibility to get rid of sewerage
        (especially for motorhomes).
    :cvar FRESH_WATER: Possibility to get fresh water (e.g. for
        motorhomes) - toilets and showers etc. are not intended here.
    :cvar WASTE_DISPOSAL: Possibility to get rid of waste in a legal way
        (e.g. for truckers or motorhomes). Normal refuse bins are not
        intended here.
    :cvar REFUSE_BIN: Refuse bins for small amounts of garbage (see also
        'wasteDisposal').
    :cvar ICE_FREE_SCAFFOLD: A technical equipment to remove ice and
        snow from the roof of lorries.
    :cvar PLAYGROUND: A playground for children.
    :cvar ELECTRIC_CHARGING_STATION: For charging vehicles, motorhome
        supply etc. The 'numberOf...' attribute specifies the number of
        charging stations. You may specify the number of charging points
        and further information with component 'ElectricCharging'.
    :cvar BIKE_PARKING: Bike parking.
    :cvar TOLL_TERMINAL: A terminal, where toll charges can be paid
        manually (this does not mean a toll gate on the road)
    :cvar DEFIBRILLATOR: Medical equipment to provide first aid after
        heart attacks.
    :cvar FIRST_AID_EQUIPMENT: Equipment to support first aid on injured
        people. Note that 'defibrillator' is a separate literal.
    :cvar FIRE_HOSE: A hose for water transport in case of fire.
    :cvar FIRE_EXTINGIUSHER: Fire extinguisher
    :cvar FIRE_HYDRANT: Fire hydrant
    :cvar NONE: None.
    :cvar UNKNOWN: Unknown.
    :cvar OTHER: Some other equipment. Use
        'otherEquipmentOrServiceFacility' to specify it.
    """

    TOILET = "toilet"
    SHOWER = "shower"
    INFORMATION_POINT = "informationPoint"
    INFORMATON_STELE = "informatonStele"
    INTERNET_TERMINAL = "internetTerminal"
    INTERNET_WIRELESS = "internetWireless"
    PAY_DESK = "payDesk"
    PAYMENT_MACHINE = "paymentMachine"
    CASH_MACHINE = "cashMachine"
    VENDING_MACHINE = "vendingMachine"
    FAX_MACHINE_OR_SERVICE = "faxMachineOrService"
    COPY_MACHINE_OR_SERVICE = "copyMachineOrService"
    SAFE_DEPOSIT = "safeDeposit"
    LUGGAGE_LOCKER = "luggageLocker"
    PUBLIC_PHONE = "publicPhone"
    PUBLIC_COIN_PHONE = "publicCoinPhone"
    PUBLIC_CARD_PHONE = "publicCardPhone"
    ELEVATOR = "elevator"
    PICNIC_FACILITIES = "picnicFacilities"
    DUMPING_STATION = "dumpingStation"
    FRESH_WATER = "freshWater"
    WASTE_DISPOSAL = "wasteDisposal"
    REFUSE_BIN = "refuseBin"
    ICE_FREE_SCAFFOLD = "iceFreeScaffold"
    PLAYGROUND = "playground"
    ELECTRIC_CHARGING_STATION = "electricChargingStation"
    BIKE_PARKING = "bikeParking"
    TOLL_TERMINAL = "tollTerminal"
    DEFIBRILLATOR = "defibrillator"
    FIRST_AID_EQUIPMENT = "firstAidEquipment"
    FIRE_HOSE = "fireHose"
    FIRE_EXTINGIUSHER = "fireExtingiusher"
    FIRE_HYDRANT = "fireHydrant"
    NONE = "none"
    UNKNOWN = "unknown"
    OTHER = "other"
