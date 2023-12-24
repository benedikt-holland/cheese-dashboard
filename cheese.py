import pandas as pd

TEMPERATURE = 13
HUMIDITY = 94

class Cheese():
    def __init__(self, filename="Käsekammer.csv") -> None:
        data = pd.read_csv("Käsekammer.csv")
        data.time = pd.to_datetime(data.time)
        self.humidity = data[data["variable"] == "Humditiy"][["time", "value"]].set_index("time")
        self.temperature = data[data["variable"] == "Temperature"][["time", "value"]].set_index("time")
        