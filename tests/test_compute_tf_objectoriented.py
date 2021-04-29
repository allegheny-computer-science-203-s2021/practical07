"""Test cases for the object-oriented implementation."""

import pytest

from termfrequency import compute_tf_objectoriented

# TODO: Add more test cases, for a total of at least 5 with at least 1 parameterized test

def test_read_file_populates_data_0():
    """ Checks that the reading of the small text file works """
    storage_manager = compute_tf_objectoriented.DataStorageManager("inputs/input.txt")
    word_list = storage_manager.words()
    assert word_list is not None
    assert len(word_list) == 12

def test_check_stop_word():
    """Checks that the word is identified as a stop word correctly."""
    stop_word_manager = compute_tf_objectoriented.StopWordManager()
    stop_word = stop_word_manager.is_stop_word("were")
    assert stop_word
