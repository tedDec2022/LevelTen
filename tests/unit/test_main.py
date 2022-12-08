import pytest
from main import find_max_substring, print_results

test_cases = [
	{	'input': "defdefdef",
		'expected_set_output': {'def', 'efd', 'fde'},
		'expected_length': 3,
		'description': 'Tests a basic case with repeating 3 character term'
		},
	{	'input': "meowmeowmeow",
		'expected_set_output': {'meow', 'wmeo', 'eowm', 'owme'},
		'expected_length': 4,
		'description': 'Tests a basic case with repeating 4 character term'
		},
	{	'input': "ccccccc",
		'expected_set_output': {'c'},
		'expected_length': 1,
		'description': 'Tests a basic case with repeating single character'
		},
	{	'input': "defddefstuyt",
		'expected_set_output': {'defstuy'},
		'expected_length': 7,
		'description': 'Tests a basic case with a single long non-repeating term'
		},
	{	'input': "LevEl10Rocks",
		'expected_set_output': {'LevEl10Rocks'},
		'expected_length': 12,
		'description': ('Tests no repeating character and case sensitivity, '
						'assuming case must match to count as a repeating characters')
		},
	{	'input': "LevEl10!!nR0cks",
		'expected_set_output': {'LevEl10!'},
		'expected_length': 8,
		'description': 'Tests special characters are counted as characters'
		},
	{	'input': "",
		'expected_set_output': {''},
		'expected_length': 0,
		'description': 'Tests empty strings'
		},
	{	'input': "   ",
		'expected_set_output': {' '},
		'expected_length': 1,
		'description': 'Tests all spaces'
		},
	{	'input': "aabcd12345",
		'expected_set_output': {'abcd12345'},
		'expected_length': 9,
		'description': 'Tests repetition at start of string'
		},
	{	'input': "abcd123455",
		'expected_set_output': {'abcd12345'},
		'expected_length': 9,
		'description': 'Tests repetition at end of string'
		}

]

@pytest.mark.parametrize('param,', test_cases)
def test_find_max_substring(param):
	found_set, found_length = find_max_substring(param['input'])
	assert param['expected_set_output'] == found_set
	assert param['expected_length'] == found_length

@pytest.mark.parametrize('param,', [[], {}, 1 , 1.1, -1, True, False, None, Exception(), b'1'])
def test_find_max_substring_exceptions(param):
	with pytest.raises(Exception):
		find_max_substring(param)

def test_print_results():
	assert print_results({'Wind~Solar*stORAge :)'}, 21) == "{'Wind~Solar*stORAge :)'} with the length of 21."
