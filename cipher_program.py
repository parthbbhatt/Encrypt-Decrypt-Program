"""
Encrypt or decrypt the contents of a message file using a deck of cards.
"""

import cipher_functions

DECK_FILENAME = 'deck1.txt'
MSG_FILENAME = 'message-encrypted.txt'
MODE = 'd'  # 'e' for encryption, 'd' for decryption.


def main():
    """ () -> NoneType

    Perform the encryption using the deck from a file called DECK_FILENAME and
    the messages from a file called MSG_FILENAME. If MODE is 'e', encrypt;
    otherwise, decrypt. Print the decrypted message to the screen.
    """
    # open a file with to use as a deck of cards
    file_deck = open(DECK_FILENAME, 'r')

    # open a file with the messages that need to be encrypted or decrypted
    file_message = open(MSG_FILENAME, 'r')

    # read the file with the deck of cards
    deck_cards = cipher_functions.read_deck(file_deck)

    # read the file with the messages
    messaged = cipher_functions.read_messages(file_message)

    # encrypt or decrypt the messages
    e_or_d_messages = (cipher_functions.process_messages(deck_cards, messaged,
                                                         MODE))

    # print each message per line
    for string_elements in e_or_d_messages:
        print(string_elements)

main()
