# Random ID

[![Build Status](https://travis-ci.com/AlexiWolf/random_id.svg?branch=main)](https://travis-ci.com/AlexiWolf/random_id)

A simple, flexible random ID generator.

## Installation

```
pip install random_id
```

## Basic Usage

### Importing

```Python
from random_id import *
```

Or

```Python
from random_id import random_id
```

### Generating IDs

Call with no arguments for default settings.

```Python
random_id()
# -> 'Y4M460zrRMqRuv'
```

Default IDs are 14 characters long and contain lower/uppercase ascii letters and numbers only (to be URL-safe.)

You can also customize the length and the character set used.

```Python
random_id(length=4)
# -> 'Dl3d'

random_id(character_set="abc")
# -> 'bbacabccaaacab'

random_id(length=8, character_set=string.digits)
# -> '27244839'
```

## License

Random ID is licensed under the [GNU General Public License version 3 or higher](COPYING.txt).
