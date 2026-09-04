from src.city import Neighborhood


def test_neighborhood_creation():
    neighborhood = Neighborhood(
        name="Central",
        population=150000,
        area_km2=12.5,
        latitude=28.46,
        longitude=77.03,
    )

    assert neighborhood.name == "Central"
    assert neighborhood.population == 150000