import re

def calculator(input_data) -> float:
    if isinstance(input_data, str):
        # Try to parse simple math string like "7 * 3" or "12.5 / 5"
        pattern = r'^\s*([-+]?\d*\.?\d+)\s*([\+\-\*/])\s*([-+]?\d*\.?\d+)\s*$'
        match = re.match(pattern, input_data)
        if not match:
            raise ValueError(f"Invalid input format: '{input_data}'")
        a = float(match.group(1))
        operator = match.group(2)
        b = float(match.group(3))

        operation_map = {
            '+': 'add',
            '-': 'subtract',
            '*': 'multiply',
            '/': 'divide'
        }
        operation = operation_map.get(operator)
    elif isinstance(input_data, dict):
        # Structured JSON-style input
        a = float(input_data["a"])
        b = float(input_data["b"])
        operation = input_data["operation"]
    else:
        raise TypeError("Input must be a string or a dictionary.")

    # Execute operation
    if operation == 'add':
        return a + b
    elif operation == 'subtract':
        return a - b
    elif operation == 'multiply':
        return a * b
    elif operation == 'divide':
        return a / b if b != 0 else float('inf')
    else:
        raise ValueError(f"Unsupported operation: {operation}")
