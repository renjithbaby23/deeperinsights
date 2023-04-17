# Solution
Solution for deeper insights assignment.


### Assumptions
1. Valid words and search terms are comprised of characters from "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
2. Search term is always a string of characters and do not require formatting
   * correct search terms - 's', 'sa', 'sample'
   * incorrect search terms - '1s', 'sa12#', 'sa mple'
3. The text and search term can be matched irrespective of their case
   * eg: 'Test', 'test' and 'TEST' are all match for the search term 'test'
4. The result will be displayed with the original case (will not be converted to lower case for outputting the result.)
5. Exactly three words are expected per line of the input source text; else, exceptions will be raised
6. Expecting the whole text file size to be small enough to fit into the memory

### Solution:
The solution is built with mainly three components;
1. file parser
2. content formatter
3. pattern matcher


#### file parser
The `TextFileParser` class which is derived from the `FileParser` abstract class
is responsible for parsing the input file and ensuring it is a valid file.
The parsing process includes opening and reading the file contents and
extracting `source_text` and `search_term`. It raises `FileNotFoundError`
if the file is not found. It also raises `ValueError` if it doesn't contain any `source_text` and `search_term`


#### content formatter
`TextContentFormatter` class which is derived from `ContentFormatter` is
the abstraction for formatting and filtering out the words from the `source_text`.
It ensures the assumptions are met before formatting and ensures exactly three words
are present there in each line of the `source_text`.


#### pattern matcher
The pattern matcher module takes care of the
pattern matching and prints matching line in the expected format and order.

#### Tests
The tests are organised in `./tests/` directory. You can run them directly using pytest or use `make test` to run them.
Ensure that the project environment and prerequisites are ready by
running the command `make install` and activate the poetry shell using `make activate`.

#### Code quality
Static code quality is ensured using
flake8, black, mypy etc via pre-commit hooks.


### How to install the solution package?
1. Requirements:
   1. python 3.8 or higher
   2. [poetry](https://python-poetry.org/docs/)
2. Unzip the DeeperInsights.zip file provided
3. Enter the unzipped directory ```cd DeeperInsights```
4. Run ```make install``` to build and install the solution package

   *Note: If the make install fails int the first attempt, try running it one more time before manually installing the package using the following commands.*


   The `make install` command is equivalent to the following commands running one after the other;
   * Run ```poetry install``` to install the dependencies
   * Use poetry to build the solution by running ```poetry build```
   * The installable `.whl` file will be available here ```DeeperInsights/dist/solution-0.1.0-py3-none-any.whl```
   * Install the whl file using pip (in a python 3.8 virtual environment)
   ```pip install dist/solution-0.1.0-py3-none-any.whl```
6. Now you can run ```solution <path_to_text_file.txt>``` to execute the solution

*Note: The solution libray is not hosted publicly anywhere in github or similar code hosting platforms.
But I used a personal git repository to make the development process easier.*
