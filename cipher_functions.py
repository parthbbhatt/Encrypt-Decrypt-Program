# Functions for running an encryption or decryption.

# The values of the two jokers.
JOKER1 = 27
JOKER2 = 28

# Write your functions here:


def clean_message(message):
    '''(str) -> str

    The function takes a single message and capitalizes all the alphabetic
    letters and removes any numbers and spaces in it.

    >>> clean_message("helloworld")
    'HELLOWORLD'
    >>> clean_message("ThisWorks")
    'THISWORKS'
    >>> clean_message("test123test")
    'TESTTEST'
    '''
    alpha_message = ''

    for letter in message:
        if letter.isalpha():
            upper_letter = letter.upper()
            alpha_message += upper_letter

    return alpha_message


def encrypt_letter(character, keystream_value):
    '''(str, int) -> str

    This function converts the character to a nummeric value given by its
    position in the alphabet and then adds the keystream_value. If the sum
    is greater than 25, it subtracts 26 from it. Given the new value, it
    converts it into an back to a letter in the alphabet.

    REQ: keystream_value >= 0 and keystream_value <= 26.
    REQ: Character must be a letter from the english alphabet.

    >>> encrypt_letter('L', 6)
    'R'
    >>> encrypt_letter('a', 0)
    'A'
    >>> encrypt_letter('X', 8)
    'F'
    '''
    # make sure the letter is not number and is capitalized
    letter = clean_message(character)

    # covert letter into integer and ensure that the first letter(A) starts
    # from value 0
    letter_clean = ord(letter) - 65

    # add keystream value to letter
    encryption = letter_clean + keystream_value

    # if encryption value is greater than 25, then subtract 26 from it
    if(encryption > 25):
        encryption_check = encryption - 26

    # else leave as it is
    else:
        encryption_check = encryption

    # new letter's value must be +65 to revert to the orignal numbering
    # system for alphabets
    new_letter_value = encryption_check + 65

    # convert the letter value to a new letter
    new_letter = chr(new_letter_value)

    # return new letter
    return new_letter


def decrypt_letter(character, keystream_value):
    '''(str, int) -> str

    This function performs decrypts the message with the given kystream value
    on a single character. It converts the letter to a numeric value which is
    given by its position in the alphabet and then adds the keystream value to
    it. If the output is greater than 26, it adds 26 to the letters valune and
    then subtracts the keystream value form it. It then converts the final
    output back into a letter in the aplhabet.

    REQ: Character has to be a single uppercase letter from the alphabet.
    REQ: keystream_value <=26 and keystream_value >= 0.

    >>> decrypt_letter('X', 12)
    'L'
    >>> decrypt_letter('B', 1)
    'A'
    >>> decrypt_letter('B', 17)
    'K'
    >>> decrypt_letter('D', 25)
    'E'
    '''
    # covert letter into integer and ensure that the first letter(A) starts
    # from value 0
    letter_value = ord(character) - 65

    # if the letter's value is less than the keystream value then add 26 to the
    # letter's value and then subtract the keystream value from them
    if(letter_value < keystream_value):
        decrypt = (letter_value + 26) - keystream_value

    # else subtract directly from the letter's value
    else:
        decrypt = letter_value - keystream_value

    # original letter's value must be +65 to revert to the orignal numbering
    # system for alphabets
    new_letter_value = decrypt + 65

    # convert the letter value to a new letter
    new_letter = chr(new_letter_value)

    # returns the new letter
    return new_letter


