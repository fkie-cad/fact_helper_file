# FACT helper file

This library offers two functions:

```python
from fact_helper_file import get_file_type_from_binary, get_file_type_from_path

get_file_type_from_binary(b'[...]')
get_file_type_from_path('/path/to/file')
```

The result is a dictionary with keys `['mime', 'full']` offering full file type string as well as mime string.

Why use? Because the library uses the extended magic library of [FACT](https://github.com/fkie-cad/FACT_core) as default before falling back on the system magic library if nothing is detected.


## Acknowledgments
This project is partly financed by [German Federal Office for Information Security (BSI)](https://www.bsi.bund.de) and others.

## License
```
    Firmware Analysis and Comparison Tool (FACT) extractor
    Copyright (C) 2015-2019  Fraunhofer FKIE

    This program is free software: you can redistribute it and/or modify
    it under the terms of the GNU General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    This program is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU General Public License for more details.

    You should have received a copy of the GNU General Public License
    along with this program.  If not, see <http://www.gnu.org/licenses/>.

    Some plug-ins may have different licenses. If so, a license file is provided in the plug-in's folder.
```
