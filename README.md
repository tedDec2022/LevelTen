## Max Substring Finder

Simple function to find the longest substring without repeating characters from a given string.

The algorithm starts from each character in the input string and starts a "reading session". During a "read session" characters subsequent to the starting character are read in order. If a character is new then it is added to a list of seen characters. If a character has already been seen, or we've reached the end of the input string, the "read session" is ended.
After a read session the list of seen characters is reconstituted into a term that is added to a storage dictionary. The keys in the storage dictionary are the unique lengths of the resulting terms from read sessions and the values are sets of term values. 

The function provides the maximum length of a term without repeating characters, and the set of terms as a result. A simple print function is also provided to format these results for printing to a string or logging.

Notes:
 - upper and lower case characters are treated as different characters
 - spaces, special characters and numbers (0-9) are treated as valid characters
 - the prompt identified `defddefstuyt` as having the longest non-repeating term of `defstuyt` at length 8. This seems suspect since that term has two `t`'s in it, so the code assumes the correct output here is `defstuy` at length 7.


### Running the code

The code has been tested in in Python `3.9` and `3.10`. Install Python dependencies with:
```
pip install -r requirements.txt
```

Run the code from command line with:
```
$ python main.py <input text>
```

Example:
```
$ python main.py LEVel10

> {'LEVel10'} with the length of 7.
```

### Testing the code

```
$ pytest
>
====================================================================================== test session starts =======================================================================================
platform darwin -- Python 3.9.0, pytest-7.2.0, pluggy-1.0.0
rootdir: /Users/Ted/Desktop/LevelTen
collected 19 items                                                                                                                                                                               

tests/unit/test_main.py ...................                                                                                                                                                [100%]

======================================================================================= 19 passed in 0.06s =======================================================================================

```
