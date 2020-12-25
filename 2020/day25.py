card_public_key = 15733400
door_public_key = 6408062
# card_public_key = 5764801  # loop size must be 8
# door_public_key = 17807724  # loop size must be 11


def transform_subject_number(subject_number, loop_size):
    value = 1
    for _ in range(loop_size):
        value = value * subject_number
        value = value % 20201227
    return value


def find_loop_size(public_key):
    value = 1
    loop_size = 1
    while True:
        value = value * 7
        value = value % 20201227
        if value == public_key:
            return loop_size
        loop_size += 1


print("Part 1:")
card_loop_size = find_loop_size(card_public_key)
door_loop_size = find_loop_size(door_public_key)

encryption_key = transform_subject_number(card_public_key, door_loop_size)
other_encryption_key = transform_subject_number(door_public_key, card_loop_size)
if encryption_key != other_encryption_key:
    print(f'Encryption keys don\'t match: {encryption_key}, {other_encryption_key}')
    exit()
print(encryption_key)

