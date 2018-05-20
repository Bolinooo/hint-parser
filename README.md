# hint-parser

hint-parser is a command-line application to crawl schedule-information from the Hogeschool Rotterdam and parse it to a .csv-file.

### Prerequisites

You'll need to install a couple of libraries.

```
~$ pip install beautifulsoup4
~$ pip install requests
```

Please note: make sure you are using python 3 in your environment.

### Usage

This application is easy to use. To run the main application apply the following command from your project directory:

```
~$ python3 run.py 'option' 'quarter'
```
(example)
```
~& python3 run.py teacher 1
```

### Output

The output will be in .csv-format. Small start-up for .json is included, but not finished yet.
Output for .csv per option can be set in src/main.py in the settings-dictionary.

### Tests

To make use of the written unittests, please apply the following command to test individual components.

```
~$ python3 -m unittest tests/testfile.py
```

Please note: Only use this command from your project directory. Do not use it from your /tests-dir.

## Built With

* [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - Python library for screen-scraping
* [Requests](https://maven.apache.org/) - Python HTTP library 

## License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/Bolinooo/hint-parser/blob/master/LICENSE) file for details
