from dataclasses import dataclass


@dataclass
class Neighborhood:
    name: str
    population: int
    area_km2: float
    latitude: float
    longitude: float


