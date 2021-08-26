import json
from collections import OrderedDict

the_answer = 42

tricolon = [
    'life',
    'the Universe',
    'everything',
]

flavors = [
    'cherry',
    'chocolate',
    'pear',
]

month_names = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December',
]

month_lengths = [
    ['January', 31],
    ['February', 28],
    ['March', 31],
    ['April', 30],
    ['May', 31],
    ['June', 30],
    ['July', 31],
    ['August', 31],
    ['September', 30],
    ['October', 31],
    ['November', 31],
    ['December', 31],
]

month_day_ranges = OrderedDict((name, list(range(1, length+1))) for name, length in month_lengths)

ABX = 'ABX'
ADCA = 'ADCA'
ADCB = 'ADCB'
ADDA = 'ADDA'
ADDB = 'ADDB'
ADDD = 'ADDD'
BNE = 'BNE'
BPL = 'BPL'
JMP = 'JMP'
JSR = 'JSR'
LBRA = 'LBRA'
LBNE = 'LBNE'
LDA = 'LDA'
LDB = 'LDB'
SUBB = 'SUBB'
SUBD = 'SUBD'
SWI = 'SWI'
SWI2 = 'SWI2'
SWI3 = 'SWI3'
SYNC = 'SYNC'
TFR = 'TFR'
TSTA = 'TSTA'
TSTB = 'TSTB'
TST = 'TST'

ORG = 'ORG'
FCB = 'FCB'

INH = "Inherent"
IMM = "Immediate"
DIR = "Direct"
IDX = "Indexed"
EXT = "Extended"
REL8 = "Relative8 8-bit"
REL16 = "Relative8 16-bit"



OPCODES =  {
    ABX:   { INH: 0x3A,                                                                     },
    ADCA:  {              IMM: 0x89,   DIR: 0x99,   IDX: 0xA9,   EXT: 0xB9,                 },
    ADCB:  {              IMM: 0xC9,   DIR: 0xD9,   IDX: 0xE9,   EXT: 0xF9,                 },
    ADDA:  {              IMM: 0x8B,   DIR: 0x9B,   IDX: 0xAB,   EXT: 0xBB,                 },
    ADDB:  {              IMM: 0xCB,   DIR: 0xDB,   IDX: 0xEB,   EXT: 0xFB,                 },
    ADDD:  {              IMM: 0xC3,   DIR: 0xD3,   IDX: 0xE3,   EXT: 0xF3,                 },
    BNE:   {                                                                   REL8: 0x26   },
    BPL:   {                                                                   REL8: 0x2A   },
    JMP:   {                           DIR: 0x0E,   IDX: 0x6E,   EXT: 0x7E,                 },
    JSR:   {                           DIR: 0x9D,   IDX: 0xAD,   EXT: 0xBD,                 },
    LBRA:  {                                                                  REL16: 0x16   },
    LBNE:  {                                                                  REL16: 0x1026 },
    LDA:   {              IMM: 0x86,   DIR: 0x96,   IDX: 0xA6,   EXT: 0xB6,                 },
    LDB:   {              IMM: 0xC6,   DIR: 0xD6,   IDX: 0xE6,   EXT: 0xF6,                 },
    SUBB:  {              IMM: 0xC0,   DIR: 0xD0,   IDX: 0xE0,   EXT: 0xF0,                 },
    SUBD:  {              IMM: 0x83,   DIR: 0x93,   IDX: 0xA3,   EXT: 0xB3,                 },
    SWI:   { INH: 0x3F,                                                                     },
    SWI2:  { INH: 0x103F,                                                                   },
    SWI3:  { INH: 0x113F,                                                                   },
    SYNC:  { INH: 0x13,                                                                     },
    TFR:   {              IMM: 0x1F,                                                        },
    TSTA:  { INH: 0x4D,                                                                     },
    TSTB:  { INH: 0x5D,                                                                     },
    TST:   {                           DIR: 0x0D,   IDX: 0x6D,   EXT: 0x7D,                 },
}

class MyClass:

    class_attribute = 89

json_month_lengths = json.dumps(month_lengths, indent=4)
