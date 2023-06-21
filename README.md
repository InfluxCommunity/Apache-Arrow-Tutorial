<p align="center">
  <img src="https://arrow.apache.org/img/arrow-logo_vertical_black-txt_white-bg.svg" alt="Arrow Icon" width="200">
</p>

# Apache-Arrow-Tutorial

This repository provides a series of Apache Arrow examples taken from various locations. The examples aim to improve understanding of what Apache Arrow is and how InfluxDB leverages this technology.

## What is Apache Arrow?

Apache Arrow is a development platform for in-memory analytics. It contains a set of technologies that enable big data systems to process and transfer data quickly. Arrow’s main feature is its columnar in-memory data format, which is optimized for modern CPUs. This allows for efficient reading and writing of data, thereby accelerating analytics and machine learning workloads.

## What is Arrow Flight?

Arrow Flight is a framework for high performance data services built on top of Apache Arrow. It allows for the fast transfer of large datasets over network interfaces, reducing serialization overhead typically encountered with other data exchange protocols. This means you can move large datasets between applications and services with minimal latency, allowing for more real-time analytics capabilities.

## What is Apache Parquet?

Apache Parquet is a columnar storage file format available to any project in the Hadoop ecosystem. It provides efficient data compression and encoding schemes with enhanced performance to handle complex data in bulk. Parquet is optimized to work with complex data in bulk and allows for efficient storage and decoding. It is especially good when querying data with SQL-like query languages, making it a perfect fit for big data processing.

## Examples

The following table provides a list of the examples available in this repository. Click on the directory name to navigate to the respective examples.

| Name  | Description |
| ----- | ----------- |
| [AnomalyDetection](https://github.com/InfluxCommunity/Apache-Arrow-Tutorial/tree/main/AnomalyDetection) | Examples related to detecting anomalies in data |
| [FlightSQL_Client](https://github.com/InfluxCommunity/Apache-Arrow-Tutorial/tree/main/FlightSQL_Client) | Demonstrations of using Arrow Flight in a SQL client context |
| [FlightTrafficDemo](https://github.com/InfluxCommunity/Apache-Arrow-Tutorial/tree/main/FlightTrafficDemo) | Demonstrations related to flight traffic data, perhaps showcasing real-time analytics |
| [ML](https://github.com/InfluxCommunity/Apache-Arrow-Tutorial/tree/main/ML) | Machine Learning examples using Apache Arrow |
| [Pandas2](https://github.com/InfluxCommunity/Apache-Arrow-Tutorial/tree/main/Pandas2) | Examples showcasing the use of Apache Arrow with the Pandas library |
| [Polars](https://github.com/InfluxCommunity/Apache-Arrow-Tutorial/tree/main/Polars) | Examples using Polars, a DataFrame library implemented in Rust and Python, with Apache Arrow |
| [PyArrow](https://github.com/InfluxCommunity/Apache-Arrow-Tutorial/tree/main/PyArrow) | Examples using PyArrow, the Python implementation of Apache Arrow |
| [pyinflux3](https://github.com/InfluxCommunity/Apache-Arrow-Tutorial/tree/main/pyinflux3) | Examples using InfluxDB Python client with Apache Arrow |
| [pyspark](https://github.com/InfluxCommunity/Apache-Arrow-Tutorial/tree/main/pyspark) | Examples of integrating Apache Arrow with PySpark |
| [sqlal](https://github.com/InfluxCommunity/Apache-Arrow-Tutorial/tree/main/sqlal) | Examples of using SQL Alchemy with Apache Arrow |

## Contributing

We warmly welcome and appreciate contributions from the community! Whether it's enhancing existing examples, adding new ones, fixing bugs, or improving documentation, every contribution helps make this project better.

Before contributing, please ensure you have read and understood our [Contribution Guidelines](./CONTRIBUTING.md).

To get started:

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/YourFeature`)
3. Commit your changes (`git commit -am 'Add some feature'`)
4. Push to the branch (`git push origin feature/YourFeature`)
5. Open a new Pull Request

Thank you for your interest in contributing to FlowForge examples!
