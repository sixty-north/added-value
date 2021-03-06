class Mnemonic(object):

    _instances = {}

    def __new__(cls, mnemonic):
        if len(mnemonic) < 1:
            raise ValueError("Mnemonic cannot be empty")
        if not (mnemonic[0].isalpha() and mnemonic[0].isupper()):
            raise ValueError("Mnemonic {} does not begin with an uppercase alphabetic character".format(mnemonic))
        if (len(mnemonic) > 1) and not (mnemonic[1:].isalnum() and all(c.isupper() for c in mnemonic[1:] if c.isalpha())):
            raise ValueError("Mnemonic {} is not uppercase alphanumeric".format(mnemonic))
        if mnemonic in cls._instances:
            return cls._instances[mnemonic]
        obj = object.__new__(cls)
        obj._mnemonic = mnemonic
        cls._instances[mnemonic] = obj
        return obj

    def __str__(self):
        return self._mnemonic

    def __repr__(self):
        return "{}({})".format(self.__class__.__name__, self._mnemonic)

    def __lt__(self, rhs):
        if not isinstance(rhs, Mnemonic):
            return NotImplemented
        return self._mnemonic < rhs._mnemonic



ABX = Mnemonic('ABX')
ADCA = Mnemonic('ADCA')
ADCB = Mnemonic('ADCB')
ADDA = Mnemonic('ADDA')
ADDB = Mnemonic('ADDB')
ADDD = Mnemonic('ADDD')
ANDA = Mnemonic('ANDA')
ANDB = Mnemonic('ANDB')
ANDCC = Mnemonic('ANDCC')
ASLA = Mnemonic('ASLA')
ASLB = Mnemonic('ASLB')
ASL = Mnemonic('ASL')
ASRA = Mnemonic('ASRA')
ASRB = Mnemonic('ASRB')
ASR = Mnemonic('ASR')
BEQ = Mnemonic('BEQ')
BITA = Mnemonic('BITA')
BITB = Mnemonic('BITB')
BHS = Mnemonic('BHS')
BLO = Mnemonic('BLO')
BNE = Mnemonic('BNE')
BPL = Mnemonic('BPL')
BRA = Mnemonic('BRA')
CLRA = Mnemonic('CLRA')
CLRB = Mnemonic('CLRB')
CLR = Mnemonic('CLR')
CMPA = Mnemonic('CMPA')
CMPB = Mnemonic('CMPB')
CMPD = Mnemonic('CMPD')
CMPS = Mnemonic('CMPS')
CMPU = Mnemonic('CMPU')
CMPX = Mnemonic('CMPX')
CMPY = Mnemonic('CMPY')
COMA = Mnemonic('COMA')
COMB = Mnemonic('COMB')
COM = Mnemonic('COM')
CWAI = Mnemonic('CWAI')
DAA = Mnemonic('DAA')
DECA = Mnemonic('DECA')
DECB = Mnemonic('DECB')
DEC = Mnemonic('DEC')
EORA = Mnemonic('EORA')
EORB = Mnemonic('EORB')
EXG = Mnemonic('EXG')
INCA = Mnemonic('INCA')
INCB = Mnemonic('INCB')
INC = Mnemonic('INC')
JMP = Mnemonic('JMP')
JSR = Mnemonic('JSR')
LBRA = Mnemonic('LBRA')
LBNE = Mnemonic('LBNE')
LDA = Mnemonic('LDA')
LDB = Mnemonic('LDB')
LDD = Mnemonic('LDD')
LDS = Mnemonic('LDS')
LDU = Mnemonic('LDU')
LDX = Mnemonic('LDX')
LDY = Mnemonic('LDY')
LEAS = Mnemonic('LEAS')
LEAU = Mnemonic('LEAU')
LEAX = Mnemonic('LEAX')
LEAY = Mnemonic('LEAY')
LSLA = Mnemonic('LSLA')
LSLB = Mnemonic('LSLB')
LSL = Mnemonic('LSL')
LSRA = Mnemonic('LSRA')
LSRB = Mnemonic('LSRB')
LSR = Mnemonic('LSR')
MUL = Mnemonic('MUL')
NEGA = Mnemonic('NEGA')
NEGB = Mnemonic('NEGB')
NEG = Mnemonic('NEG')
NOP = Mnemonic('NOP')
ORA = Mnemonic('ORA')
ORB = Mnemonic('ORB')
ORCC = Mnemonic('ORCC')
PSHS = Mnemonic('PSHS')
PSHU = Mnemonic('PSHU')
PULS = Mnemonic('PULS')
PULU = Mnemonic('PULU')
ROLA = Mnemonic('ROLA')
ROLB = Mnemonic('ROLB')
ROL = Mnemonic('ROL')
RORA = Mnemonic('RORA')
RORB = Mnemonic('RORB')
ROR = Mnemonic('ROR')
RTI = Mnemonic('RTI')
RTS = Mnemonic('RTS')
SBCA = Mnemonic('SBCA')
SBCB = Mnemonic('SBCB')
SEX = Mnemonic('SEX')
STA = Mnemonic('STA')
STB = Mnemonic('STB')
STD = Mnemonic('STD')
STS = Mnemonic('STS')
STU = Mnemonic('STU')
STX = Mnemonic('STX')
STY = Mnemonic('STY')
SUBA = Mnemonic('SUBA')
SUBB = Mnemonic('SUBB')
SUBD = Mnemonic('SUBD')
SWI = Mnemonic('SWI')
SWI2 = Mnemonic('SWI2')
SWI3 = Mnemonic('SWI3')
SYNC = Mnemonic('SYNC')
TFR = Mnemonic('TFR')
TSTA = Mnemonic('TSTA')
TSTB = Mnemonic('TSTB')
TST = Mnemonic('TST')

