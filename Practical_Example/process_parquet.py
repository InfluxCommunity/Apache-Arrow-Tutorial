import pyarrow.dataset as ds

# Loading back the partitioned dataset will detect the chunks                
usgs = ds.dataset("usgs", format="parquet", partitioning=["_measurement"])
print(usgs.files)

# Convert to a table
usgs = usgs.to_table()
print(usgs)

# Grouped Aggregation example
aggregation = usgs.group_by("_measurement").aggregate([("rms", "mean"), ("rms", "max"), ("rms", "min") ]).to_pandas()
print(aggregation)