def swap_cards(deck_cards, index):
    '''(list of int, int) -> NoneType

    This function swaps the card at the index with the card that follows it. It
    treats the deck as circular so the card at the index is at the bottom of
    the deck, swaps with the card with at top of the deck.

    REQ: deck_cards must contain only intergers from 1-28 in some order.

    >>> deck_cards = [27, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 25]
    >>> swap_cards(deck_cards, 0)
    >>> deck_cards == [7, 27, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 25]
    True
    >>> deck_cards = [27, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 25]
    >>> swap_cards(deck_cards, 27)
    >>> deck_cards == [25, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 27]
    True
    >>> deck_cards = [27, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 25]
    >>> swap_cards(deck_cards, 17)
    >>> deck_cards == [27, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 18, 17, 19, 20, 21, 22, 23, 24, 26, 28, 25]
    True
    '''
    last_index = len(deck_cards) - 1

    # if index is the last element of array, swap with the card at the top of
    # the deck
    if (index == last_index):
        deck_cards[:] = (deck_cards[index:index+1] + deck_cards[1:index] +
                         deck_cards[0:1])

    # else swap with the card before it
    else:
        deck_cards[:] = (deck_cards[:index] + deck_cards[index+1:index+2] +
                         deck_cards[index:index+1] + deck_cards[index+2:])


def move_joker_1(deck_cards):
    '''(list of int) -> NoneType

    This is step 1 of the algorithm where it finds JOKER1 in the deck and swaps
    it with the card that follows it. It treats the deck as ciruclar.

    REQ: deck_cards must contain only intergers from 1-28 in some order.

    >>> deck_cards = [25, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 27, 18, 19, 20, 21, 22, 23, 24, 26, 28]
    >>> move_joker_1(deck_cards)
    >>> deck_cards == [25, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 18, 27, 19, 20, 21, 22, 23, 24, 26, 28]
    True
    >>> deck_cards = [25, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 27]
    >>> move_joker_1(deck_cards)
    >>> deck_cards == [27, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 25]
    True
    >>> deck_cards = [27,7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 25]
    >>> move_joker_1(deck_cards)
    >>> deck_cards == [7, 27, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 26, 28, 25]
    True
    '''
    # find the index of JOKER1 in the deck of cards
    first_joker = deck_cards.index(JOKER1)

    # use the swap function to swap the following card in the deck
    joker1_swap = swap_cards(deck_cards, first_joker)


def move_joker_2(deck_cards):
    '''(list of int) -> NoneType

    This function is step 2 of the algorithm where it finds JOKER2 in the deck
    and moves it 2 cards down while treating the deck as circular.

    REQ: deck_cards must contain only intergers from 1-28 in some order.

    >>> deck_cards = [25, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 28, 14, \
    13, 16, 17, 27, 18, 19, 20, 21, 22, 23, 24, 26]
    >>> move_joker_2(deck_cards)
    >>> deck_cards == [25, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    28, 16, 17, 27, 18, 19, 20, 21, 22, 23, 24, 26]
    True
    >>> deck_cards = [28, 25, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, \
    13, 16, 17, 27, 18, 19, 20, 21, 22, 23, 24, 26]
    >>> move_joker_2(deck_cards)
    >>> deck_cards == [25, 7, 28, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, \
    13, 16, 17, 27, 18, 19, 20, 21, 22, 23, 24, 26]
    True
    >>> deck_cards = [25, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 27, 18, 19, 20, 21, 22, 23, 24, 26, 28]
    >>> move_joker_2(deck_cards)
    >>> deck_cards == [7, 28, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 14, 13, \
    16, 17, 27, 18, 19, 20, 21, 22, 23, 24, 26, 25]
    True
    '''
    # find the index of JOKER1 in the deck of cards
    second_joker_check1 = deck_cards.index(JOKER2)

    # use the swap function to swap the following card in the deck
    joker2_swap1 = swap_cards(deck_cards, second_joker_check1)

    # get the new postion of the joker
    second_joker_check2 = deck_cards.index(JOKER2)

    # swap the deck the second time
    joker2_swap2 = swap_cards(deck_cards, second_joker_check2)


