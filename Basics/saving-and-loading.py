import pyarrow as pa
import pyarrow.parquet as pq

# Create a array from a list of values
animal = pa.array(["sheep", "cows", "horses", "foxes"], type=pa.string())
count = pa.array([12, 5, 2, 1], type=pa.int8())
year = pa.array([2022, 2022, 2022, 2022], type=pa.int16())

# Create a table from the arrays
table = pa.Table.from_arrays([animal, count, year], names=['animal', 'count', 'year'])

# Save the table to a Parquet file
pq.write_table(table, 'example.parquet')

# Load the table from the Parquet file
table2 = pq.read_table('example.parquet')
print(table2)