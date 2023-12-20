

# Here we include all the imports required from influxdb_client_3 
import pandas as pd
import random
from pyarrow.flight import FlightDescriptor, FlightClient
from pyarrow import flight
# These are just some library imports for Plotly so we can make use of the interactive graphs.
import plotly.express as px
import plotly.io as pio
import polars as pl


now =  pd.Timestamp.now(tz='+00:00').floor('ms')

# Lists of possible trainers
trainers = ["ash", "brock", "misty", "gary", "jessie", "james"]

# Read the CSV into a DataFrame. (Credit to @ritchie46 for the dataset)
pokemon_df = pd.read_csv("./pokemon.csv")

# Creating an empty list to store the data
data = []

# Dictionary to keep track of the number of times each trainer has caught each Pokémon
trainer_pokemon_counts = {}



num_entries = 100000 # You can reduce this if required. The more data the more interesting the results.
now =  pd.Timestamp.now(tz='+00:00').floor('ns')
data = []


# Generating random data
for i in range(num_entries):
    # Randomise the timestamp
    timestamp = now - pd.Timedelta(minutes=random.randint(0, 60))
    trainer = random.choice(trainers)
    
    # Randomly select a row from pokemon_df
    random_pokemon = pokemon_df.sample().iloc[0]
    caught = random_pokemon['Name']
    
    # Count the number of times this trainer has caught this Pokémon
    if (trainer, caught) in trainer_pokemon_counts:
        trainer_pokemon_counts[(trainer, caught)] += 1
    else:
        trainer_pokemon_counts[(trainer, caught)] = 1
    
    # Get the number for this combination of trainer and Pokémon
    num = trainer_pokemon_counts[(trainer, caught)]

    entry = {
        "trainer": trainer,
        "id": f"{0000 + random_pokemon['#']:04d}",
        "num": str(num),
        "name": caught,
        "level": random.randint(5, 20),
        "attack": random_pokemon['Attack'],
        "defense": random_pokemon['Defense'],
        "hp": random_pokemon['HP'],
        "speed": random_pokemon['Speed'],
        "type1": random_pokemon['Type 1'],
        "type2": random_pokemon['Type 2'],
        "timestamp": timestamp
    }
    data.append(entry)

# Convert the list of dictionaries to a DataFrame
caught_pokemon_df = pd.DataFrame(data)

# Print the DataFrame
pl_df = pl.from_pandas(caught_pokemon_df)

print(pl_df)

pl_df.write_parquet('pokemon_100_000.parquet')