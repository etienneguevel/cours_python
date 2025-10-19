import dataclasses
from dataclasses import dataclass

@dataclass(frozen=True)
class Coordinates:
	lat: float
	lon: float
	
	def __str__(self):
		return f"Coordinate : {self.lat} | {self.lon}"
	
Paris = Coordinates(48.51, 2.21)
print(Paris)
print(dataclasses.asdict(Paris))