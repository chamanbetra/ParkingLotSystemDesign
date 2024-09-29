from helper import Helper
from solution import Solution

def main():
    helper = Helper()

    parking = [
        [
            [4, 4, 2, 2],
            [2, 4, 2, 0],
            [0, 2, 2, 2],
            [4, 4, 4, 0]
        ]
    ]

    solution = Solution()
    solution.init(helper, parking)

    #Testing for strategy 0 (lowest index)
    spot_id1 = solution.park(2, "bh234", "tkt4534", 0)
    helper.println(f"Vehicle parked at: {spot_id1}")

    #Testing for strategy 0 lowest index - 4 wheeler
    spot_id2 = solution.park(4, "bmw567", "tkt5678", 0)
    helper.println(f"Vehicle parked at: {spot_id2}")

    #test search for vehicle using vehicle number
    search_result = solution.searchVehicle("bh234")
    helper.println(f"Search result for vehicle 'bh234': {search_result}")

    # Test searching for a vehicle using ticket ID
    search_result_ticket = solution.searchVehicle("tkt4534")
    helper.println(f"Search result for ticket 'tkt4534': {search_result_ticket}")

    # Test removing a vehicle
    remove_result = solution.removeVehicle(spot_id1)
    helper.println(f"Vehicle removed from spot {spot_id1}: {remove_result}")

    # Test getting free spots count for 2-wheeler on floor 0
    free_spots_count = solution.getFreeSpotsCount(0, 2)
    helper.println(f"Free 2-wheeler spots on floor 0: {free_spots_count}")

if __name__ == "__main__":
    main()