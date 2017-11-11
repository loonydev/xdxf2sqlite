# xdxf2sqlite

Not so long ago it took me to work with XDXF, but for my programm needed more than just XML, so I write simple script for translate it into SQLite batabase

## Getting Started
Here is an example of my command

```
python xdxf2sqlitedb.py -i dict.xdxf -o test.db -d dictionary -k KEY -a ANS
```

Now let's look at the parameters:
```
-i - File for conversion in format XDXF
```
```
-o - Output file with\for SQLite database
```
```
-d - Name of the table
```
```
-k - Name of the key column
```
```
-a - Name of the answer column
```

## Authors

* **Andrew Artyushok** - *All work* - [loonydev](https://github.com/loonydev)

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details
