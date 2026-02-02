from strategy.wareHouseSelectionStrategy import WareHouseSelectionStrategy


class NearestWareHouseSelectionStrategy(WareHouseSelectionStrategy):

    def selectWareHouse(self, ware_house_list):
        if not ware_house_list:
            return "No wareHouse available for given location."
        print("list", ware_house_list)
        
        # // 🏗️ Future Scope: Implement actual distance calculation logic here
        # // 1️⃣ Get the user's location (latitude, longitude).
        # // 2️⃣ Use Haversine Formula OR Google Maps API to calculate distance between user & warehouses.
        # // 3️⃣ Select the warehouse with the shortest distance.

        for warehouse_id, warehouse in ware_house_list.items(): # dummy selection for now
            return warehouse