class InventorySystem:
    def __init__(self) -> None:
        self.items: dict[str, int] = {"wood": 0, "meat": 0}

    def add_item(self, item: str, amount: int = 1) -> None:
        self.items[item] = self.items.get(item, 0) + amount
