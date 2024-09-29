from Strategies import LowestIndexStrategy, MaxFreeSpotsStrategy
class Solution:

    def __init__(self):
        self.parking = []
        self.vehicles = {}
        self.helper = None
        self.spot_map = {}

    def init(self, helper, parking):
        self.parking = parking
        self.helper = helper

        for floor in range(len(parking)):
            for row in range(len(parking[floor])):
                for column in range(len(parking[floor][row])):
                    if parking[floor][row][column] in (2, 4): # 2 or 4 wheeler
                        spot_id = f"{floor}-{row}-{column}"
                        self.spot_map[spot_id] = {
                            "type": parking[floor][row][column],
                            "occupied": False,
                            "vehicle_number": None,
                            "ticket_id": None,
                        }

    def park(self, vehicle_type, vehicle_number, ticket_id, parking_strategy):
        strategy = None
        if parking_strategy == 0:
            strategy = LowestIndexStrategy()
        elif parking_strategy == 1:
            strategy = MaxFreeSpotsStrategy()
        else:
            self.helper.println("Invalid parking strategy!")
            return ""
        
        #find a parkign spot
        spot_id = strategy.find_parking_spot(self.spot_map, vehicle_type)

        if spot_id:
            #parking the vehicle
            self.spot_map[spot_id]['occupied']         = True
            self.spot_map[spot_id]['vehicle_number']   = vehicle_number
            self.spot_map[spot_id]['ticket_id']        = ticket_id
            self.vehicles[vehicle_number]              = vehicle_number
            self.vehicles[ticket_id]                   = ticket_id
            self.helper.println(f"Parked vehicle {vehicle_number} at {spot_id}")
            return spot_id
        
        self.helper.println("No available parking spot.")
        return ""

    def removeVehicle(self, spot_id):
        if spot_id in self.spot_map and self.spot_map[spot_id]['occupied']:
            #unparking the vehicle
            self.spot_map[spot_id]['occupied']         = False
            vehicle_number                             = self.spot_map[spot_id]['vehicle_number'] 
            ticket_id                                  = self.spot_map[spot_id]['ticket_id']
            self.vehicles[vehicle_number]              = None
            self.vehicles[ticket_id]                   = None

            #need to remove vehicle info from mapping
            if vehicle_number in self.vehicles:
                del self.vehicles[vehicle_number]
            if ticket_id in self.vehicles:
                del self.vehicles[ticket_id]

            self.helper.println(f"Removed vehicle from {spot_id}")
            return True
        
        self.helper.println("Vehicles not found or already removed")
        return False
    
    def searchVehicle(self, query):
        return self.vehicles.get(query, "")
    
    def getFreeSpotsCount(self, floor, vehicle_type):
        if 0 <= floor < len(self.parking):
            return sum(1 for spot_id, details in self.spot_map.items() 
                       if details['type'] == vehicle_type and not details['occupied'] and spot_id.startswith(str(floor)))
        return 0




    
