import pandas as pd
import pymongo
from pymongo import MongoClient
import os, sys
from src.constants import *
from src.exception import CustomException


class MongoIO:
    mongo_ins = None
    db = None

    def __init__(self):
        if MongoIO.mongo_ins is None:
            # Default to MongoDB Atlas cloud connection (password URL-encoded)
            default_atlas_url = "mongodb+srv://SaralTripathi:Saral%4012345@cluster0.shmedgm.mongodb.net/?retryWrites=true&w=majority"
            mongo_db_url = os.getenv(MONGODB_URL_KEY, default_atlas_url)
            MongoIO.mongo_ins = MongoClient(mongo_db_url)
            MongoIO.db = MongoIO.mongo_ins[MONGO_DATABASE_NAME]
        self.mongo_ins = MongoIO.mongo_ins
        self.db = MongoIO.db

    def store_reviews(self,
                      product_name: str, reviews: pd.DataFrame):
        try:
            # Store data in MongoDB Atlas (cloud only)
            collection_name = product_name.replace(" ", "_")
            collection = self.db[collection_name]
            
            # Convert DataFrame to list of dictionaries
            reviews_dict = reviews.to_dict('records')
            
            # Insert documents
            if reviews_dict:
                collection.insert_many(reviews_dict)
                print(f"✅ Data saved to MongoDB Atlas collection: {collection_name}")
                print(f"📊 Database: {self.db.name}")
                print(f"🔗 Cluster: cluster0.shmedgm.mongodb.net")

        except Exception as mongo_e:
            raise CustomException(f"MongoDB Atlas storage failed: {mongo_e}", sys)

    def get_reviews(self,
                    product_name: str):
        try:
            # Read from MongoDB Atlas only
            collection_name = product_name.replace(" ", "_")
            collection = self.db[collection_name]
            data = list(collection.find())
            
            if data:
                # Convert MongoDB documents to DataFrame
                data_df = pd.DataFrame(data)
                # Remove MongoDB's _id field if present
                if '_id' in data_df.columns:
                    data_df = data_df.drop('_id', axis=1)
                return data_df
            else:
                return pd.DataFrame()  # Return empty DataFrame if no data found

        except Exception as e:
            raise CustomException(f"MongoDB Atlas retrieval failed: {e}", sys)


