import time
class timer:
    def __init__(self):
        self.start_time = time.time()
        self.end_time = None
        self.elapsed_time = None

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end_time = time.time()
        self.elapsed_time = self.end_time - self.start_time
        print('Execution time:', self.elapsed_time, 'seconds')
        return self.elapsed_time
    

def update_spark_log_level(spark, log_level='info'):
        spark.sparkContext.setLogLevel(log_level)
        log4j = spark._jvm.org.apache.log4j
        logger = log4j.LogManager.getLogger("my custom Log Level")
        return logger