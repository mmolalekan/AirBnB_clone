#!/usr/bin/python3
"""special method __init__ for the models directory"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
