class Table:

    def __init__(self, column_keys, rows_mapping):
        self._column_keys = list(column_keys)
        self._column_indexes = {key:index for index, key in enumerate(self._column_keys)}
        num_columns = len(column_keys)
        self._row_keys = list(rows_mapping.keys())
        if not all(len(row)==num_columns for row in rows_mapping.values()):
            raise ValueError("Not all row mapping values have a length of {}".format(num_columns))
        self._rows_mapping = rows_mapping

    @property
    def column_keys(self):
        return self._column_keys

    @property
    def row_keys(self):
        return self._row_keys

    def has_row_key(self, row_key):
        return row_key in self._rows_mapping.keys()

    def has_column_key(self, column_key):
        return column_key in self._column_keys

    def row(self, row_key):
        try:
            return self._rows_mapping[row_key]
        except KeyError:
            raise ValueError("No such row key {!r} for {!r}".format(row_key, self))

    def column(self, column_key):
        try:
            column_index = self._column_indexes[column_key]
        except KeyError:
            raise ValueError("No such column key {!r} for {!r}".format(column_key, self))
        return [row[column_index] for row in self._rows_mapping.values()]

    def cell(self, row_key, column_key):
        try:
            column_index = self._column_indexes[column_key]
        except KeyError:
            raise ValueError("No such column key {!r} for {!r}".format(column_key, self))

        try:
            return self._rows_mapping[row_key][column_index]
        except KeyError:
            raise ValueError("No such row key {!r} for {!r}".format(row_key, self))

    # TODO: __getitem__ indexes and slices

    @property
    def cells(self):
        """A dictionary of dictionaries containing all cells.
        """
        return {row_key: {column_key:cell for column_key, cell in zip(self._column_keys, cells)}
                for row_key, cells in self._rows_mapping.items()}

    def transpose(self):
        return Table(
            self._row_keys,
            {column_key: self.column(column_key) for column_key in self.column_keys}
        )


class MaterialStressTable:

    def __init__(self, temperatures, materials):
        """Create a material stress table.

        Args:
            temperatures: A sequence of temperatures.

            materials: A mapping of material names to sequences of stress values
                which correspond to the temperatures.
        """
        self._table = Table(
            column_keys=temperatures,
            rows_mapping=materials
        )

    @property
    def temperatures(self):
        return self._table.column_keys

    @property
    def materials(self):
        return self._table.row_keys

    def has_material(self, material):
        return self._table.has_row_key(material)

    def stresses_for_material(self, material):
        return self._table.row(material)

    def stress(self, material, temperature):
        return self._table.cell(material, temperature)

    @property
    def table(self):
        return self._table

CS_OR_LTCS = "CS/LTCS"

CS_200_MM = "200"

CS_150_MM = "150"

CS_100_MM = "100"

CS_60_MM = "60"

CS_40_MM = "40"

CS_16_MM = "16"

#: No material
NO_MATERIAL = "no material"

#: Carbon steel - default option
CS = "CS"

#: Low-temperature carbon steel
LTCS = "LTCS"

#: 304 stainless steel
SS_304 = "304 SS"

#: 316 stainless steel
SS_316 = "316 SS"

#: 304L low-carbon stainless steel
SS_304L = "304L SS"

#: 316L low-carbon stainless steel
SS_316L = "316L SS"

#: Duplex (22-Cr) 22% Cr Duplex stainless steel
DUPLEX_22CR = "Duplex (22-Cr)"

#: Super Duplex (25-Cr) 25% Cr Duplex stainless steel
SUPER_DUPLEX_25CR = "Duplex (25-Cr)"

# 6Mo stainless steel
MO_6 = "6Mo"

# Titanium
TITANIUM = "Titanium"

CARBON_STEEL_THICKNESSES_MM = (CS_16_MM, CS_40_MM, CS_60_MM, CS_100_MM, CS_150_MM, CS_200_MM)

stress_en13445 = MaterialStressTable(
                 temperatures = [  50,  100,  150,  200,  250,  300,  325,  350,  375,  400, 425, 450, 500, 550, 600, 650, 700, 750],
    materials =
    {
        CS_16_MM:               [2287, 2153, 1993, 1833, 1680, 1547, 1487, 1427, 1387, 1347,   0, 0, 0, 0, 0, 0, 0, 0],
        CS_40_MM:               [2227, 2093, 1940, 1780, 1633, 1500, 1443, 1387, 1347, 1307,   0, 0, 0, 0, 0, 0, 0, 0],
        CS_60_MM:               [2160, 2033, 1880, 1727, 1587, 1460, 1403, 1347, 1307, 1267,   0, 0, 0, 0, 0, 0, 0, 0],
        CS_100_MM:              [2033, 1913, 1767, 1627, 1493, 1373, 1320, 1267, 1230, 1193,   0, 0, 0, 0, 0, 0, 0, 0],
        CS_150_MM:              [1900, 1787, 1660, 1520, 1393, 1280, 1233, 1187, 1150, 1113,   0, 0, 0, 0, 0, 0, 0, 0],
        CS_200_MM:              [1807, 1700, 1573, 1447, 1327, 1220, 1173, 1127, 1093, 1060,   0, 0, 0, 0, 0, 0, 0, 0],
        SS_304:                 [1520, 1273, 1147, 1047,  967,  900,  880,  860,  847,  833, 823, 813, 800, 800,   0,   0,   0,   0],
        SS_304L:                [1453, 1207, 1080,  980,  913,  847,  827,  807,  790,  773, 760, 747, 727, 720,   0,   0,   0,   0],
        SS_316:                 [1613, 1407, 1273, 1180, 1113, 1040, 1020, 1000,  980,  960, 950, 940, 927, 913,   0,   0,   0,   0],
        SS_316L:                [1580, 1327, 1207, 1113, 1047,  967,  947,  927,  913,  900, 883, 867, 853, 847,   0,   0,   0,   0],
        DUPLEX_22CR:            [2813, 2400, 2233, 2100, 2000,    0,    0,    0,    0,    0,   0,   0,   0,   0,   0,   0,   0,   0],
        SUPER_DUPLEX_25CR:      [3333, 3000, 2800, 2667, 2533,    0,    0,    0,    0,    0,   0,   0,   0,   0,   0,   0,   0,   0],
        TITANIUM:               [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,   0,   0,   0,   0,   0,   0,   0,   0],
        MO_6:                   [   0,    0,    0,    0,    0,    0,    0,    0,    0,    0,   0,   0,   0,   0,   0,   0,   0,   0],
    }
)

en13445_docs = stress_en13445.table.cells