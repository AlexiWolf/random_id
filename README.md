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

Copyright (C) 2020 AlexiWolf

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.