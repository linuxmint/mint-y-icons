
Credits
=======

The mimetype icons originate from the Elementary icon theme:

* Link: https://github.com/elementary/icons
* Author: Members of the Elementary OS team (https://github.com/orgs/elementary/people)
* License: GPLv3 (https://choosealicense.com/licenses/gpl-3.0/)

The applications, categories, devices, places, action and panel icons originate and inspired from the Papirus theme:

* Link: https://github.com/PapirusDevelopmentTeam/papirus-icon-theme
* Author: Members of the Papirus Development Team (https://github.com/orgs/PapirusDevelopmentTeam/people)
* License: GPLv3 (https://choosealicense.com/licenses/gpl-3.0/)

License
=======

This theme is licensed under Creative Commons Attribution-ShareAlike 4.0 (https://creativecommons.org/licenses/by-sa/4.0).

Any bundled software is free software; you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation; either version 3, or (at your option) any later version.

Custom color variants
=====================

You can generate your own Mint-Y icon colors theme easily.

Say you want to generate a "Suse" theme with these colors:

![image](https://user-images.githubusercontent.com/1138515/236241924-0552bebc-0d5c-4167-b8dd-444c76a8554e.png)

1. Go to `src/places`
2. In `generate-color-variations.py`, each `VARIANTS.append({...})` line defines a color variant.
3. Add an extra line with the proper name and color codes and save the file. For instance, to make the Suse theme you would add this line:

```
VARIANTS.append({"name":"Suse","folder":"183f50","backfolder":"00a489","paper":"e4e4e4","emblem":"e4e4e4"})
```

4. Run `./generate-color-variations.py`. This generates `Suse.svg`.
3. Run `./render_places.py Suse`. This generates the new icon theme in `../../usr/share/icons/Mint-Y-Suse`.
4. You can test your theme by copying it to `/usr/share/icons/` or `~/.icons/`
6. This theme only contains places icons, but it inherits Mint-Y, so you can package it or distribute it to anyone who already has Mint-Y installed.

How to Contribute
===============

Read [here](src/README.md).

Useful commands
===============

To find circular symbolic links:

	find . -follow -printf ""

To find broken links use `./deadlinks` or:

	find -L usr/ -type l

To find files with spaces in their filenames (that breaks the icon cache generation):

	find . | egrep '. '
