# Shell - I/O Redirections and Filters

*Description or function of all the programs in this directory are listed below.*

* 0-hello_world :- a script that prints `Hello, World`, followed by a new line to the `standard output`.

* 1-confused_smiley :- a script that displays a `confused smiley` (`"(Ôo)'`).

* 2-hellofile :- Display the `content` of the `/etc/passwd` file.

* 3-twofiles :- Display the content of `/etc/passwd` and `/etc/hosts`.

* 4-lastlines :- Display the `last 10 lines` of `/etc/passwd`.

* 5-firstlines :- Display the `first 10 lines` of `/etc/passwd`.

* 6-third_line :- a script that displays the `third line` of the file `iacta`.

* 7-file :- a script that creates a file named exactly `\*\\'"Best School"\'\\*$\?\*\*\*\*\*:)` containing the text `Best School` ending by a new line.

* 8-cwd_state :- a script that `writes` into the file `ls_cwd_content` the `result` of the command `ls -la`. If the file `ls_cwd_content` already exists, it `overwrittes` it and if the file `ls_cwd_content` does not exist, `creates` it.

* 9-duplicate_last_line :- a script that `duplicates` the `last line` of the file `iacta`.

* 10-no_more_js :- a script that `deletes` all the `regular files` (not the `directories`) with a `.js` extension that are present in the `current` directory and all its `subfolders`.

* 11-directories :- a script that `counts` the `number` of `directories` and `sub-directories` in the `current` directory.
  * The `current` and `parent` directories are not taken into account
  * `Hidden` directories are also counted

* 12-newest_files :- a script that `displays` the `10 newest files` in the `current` directory, and:
  * displayed one file per line
  * `sorted` from the newest to the oldest

* 13-unique :- a script that takes a `list of words` as `input` and prints only words that appear exactly `once`.
  * Input format: One line, one word
  * Output format: One line, one word
  * Words are sorted

* 14-findthatword :- Displays `lines` containing the pattern `root` from the file `/etc/passwd`.

* 15-countthatword :- Displays the number of `lines` that contain the pattern `bin` in the file `/etc/passwd`.

* 16-whatsnext :- Displays `lines` containing the pattern `root` and `3 lines` after them in the file `/etc/passwd`.

* 17-hidethisword :- Displays all the lines in the file `/etc/passwd` that do not contain the pattern `bin`.

* 18-letteronly :- Displays all lines of the file `/etc/ssh/sshd_config` starting with a `letter` and also lines that include `capital letters` as well.

* 19-AZ :- Replace all characters `A` and `c` from `input` to `Z` and `e` respectively.

* 20-hiago :- a script that `removes` all letters `c` and `C` from `input`.

* 21-reverse :- a script that `reverse` its `input`.

* 22-users_and_homes :- a script that displays all `users` and their `home directories`, sorted by `users` based on the the `/etc/passwd` file.

* 100-empty_casks :- a command that `finds` all `empty` files and directories in the `current` directory and all `sub-directories` and:
  * Only the `names` of the files and directories are displayed (not the entire path)
  * `Hidden` files are listed
  * One file name per line
  * The listing should end with a new line

* 101-gifs :- a script that lists all the files with a `.gif` extension in the `current` directory and all its sub-directories.
  * `Hidden` files should be listed
  * Only regular files (not directories) should be listed
  * The names of the files should be displayed without their extensions
  * The files should be `sorted` by `byte values`, but `case-insensitive` (Example: File `aaa` is listed before file `bbb`, File `.b` should be listed before file `a`, and File `Rona` should be listed after File `jay`)
  * One file name per line
  * The listing should end with a new line

* 102-acrostic :- a script that `decodes` `acrostics` that use the `first letter` of each line.

* 103-the_biggest_fan :- a script that `parses` web servers `logs` in `TSV` format as `input` and displays the `11` hosts or `IP addresses` which did the most `requests`.
