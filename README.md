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


### How to install
1. Requirements:
   1. python 3.8 or higher
   2. [poetry](https://python-poetry.org/docs/)
2. Unzip the DeeperInsights.zip file provided
3. Enter the unzipped directory ```cd DeeperInsights```
4. Use poetry to build the solution ```poetry build```
5. The installable .whl file will be available in ```DeeperInsights/dist/solution-0.1.0-py3-none-any.whl```
6. Install the whl file using pip in the python 3.8 virtual environment ```pip install dist/solution-0.1.0-py3-none-any.whl```
7. Now you can run ```solution <path_to_text_file.txt>``` to run the solution