ORG = Mnemonic('ORG')
FCB = Mnemonic('FCB')

INH = "Inherent"
IMM = "Immediate"
DIR = "Direct"
IDX = "Indexed"
EXT = "Extended"
REL8 = "Relative8 8-bit"
REL16 = "Relative8 16-bit"



OPCODES = {
    ABX:   { INH: 0x3A,                                                                     },
    ADCA:  {              IMM: 0x89,   DIR: 0x99,   IDX: 0xA9,   EXT: 0xB9,                 },
    ADCB:  {              IMM: 0xC9,   DIR: 0xD9,   IDX: 0xE9,   EXT: 0xF9,                 },
    ADDA:  {              IMM: 0x8B,   DIR: 0x9B,   IDX: 0xAB,   EXT: 0xBB,                 },
    ADDB:  {              IMM: 0xCB,   DIR: 0xDB,   IDX: 0xEB,   EXT: 0xFB,                 },
    ADDD:  {              IMM: 0xC3,   DIR: 0xD3,   IDX: 0xE3,   EXT: 0xF3,                 },
    # ANDA:  {              IMM: 0x84,   DIR: 0x94,   IDX: 0xA4,   EXT: 0xB4,                 },
    # ANDB:  {              IMM: 0xC4,   DIR: 0xD4,   IDX: 0xE4,   EXT: 0xF4,                 },
    # ANDCC: {              IMM: 0x1C,                                                        },
    # ASLA:  { INH: 0x48,                                                                     },
    # ASLB:  { INH: 0x58,                                                                     },
    # ASL:   {                           DIR: 0x08,   IDX: 0x68,   EXT: 0x78,                 },
    # ASRA:  { INH: 0x47,                                                                     },
    # ASRB:  { INH: 0x57,                                                                     },
    # ASR:   {                           DIR: 0x07,   IDX: 0x67,   EXT: 0x77,                 },
    # BEQ:   {                                                                   REL8: 0x27   },
    # BITA:  {              IMM: 0x85,   DIR: 0x95,   IDX: 0xA5,   EXT: 0xB5,                 },
    # BITB:  {              IMM: 0xC5,   DIR: 0xD5,   IDX: 0xE5,   EXT: 0xF5,                 },
    # BHS:   {                                                                   REL8: 0x24   },
    # BLO:   {                                                                   REL8: 0x25   },
    # BNE:   {                                                                   REL8: 0x26   },
    # BPL:   {                                                                   REL8: 0x2A   },
    # BRA:   {                                                                   REL8: 0x20   },
    # CLRA:  { INH: 0x4F,                                                                     },
    # CLRB:  { INH: 0x5F,                                                                     },
    # CLR:   {                           DIR: 0x0F,   IDX: 0x6F,   EXT: 0x7F,                 },
    # CMPA:  {              IMM: 0x81,   DIR: 0x91,   IDX: 0xA1,   EXT: 0xB1,                 },
    # CMPB:  {              IMM: 0xC1,   DIR: 0xD1,   IDX: 0xE1,   EXT: 0xF1,                 },
    # CMPD:  {              IMM: 0x1083, DIR: 0x1093, IDX: 0x10A3, EXT: 0x10B3,               },
    # CMPS:  {              IMM: 0x118C, DIR: 0x119C, IDX: 0x11AC, EXT: 0x11BC,               },
    # CMPU:  {              IMM: 0x1183, DIR: 0x1193, IDX: 0x11A3, EXT: 0x11B3,               },
    # CMPX:  {              IMM: 0x8C,   DIR: 0x9C,   IDX: 0xAC,   EXT: 0xBC,                 },
    # CMPY:  {              IMM: 0x108C, DIR: 0x109C, IDX: 0x10AC, EXT: 0x10BC,               },
    # COMA:  { INH: 0x43,                                                                     },
    # COMB:  { INH: 0x53,                                                                     },
    # COM:   {                           DIR: 0x03,   IDX: 0x63,   EXT: 0x73,                 },
    # CWAI:  {              IMM: 0x3C,                                                        },
    # DAA:   { INH: 0x19,                                                                     },
    # DECA:  { INH: 0x4A,                                                                     },
    # DECB:  { INH: 0x5A,                                                                     },
    # DEC:   {                           DIR: 0x0A,   IDX: 0x6A,   EXT: 0x7A,                 },
    # EORA:  {              IMM: 0x88,   DIR: 0x98,   IDX: 0xA8,   EXT: 0xB8,                 },
    # EORB:  {              IMM: 0xC8,   DIR: 0xD8,   IDX: 0xE8,   EXT: 0xF8,                 },
    # EXG:   {              IMM: 0x1E,                                                        },
    # INCA:  { INH: 0x4C,                                                                     },
    # INCB:  { INH: 0x5C,                                                                     },
    # INC:   {                           DIR: 0x0C,   IDX: 0x6C,   EXT: 0x7C,                 },
    # JMP:   {                           DIR: 0x0E,   IDX: 0x6E,   EXT: 0x7E,                 },
    # JSR:   {                           DIR: 0x9D,   IDX: 0xAD,   EXT: 0xBD,                 },
    # LBRA:  {                                                                  REL16: 0x16   },
    # LBNE:  {                                                                  REL16: 0x1026 },
    # LDA:   {              IMM: 0x86,   DIR: 0x96,   IDX: 0xA6,   EXT: 0xB6,                 },
    # LDB:   {              IMM: 0xC6,   DIR: 0xD6,   IDX: 0xE6,   EXT: 0xF6,                 },
    # LDD:   {              IMM: 0xCC,   DIR: 0xDC,   IDX: 0xEC,   EXT: 0xFC,                 },
    # LDS:   {              IMM: 0x10CE, DIR: 0x10DE, IDX: 0x10EE, EXT: 0x10FE,               },
    # LDU:   {              IMM: 0xCE,   DIR: 0xDE,   IDX: 0xEE,   EXT: 0xFE,                 },
    # LDX:   {              IMM: 0x8E,   DIR: 0x9E,   IDX: 0xAE,   EXT: 0xBE,                 },
    # LDY:   {              IMM: 0x108E, DIR: 0x109E, IDX: 0x10AE, EXT: 0x10BE,               },
    # LEAS:  {                                        IDX: 0x32,                              },
    # LEAU:  {                                        IDX: 0x33,                              },
    # LEAX:  {                                        IDX: 0x30,                              },
    # LEAY:  {                                        IDX: 0x31,                              },
    # LSLA:  { INH: 0x48,                                                                     },
    # LSLB:  { INH: 0x58,                                                                     },
    # LSL:   {                           DIR: 0x08,   IDX: 0x68,   EXT: 0x78,                 },
    # LSRA:  { INH: 0x44,                                                                     },
    # LSRB:  { INH: 0x54,                                                                     },
    # LSR:   {                           DIR: 0x04,   IDX: 0x64,   EXT: 0x74,                 },
    # MUL:   { INH: 0x3D,                                                                     },
    # NEGA:  { INH: 0x40,                                                                     },
    # NEGB:  { INH: 0x50,                                                                     },
    # NEG:   {                           DIR: 0x00,   IDX: 0x60,   EXT: 0x70,                 },
    # NOP:   { INH: 0x12,                                                                     },
    # ORA:   {              IMM: 0x8A,   DIR: 0x9A,   IDX: 0xAA,   EXT: 0xBA,                 },
    # ORB:   {              IMM: 0xCA,   DIR: 0xDA,   IDX: 0xEA,   EXT: 0xFA,                 },
    # ORCC:  {              IMM: 0x1A,                                                        },
    # PSHS:  {              IMM: 0x34,                                                        },
    # PSHU:  {              IMM: 0x36,                                                        },
    # PULS:  {              IMM: 0x35,                                                        },
    # PULU:  {              IMM: 0x37,                                                        },
    # ROLA:  { INH: 0x49,                                                                     },
    # ROLB:  { INH: 0x59,                                                                     },
    # ROL:   {                           DIR: 0x09,   IDX: 0x69,   EXT: 0x79,                 },
    # RORA:  { INH: 0x46,                                                                     },
    # RORB:  { INH: 0x56,                                                                     },
    # ROR:   {                           DIR: 0x06,   IDX: 0x66,   EXT: 0x76,                 },
    # RTI:   { INH: 0x3B,                                                                     },
    # RTS:   { INH: 0x39,                                                                     },
    # SBCA:  {              IMM: 0x82,   DIR: 0x92,   IDX: 0xA2,   EXT: 0xB2,                 },
    # SBCB:  {              IMM: 0xC2,   DIR: 0xD2,   IDX: 0xE2,   EXT: 0xF2,                 },
    # SEX:   { INH: 0x1D,                                                                     },
    # STA:   {                           DIR: 0x97,   IDX: 0xA7,   EXT: 0xB7,                 },
    # STB:   {                           DIR: 0xD7,   IDX: 0xE7,   EXT: 0xF7,                 },
    # STD:   {                           DIR: 0xDD,   IDX: 0xED,   EXT: 0xFD,                 },
    # STS:   {                           DIR: 0x10DF, IDX: 0x10EF, EXT: 0x10FF,               },
    # STU:   {                           DIR: 0xDF,   IDX: 0xEF,   EXT: 0xFF,                 },
    # STX:   {                           DIR: 0x9F,   IDX: 0xAF,   EXT: 0xBF,                 },
    # STY:   {                           DIR: 0x109F, IDX: 0x10AF, EXT: 0x10BF,               },
    # SUBA:  {              IMM: 0x80,   DIR: 0x90,   IDX: 0xA0,   EXT: 0xB0,                 },
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
