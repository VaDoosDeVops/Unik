import math

def calculate_cube_volume(side=1):
    """Расчет объема куба"""
    return side ** 3

def calculate_sphere_volume(radius=1):
    """Расчет объема сферы"""
    return (4/3) * math.pi * (radius ** 3)

def calculate_pyramid_volume(base_length=1, base_width=1, height=1):
    """Расчет объема пирамиды"""
    base_area = base_length * base_width
    return (1/3) * base_area * height

def calculate_cylinder_volume(radius=1, height=1):
    """Расчет объема цилиндра"""
    return math.pi * (radius ** 2) * height
