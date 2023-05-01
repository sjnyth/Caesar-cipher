import sys

def output_formatter(output):
    result_str = ''
    line_str = ''
    counter = 0
    for letter_char in output:
        line_str += letter_char
        counter += 1
        if counter == 5:
            result_str += line_str + ' '
            line_str = ''
            counter = 0
    if line_str:
        result_str += line_str + '\n'
    return result_str

def encode(text_str, move):
    letters = [char.upper() for char in text_str if char.isalpha()]
    encoded_list = []
    for char in letters:
        ascii_val = ord(char)
        new_val = ascii_val + move
        if new_val > ord('Z'):
            final_val = (new_val - ord('Z')) % 26
            if final_val == 0:
                final_val = 26
            new_val = final_val + ord('A') - 1
        encoded_list.append(chr(new_val))
    return output_formatter(''.join(encoded_list))

command_args = sys.argv
if len(command_args) < 2:
    print("Please provide a shift value as a command line argument.")
    sys.exit(1)

shift_val = int(command_args[1])
for line in sys.stdin:
    result_output = encode(line.strip(), shift_val)
    sys.stdout.write(result_output)