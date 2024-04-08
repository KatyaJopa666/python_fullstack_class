incoming_str: str = input()
string_middle: int = int(len(incoming_str) / 2)
result_str: str = incoming_str[string_middle:] + incoming_str[:string_middle]
print(result_str)