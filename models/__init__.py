#!/usr/bin/python3
"""This module autoinit the FileStorage"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
