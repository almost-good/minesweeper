"""
Constants.

Constants module contains constants used in game package.

Constants list:
    - HIDDEN (str) - represents hidden value of game board field.
    - MINE (str) - represents mine value of game board field.
    - EMPTY - represents empty value of game board field.
        Meaning there are no mines nearby to the field.
    - OFFSETS - formula for getting adjacent game board fields.
"""

# Board field values.
HIDDEN = 'x'
MINE = '*'
EMPTY = '.'
FLAG = '?'

# Formula for getting adjacent board fields.
OFFSETS = [(-1, -1), (-1, 0), (-1, 1), (0, -1),
           (0, 1), (1, -1), (1, 0), (1, 1)]
