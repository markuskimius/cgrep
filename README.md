# cgrep
A command line utility to grep for blocks of text

This tool displays a block of text that matches a regex.

## Usage

```sh
usage: cgrep [-h] [-k PATTERN] [-i] [-v] PATTERN [FILE [FILE ...]]

grep blocks of text.

positional arguments:
  PATTERN               pattern to grep for.
  FILE                  file(s) to grep.

optional arguments:
  -h, --help            show this help message and exit
  -k PATTERN, --block-marker PATTERN
                        regex pattern describing the start of a block
                        (default=^$)
  -i, --ignore-case     ignore case distinctions
  -v, --invert-match    select non-matching blocks
```

## Example

Given the following file,
```
2018-10-05
Nothing interesting happened.

2018-10-06
cgrep released on github.

2018-10-07
Nobody knows what the future will bring.
```
Running cgrep on the file produces the following output:
```sh
$ cgrep 2018-10-06 diary.txt
2018-10-06
cgrep released on github.
```

By default, a *block* begins and ends with an empty line.
This default can be changed with the `-k` option.
