"""Seed file to make sample data for db."""

from models import Pet, db
from app import app

# Create all tables
db.drop_all()
db.create_all()

dog_url = "https://images.unsplash.com/photo-1561037404-61cd46aa615b?q=80&w=2070&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
cat_url = "https://images.unsplash.com/photo-1514888286974-6c03e2ca1dba?q=80&w=2043&auto=format&fit=crop&ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D"
porcupine_url = "https://unsplash.com/photos/close-up-photo-of-brown-puffin-fish-IKFVzqVNGK0?utm_content=creditShareLink&utm_medium=referral&utm_source=unsplash"

# Add sample pets
pd = Pet(name='Doug', species='dog', photo_url= dog_url, age=5, notes="He is a good boy")
pc = Pet(name='Alice', species='cat', photo_url=cat_url, age=11, notes="She is a cat")
pp = Pet(name='Larry', species='porcupine', photo_url= porcupine_url, age=5, notes="Not a fish")

db.session.add_all([pd, pc, pp])
db.session.commit()
