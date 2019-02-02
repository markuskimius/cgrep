# cgrep
A command line utility to grep for blocks of text

This tool displays a block of text that matches a regex.

## Usage

```
usage: cgrep [-h] [-k PATTERN] [-i] [-v] [--color] PATTERN [FILE [FILE ...]]

grep blocks of text.

positional arguments:
  PATTERN               pattern to grep for
  FILE                  file(s) to grep.

optional arguments:
  -h, --help            show this help message and exit
  -k PATTERN, --block-marker PATTERN
                        regex pattern describing the start of a block
                        (default=^$)
  -i, --ignore-case     ignore case distinctions
  -v, --invert-match    select non-matching blocks
  --color               use markers to highlight the matching strings
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

## Footnotes

cgrep was inspired by mgrep.  mgrep was (is?) a UNIX command line tool to grep
emails on UNIX accounts, stored as flat files in a format called "[mbox]".
mgrep-ing a pattern in an mbox displayed the entire email containing the
pattern.  cgrep is a generalized version of the mgrep that can grep for any
block of text and not just emails in an mbox.  Passing `-k '^From '` option to
cgrep is practically equivalent to mgrep.

The "c" in cgrep is largely historical.  It originally stood for "context".

[mbox]: https://en.wikipedia.org/wiki/Mbox
