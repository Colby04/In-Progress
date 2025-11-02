"""A simple Python Utility demo for clean and modular code """

from datetime import datetime

class Shipment:
    def __init__(self, id, destination, weight, start_time, delivery_time):
        self.id = id
        self.destination = destination
        self.weight = weight
        self.start_time = start_time
        self.delivery_time = delivery_time
        self.shipped_date = None

    def ship(self):
        self.shipped_date = datetime.now()
        print(f"Shipment {self.id} to {self.destination} of weight {self.weight}kg shipped on {self.shipped_date}")

    def tracking_info(self):
        if self.shipped_date:
            return f"Shipment {self.id} to {self.destination} shipped on {self.shipped_date}"
        else:
            return "Shipment not yet shipped."

    def delivery_duration(self):
        duration = self.delivery_time - self.start_time
        return round(duration.total_seconds() / 3600, 2)


def average_delivery_time(shipments):
    if not shipments:
        return 0.0
    total = sum([shipment.delivery_duration() for shipment in shipments])
    return round(total / len(shipments), 2)

if __name__ == "__main__":
    s1 = Shipment("SHP001", "Birmingham", 10.5, datetime(2025, 10, 30, 9, 0), datetime(2025, 10, 30, 13, 30))
    s2 = Shipment("SHP002", "New York", 5.0, datetime(2025, 10, 30, 10, 0), datetime(2025, 10, 30, 15, 0))
    s3 = Shipment("SHP003", "California", 7.25, datetime(2025, 10, 30, 8, 30), datetime(2025, 10, 30, 12, 15))

    shipments = [s1, s2, s3]
    avg = average_delivery_time(shipments)

    print(f"Average delivery time: {avg} hours")