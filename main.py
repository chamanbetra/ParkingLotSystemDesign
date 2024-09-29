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

    spot_id = solution.park(2, "bh234", "tkt4534", 0)
    helper.println(f"Parked at: {spot_id}")

    search_result_vehicle_number = solution.searchVehicle("bh234")
    helper.println(f"Found by vehicle number: {search_result_vehicle_number}")

    search_result_ticket_id = solution.searchVehicle("tkt4534")
    helper.println(f"Found by ticket ID: {search_result_ticket_id}")

    free_spots_count = solution.getFreeSpotsCount(0, 2)
    helper.println(f"Free 2-wheeler spots before removal: {free_spots_count}")

    removal_status = solution.removeVehicle("0-0-2")
    helper.println(f"Vehicle removed: {removal_status}")

    free_spots_count_after_removal = solution.getFreeSpotsCount(0, 2)
    helper.println(f"Free 2-wheeler spots after removal: {free_spots_count_after_removal}")



if __name__ == "__main__":
    main()