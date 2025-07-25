import pytest
from palindrome import longest_palindromic_substring

def test_palindrome():
	assert longest_palindromic_substring("babad") == "bab"
	assert longest_palindromic_substring("cbbd") == "bb"
	assert longest_palindromic_substring("") == ""
	assert longest_palindromic_substring("t*st") == ""