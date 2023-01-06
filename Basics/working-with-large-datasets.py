import pyarrow.dataset as ds


import pyarrow as pa

# Create a array from a list of values
animal = pa.array(["sheep", "cows", "horses", "foxes"], type=pa.string())
count = pa.array([12, 5, 2, 1], type=pa.int8())
year = pa.array([2022, 2022, 2022, 2022], type=pa.int16())

# Create a table from the arrays
table = pa.Table.from_arrays([animal, count, year], names=['animal', 'count', 'year'])
print(table)

# partitioning of your data in smaller chunks
ds.write_dataset(table, "savedir", format="parquet",
                 partitioning=ds.partitioning(
                    pa.schema([table.schema.field("year")])
                ))
# Loading back the partitioned dataset will detect the chunks                
table2 = ds.dataset("savedir", format="parquet", partitioning=["year"])
print(table2.files)