from typing import Dict
from models.warehouse import WareHouse
from strategy.wareHouseSelectionStrategy import WareHouseSelectionStrategy


class WareHouseService:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(WareHouseService, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        self.ware_houses:Dict[str, WareHouse] = {}

    def add_ware_house(self, ware_house:WareHouse):
        ware_house_id = ware_house.wareHouse_id
        if ware_house_id in self.ware_houses:
            return "This wareHouse is already registered."
        self.ware_houses[ware_house_id] = ware_house
        return "Registered Successfully."

    def remove_ware_house(self, ware_house_id:str):
        if ware_house_id not in self.ware_houses:
            return "This wareHouse is not present."
        del self.ware_houses[ware_house_id]

    def select_ware_house(self, selection_strategy:WareHouseSelectionStrategy):
        # this is dict, but func accepts list, correct it
        return selection_strategy.selectWareHouse(self.ware_houses)