def triple_cut(deck_cards):
    '''(list of int) -> NoneType

    The function does Step 3 of the algorithm where it finds the two jokers and
    and keeps everthing between them the way it is but swaps everything outside
    of them. So if JOKER1 is below JOKER2 in the deck, everything after JOKER1
    is swapped with everything before JOKER2.

    REQ: deck_cards must contain only intergers from 1-28 in some order.

    >>> deck_cards = [27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28]
    >>> triple_cut(deck_cards)
    >>> deck_cards == [27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28]
    True
    >>> deck_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 27, 13, 14, 15, 16, \
    17, 18, 19, 28, 21, 22, 23, 24, 25, 26]
    >>> triple_cut(deck_cards)
    >>> deck_cards == [21, 22, 23, 24, 25, 26, 27, 13, 14, 15, 16, 17, 18, \
    19, 28, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    True
    '''
    # get the index of JOKER1 in the deck
    joker1_index = deck_cards.index(JOKER1)

    # get the index of JOKER2 in the deck
    joker2_index = deck_cards.index(JOKER2)

    # if JOKER1 is positioned above JOKER2, slice the list in the given format
    if(joker1_index < joker2_index):
        deck_cards[:] = (deck_cards[joker2_index+1:] +
                         deck_cards[joker1_index:joker2_index+1] +
                         deck_cards[:joker1_index])

    # if JOKER1 is positioned below JOKER2, slice the list in the given format
    elif(joker2_index < joker1_index):
        deck_cards[:] = (deck_cards[joker1_index+1:] +
                         deck_cards[joker2_index:joker1_index+1] +
                         deck_cards[:joker2_index])


def insert_top_to_bottom(deck_cards):
    '''(list of int) -> NoneType

    This function does step 4 of the algorithm where it looks at the bottom
    card and moves that many cards from the top to the bottom before the last
    card.

    REQ: deck_cards must contain only intergers from 1-28 in some order.

    >>> deck_cards = [27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28]
    >>> insert_top_to_bottom(deck_cards)
    >>> deck_cards == [27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28]
    True
    >>> deck_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 27, 14, 15, \
    16, 17, 28, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    >>> insert_top_to_bottom(deck_cards)
    >>> deck_cards == [25, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 27, 14, \
    15, 16, 17, 28, 18, 19, 20, 21, 22, 23, 24, 26]
    True
    >>> deck_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 28, 14, 15, \
    16, 17, 27, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    >>> insert_top_to_bottom(deck_cards)
    >>> deck_cards = [7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 28, 14, 13, \
    16, 17, 27, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    >>> insert_top_to_bottom(deck_cards)
    >>> deck_cards == [25, 7, 2, 3, 4, 5, 6, 1, 8, 10, 9, 11, 12, 15, 28, 14, \
    13, 16, 17, 27, 18, 19, 20, 21, 22, 23, 24, 26]
    True
    '''
    # find index of the last element in the list
    last_val_index = len(deck_cards) - 1

    # if the bottom card is JOKER2, use JOKER1 as the value of the last element
    if(deck_cards[last_val_index] == JOKER2):
        last_val = JOKER1

    # value of the last element
    else:
        last_val = deck_cards[last_val_index]

    # use value of the last element as the index to slice the list from the
    # first element to the index and insert it before the last element in list
    deck_cards[:] = (deck_cards[last_val:last_val_index] +
                     deck_cards[0:last_val] +
                     deck_cards[last_val_index:last_val_index+1])


def get_card_at_top_index(deck_cards):
    '''(list of int) -> int

    Step 5 of the algorithm. Uses the value of the top card as an index and
    return the card in that deck at that index. If the top card is JOKER2, use
    JOKER1 as the index.

    REQ: deck_cards must contain only intergers from 1-28 in some order.

    >>> deck_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 27, 13, 14, 15, 16, \
    17, 18, 19, 28, 20, 21, 22, 23, 24, 25, 26]
    >>> get_card_at_top_index(deck_cards)
    2
    >>> deck_cards = [7, 2, 3, 4, 5, 6, 1, 8, 9, 10, 11, 27, 13, 14, 15, 16, \
    17, 18, 19, 28, 20, 21, 22, 23, 24, 25, 26]
    >>> get_card_at_top_index(deck_cards)
    8
    >>> deck_cards = [28, 2, 3, 4, 5, 6, 1, 8, 9, 10, 11, 27, 13, 14, 15, 16, \
    17, 18, 19, 7, 21, 22, 23, 24, 25, 26, 12, 20]
    >>> get_card_at_top_index(deck_cards)
    20
    '''
    # if the first element has value of 28, use 27 as the index
    if(deck_cards[0] == JOKER2):
        first_val = JOKER1

    # else use the value of the first element
    else:
        first_val = deck_cards[0]

    # value at index
    val_at_index = deck_cards[first_val]

    # return value at the index
    return val_at_index


