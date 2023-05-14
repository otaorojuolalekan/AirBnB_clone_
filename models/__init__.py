#!/usr/bin/env python3
"""
this creates a unique FileStorage instance for my model
"""
from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()