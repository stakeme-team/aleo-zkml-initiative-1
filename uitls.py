def get_leo_type(strType):
    leo_types = [
        'i8', 'i16', 'i32', 'i64', 'i128',
        'u8' 'u16', 'u32', 'u64', 'u128'
    ]
    for leo_type in leo_types:
        if strType.endswith(leo_type):
            return strType
    raise ValueError(f'Invalid input: {strType}')


def convert_to_leo_type(num, leo_type):
    max_values = {
        'i8': 127,
        'i16': 32767,
        'i32': 2147483647,
        'i64': 9223372036854775807,
        'i128': 170141183460469231731687303715884105727,
        'u8': 255,
        'u16': 65535,
        'u32': 4294967295,
        'u64': 18446744073709551615,
        'u128': 340282366920938463463374607431768211455
    }

    if leo_type not in max_values:
        raise ValueError(f'Invalid Leo type: {leo_type}')

    if num > max_values[leo_type]:
        raise ValueError(f'Number {num} exceeds maximum value for type {leo_type}')

    return f"{num}{leo_type}"


def convert_from_leo_type(num_str):
    max_values = {
        'i8': 127,
        'i16': 32767,
        'i32': 2147483647,
        'i64': 9223372036854775807,
        'i128': 170141183460469231731687303715884105727,
        'u8': 255,
        'u16': 65535,
        'u32': 4294967295,
        'u64': 18446744073709551615,
        'u128': 340282366920938463463374607431768211455
    }

    for leo_type in max_values:
        if num_str.endswith(leo_type):
            num = int(num_str[:-len(leo_type)])
            if num > max_values[leo_type]:
                raise ValueError(f'Number {num} exceeds maximum value for type {leo_type}')
            return num

    raise ValueError(f'Invalid Leo type in string: {num_str}')
