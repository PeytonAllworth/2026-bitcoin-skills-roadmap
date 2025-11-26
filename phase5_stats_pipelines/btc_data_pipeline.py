"""
Bitcoin Data Pipeline

Goal: Build a robust ETL pipeline for Bitcoin data
Skills: API integration, SQLite, data cleaning, error handling
"""

import requests
import sqlite3
import pandas as pd
from datetime import datetime
import time


class BitcoinDataPipeline:
    """
    A pipeline for fetching, transforming, and storing Bitcoin data.
    """
    
    def __init__(self, db_path='bitcoin_data.db'):
        """Initialize the pipeline with a database path."""
        self.db_path = db_path
        self.conn = None
        
    def connect_db(self):
        """Connect to SQLite database."""
        self.conn = sqlite3.connect(self.db_path)
        return self.conn
    
    def close_db(self):
        """Close database connection."""
        if self.conn:
            self.conn.close()
    
    def fetch_data(self, endpoint, params=None):
        """
        Fetch data from API endpoint.
        
        TODO: Implement API calls
        """
        pass
    
    def transform_data(self, raw_data):
        """
        Transform raw data into clean format.
        
        TODO: Implement data transformation
        """
        pass
    
    def load_data(self, data, table_name):
        """
        Load data into SQLite database.
        
        TODO: Implement data loading
        """
        pass
    
    def run_pipeline(self):
        """
        Execute the full ETL pipeline.
        
        TODO: Implement pipeline orchestration
        """
        pass


if __name__ == "__main__":
    # Example usage
    pipeline = BitcoinDataPipeline()
    # TODO: Add pipeline execution

