import pytest
from src.volume import calculate_volume_cube

def test_calculate_volume_cube():
    assert calculate_volume_cube(2) == 8
    assert calculate_volume_cube(2.5) == 15.625

def test_calculate_volume_cube_negative():
    with pytest.raises(TypeError):
        calculate_volume_cube(-2)

def test_calculate_volume_cube_string():
    with pytest.raises(TypeError):
        calculate_volume_cube("2")

def test_calculate_volume_cube_list():
    with pytest.raises(TypeError):
        calculate_volume_cube([2])
        
