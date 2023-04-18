def weight_converter(weight, from_unit, to_unit):
    if from_unit == 'kg':
        weight_kg = weight
    elif from_unit == 'g':
        weight_kg = weight / 1000
    elif from_unit == 'lb':
        weight_kg = weight / 2.20462
    elif from_unit == 'oz':
        weight_kg = weight / 35.274

    if to_unit == 'kg':
        return round(weight_kg, 2)
    elif to_unit == 'g':
        return round(weight_kg * 1000, 2)
    elif to_unit == 'lb':
        return round(weight_kg * 2.20462, 2)
    elif to_unit == 'oz':
        return round(weight_kg * 35.274, 2)
