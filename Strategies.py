from abc import ABC, abstractmethod

class ParkingStrategy(ABC):
    @abstractmethod
    def find_parking_spot(self, spot_map, vehicle_type):
        pass

class LowestIndexStrategy(ParkingStrategy):
    def find_parking_spot(self, spot_map, vehicle_type):
            # lowest floor
            for spot_id, details in sorted(spot_map.items()):
                  if details['type'] == vehicle_type and not details['occupied']:
                        return spot_id
            return None
    
class MaxFreeSpotsStrategy(ParkingStrategy):
      def find_parking_spot(self, spot_map, vehicle_type):
            
            #max free spots per floor

            max_free_spots = -1
            chosen_spot = None

            #counting free spots per floor 
            floor_free_counts = {}
            for spot_id, details in spot_map.items():
                  floor = int(spot_id.split('-')[0])
                  if details['type'] == vehicle_type and not details['occupied']:
                        floor_free_counts[floor] = floor_free_counts.get(floor, 0) + 1
            
            #finding floor with max spots left
            for floor, count in floor_free_counts.items():
                  if count > max_free_spots:
                        max_free_spots = count
                        chosen_spot = floor
            

            #in floor with max free spots, get lowest indexed spot
            if chosen_spot is not None:
                  for spot_id, details in spot_map.items():
                        if details['type'] == vehicle_type and not details['occupied'] and spot_id.startswith(str(chosen_spot)):
                              return spot_id
                        
            return None 