def get_next_value(deck_cards):
    '''(list of int) -> int

    A function that does all the 5 steps of the algorithm and returns a
    potential keystream.

    REQ: deck_cards must contain only intergers from 1-28 in some order.

    >>> deck_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 13, 27, 14, 15, \
    12, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28]
    >>> get_next_value(deck_cards)
    8
    >>> deck_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 13, 15, 14, 27, \
    12, 28, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26]
    >>> get_next_value(deck_cards)
    2
    >>> deck_cards = [27, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, \
    16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28]
    >>> get_next_value(deck_cards)
    4
    '''
    # applies step 1 of the algorithm to the deck of cards
    move_joker_1(deck_cards)

    # applies step 2 of the algorithm to the deck of cards
    move_joker_2(deck_cards)

    # applies step 3 of the algorithm to the deck of cards
    triple_cut(deck_cards)

    # applies step 4 of the algorithm to the deck of cards
    insert_top_to_bottom(deck_cards)

    # applies step 5 of the algorithm to the deck of cards
    potential_keystream = get_card_at_top_index(deck_cards)

    # returns potential keystream
    return potential_keystream


def get_next_keystream_value(deck_cards):
    '''(list of int) -> int

    The function gets the actual keystream value as if the potential keystream
    from the function get_next_value() is a JOKER1 or JOKER2, it will run the
    algorithm again with the deck at that current state.

    REQ: deck_cards must contain only intergers from 1-28 in some order.

    >>> deck_cards = [1, 2, 3, 4, 5, 6, 27, 8, 9, 10, 11, 12, 13, 14, 15, 16, \
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 7, 28]
    >>> get_next_keystream_value(deck_cards)
    22
    >>> deck_cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 16, 13, 27, 14, 15, \
    12, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 28]
    >>> get_next_keystream_value(deck_cards)
    8
    '''
    # set default keystream value as JOKER1
    keystream = JOKER1

    # while loop will run function get_next_value() if keystream value is
    # either JOKER1 or JOKER2 and set the new value for keystream
    while(keystream == JOKER1 or keystream == JOKER2):
        keystream = get_next_value(deck_cards)

    # returns the final keystream
    return keystream


def process_message(deck_cards, message, encrypt_decrypt):
    '''(list of int, str, str) -> str

    The function encrypts or decrypts a given message.

    REQ: deck_cards must contain only intergers from 1-28 in some order.
    REQ: encrypt_decrypt must either be 'e' or 'd'

    >>> deck_cards = [1, 2, 3, 4, 5, 6, 27, 8, 9, 10, 11, 12, 13, 14, 15, 16, \
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 7, 28]
    >>> process_message(deck_cards, 'helloworld', 'e')
    'DRCAZBQGMI'
    >>> deck_cards = [1, 2, 3, 4, 5, 6, 27, 8, 9, 10, 11, 12, 13, 14, 15, 16, \
    17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 7, 28]
    >>> process_message(deck_cards, 'DRCAZBQGMI', 'd')
    'HELLOWORLD'
    '''
    # applies the clean_message() function to the message
    cleaned_message = clean_message(message)

    # string that will have the encrypted decrypted message
    encrypt_decrypt_message = ''

    # runs through each character in the message and encrypts/decrypts it
    for character in cleaned_message:

        # if encrypt_decrypt is 'e', encrypt it
        if(encrypt_decrypt == 'e'):

            # run the keystream function to get a keystream
            keystream = get_next_keystream_value(deck_cards)
            # use the encryption function and add the encrypted letter to the
            # encrypt_decrypt_message string
            encrypt_decrypt_message += encrypt_letter(character, keystream)

        # else if encrypt_decrypt is 'd', decrypt it
        elif(encrypt_decrypt == 'd'):

            # run the keystream function to get a keystream
            keystream = get_next_keystream_value(deck_cards)

            # use the decryption function and add the decrypted letter to the
            # encrypt_decrypt_message string
            encrypt_decrypt_message += decrypt_letter(character, keystream)

    # return the encrypted/decrypted message
    return encrypt_decrypt_message


