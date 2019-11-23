generate:
	xsdata generate xsd/travelport/air_v48_0/AirReqRsp.xsd --package samples.travelport.air_v48_0
	xsdata generate xsd/amadeus/Fare_MasterPricerTravelBoardSearch_15_3_1A.xsd --package samples.amadeus

print:
	xsdata generate xsd/travelport/air_v48_0/AirReqRsp.xsd --package samples.travelport.air_v48_0 --print > ./print.txt