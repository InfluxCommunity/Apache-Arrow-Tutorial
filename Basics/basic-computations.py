import pyarrow as pa
import pyarrow.compute as pc

# Create a array from a list of values
days = pa.array([1, 12, 17, 23, 28], type=pa.int8())
months = pa.array([1, 2, 3, 4, 5], type=pa.int8())
years = pa.array([2015, 2015, 2016, 2016, 2017], type=pa.int16())

# Create a table from the arrays
table = pa.Table.from_arrays([days, months, years], names=['day', 'month', 'year'])
print(table)


count_y = pc.value_counts(table['year'])
print(count_y)

# More example on this later...