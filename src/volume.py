def calculate_volume_cube(length: int | float) -> int | float:
    """
    Function to calculate the volume of a cube
    :param length: edge length of a cube
    :return: volume of the cube
    """
    if not isinstance(length, (int, float)) or length <= 0:
        raise TypeError("Length must be a positive non-zero number")
    return length * length * length
