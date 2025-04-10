def decimal_to_roman(decimal):
    """
    Convierte un número decimal a su representación en números romanos.
    
    Args:
        decimal (int): Un número entero entre 1 y 3999.
        
    Returns:
        str: Representación en números romanos del número decimal.
        
    Raises:
        ValueError: Si el número está fuera del rango válido (1-3999).
    """
    # Validar el rango
    if not isinstance(decimal, int) or decimal < 1 or decimal > 3999:
        raise ValueError("El número debe ser un entero entre 1 y 3999")
    
    # Valores y símbolos romanos ordenados de mayor a menor
    roman_values = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]
    
    roman_numeral = ""
    remaining = decimal
    
    # Construir el número romano
    for value, symbol in roman_values:
        # Añadir símbolos mientras el número sea mayor o igual al valor actual
        while remaining >= value:
            roman_numeral += symbol
            remaining -= value
    
    return roman_numeral