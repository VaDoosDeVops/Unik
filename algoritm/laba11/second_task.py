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


def get_volume_calculator(figure_name):
    calculators = {
        "куб": calculate_cube_volume,
        "сфера": calculate_sphere_volume,
        "пирамида": calculate_pyramid_volume,
        "цилиндр": calculate_cylinder_volume
    }
    return calculators.get(figure_name.lower())

def process_user_input():
    figure = input("Введите название фигуры (куб, сфера, пирамида, цилиндр): ")
    calculator = get_volume_calculator(figure)
    
    if not calculator:
        print("Неизвестная фигура")
        return
    
    params = {
        "куб": {"side": float(input("Введите длину стороны: "))},
        "сфера": {"radius": float(input("Введите радиус: "))},
        "пирамида": {
            "base_length": float(input("Введите длину основания: ")),
            "base_width": float(input("Введите ширину основания: ")),
            "height": float(input("Введите высоту: "))
        },
        "цилиндр": {
            "radius": float(input("Введите радиус: ")),
            "height": float(input("Введите высоту: "))
        }
    }
    
    result = calculator(**params[figure.lower()])
    print(f"Объем {figure}: {result:.2f}")