def process_messages(deck_cards, messages, encrypt_decrypt):
    '''(list of int, list of str, str) -> list of str

    The function encrypts or decrypts a list of given messages.

    REQ: deck_cards must contain only intergers from 1-28 in some order.
    REQ: encrypt_decrypt must either be 'e' or 'd'

    >>> deck_cards = [28, 2, 3, 4, 5, 6, 1, 8, 9, 10, 11, 27, 13, 14, 15, 16, \
    17, 18, 19, 7, 21, 22, 23, 24, 25, 26, 12, 20]
    >>> process_messages(deck_cards, ['How','are','you','doing','today'], 'e')
    ['PBD', 'SQZ', 'XMI', 'MARKB', 'BOLWN']
    >>> deck_cards = [28, 2, 3, 4, 5, 6, 1, 8, 9, 10, 11, 27, 13, 14, 15, 16, \
    17, 18, 19, 7, 21, 22, 23, 24, 25, 26, 12, 20]
    >>> process_messages(deck_cards, ['PBD', 'SQZ', 'XMI', 'MARKB'],'d')
    ['HOW', 'ARE', 'YOU', 'DOING']
    >>> deck_cards = [28, 2, 3, 4, 5, 6, 1, 8, 9, 10, 11, 27, 13, 14, 15, 16, \
    17, 18, 19, 7, 21, 22, 23, 24, 25, 26, 12, 20]
    >>> process_messages(deck_cards, ['One message'], 'e')
    ['WALEDNRYUN']
    >>> deck_cards = [28, 2, 3, 4, 5, 6, 1, 8, 9, 10, 11, 27, 13, 14, 15, 16, \
    17, 18, 19, 7, 21, 22, 23, 24, 25, 26, 12, 20]
    >>> process_messages(deck_cards, ['WALEDNRYUN'], 'd')
    ['ONEMESSAGE']
    '''
    # an array which will include the encrypted/decryped messages
    new_message = []

    # for loop which goes through each element in the list
    for message in messages:
        # applies process_message() function to each element in the list
        list_messages = process_message(deck_cards, message, encrypt_decrypt)

        # adds the new message after encrypting/decrypting to the list
        new_message.append(list_messages)

    # returns the list called new_message
    return new_message


def read_messages(filehandle):
    '''(io.TextIOWrapper) -> list of str

    The function reads the messages in a file and puts them into a list with
    each element being a line in the code. It also strips '\n' or 'new line'
    from each element in the list.

    REQ: The file should be open.
    REQ: The file should exist within the directory.
    REQ: The file should be a textfile (.txt).
    '''
    # reads each line and puts it in an list
    list_of_lines = filehandle.readlines()

    # a new list with the modified elements
    new_lines = []

    # goes through each element in the list
    for line in list_of_lines:

        # strips '\n' from each element
        stripped_line = line.strip('\n')

        # adds it to new_lines
        new_lines.append(stripped_line)

    # returns the list with the new lines
    return new_lines


def read_deck(filehandle):
    '''(io.TextIOWrapper) -> list of str

    The function reads a file and creates a list and adds the numbers from the
    file to the list. Order doesn't matter.

    REQ: The file should be open.
    REQ: The file should exist within the directory.
    REQ: The file should be a textfile (.txt)
    REQ: The file must only contain numeric values from 1 to 28.
    '''
    # runs the read_messages function
    stripped_lines = read_messages(filehandle)

    # creates a which will contain the numbers
    list_elements_ints = []

    # goes through each line
    for line in stripped_lines:

        # splits each element
        element_split = line.split()

        # goes through each element
        for element in element_split:

            # converts the element into integer and adds it to a new list
            list_elements_ints.append(int(element))

    # returns the new list
    return list_elements_ints
