import pyarrow as pa
import pyarrow.compute as pc

# Create a array from a list of values
animal = pa.array(["sheep", "cows", "horses", "foxes", "sheep"], type=pa.string())
count = pa.array([12, 5, 2, 1, 10], type=pa.int8())
year = pa.array([2022, 2022, 2022, 2022, 2021], type=pa.int16())

# Create a table from the arrays
table = pa.Table.from_arrays([animal, count, year], names=['animal', 'count', 'year'])



count_y = pc.value_counts(table['animal'])
print(count_y)

# More example on this later...