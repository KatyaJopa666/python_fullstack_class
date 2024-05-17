def convert_to_hex(rgb_input):
    hex_color: int = '#'
    for i in rgb_input:
        if i == 0:
            hex_color += '00'
        else:
            hex_color += '%X' % i
    print(f'HEX: {hex_color}')

convert_to_hex((255, 0, 0))
convert_to_hex((0, 255, 0))
convert_to_hex((0, 0, 255))