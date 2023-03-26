import pyarrow as pa
import pyarrow.compute as pc
import polars as pl

# Create a array from a list of values
animal = pa.array(["sheep", "cows", "horses", "foxes", "sheep"], type=pa.string())
count = pa.array([12, 5, 2, 1, 10], type=pa.int8())
year = pa.array([2022, 2022, 2022, 2022, 2021], type=pa.int16())

# Create a table from the arrays
table = pa.Table.from_arrays([animal, count, year], names=['animal', 'count', 'year'])

pl.from_arrow(table)

