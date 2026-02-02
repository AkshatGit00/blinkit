from abc import ABC, abstractmethod
from typing import Dict
from models.warehouse import WareHouse

class WareHouseSelectionStrategy(ABC):

    @abstractmethod
    def selectWareHouse(self, ware_house_list:Dict[str, WareHouse]):
        pass