# Shell - Permissions

*Description or function of all the programs in this directory are listed below.*

* 0-iam_betty:- a script that switches the `current user` to the user `betty`.

* 1-who_am_i:- a script that prints the `effective username` of the `current user`.

* 2-groups:-  a script that prints all the `groups` the `current user` is part of.

* 3-new_owner:-  a script that `changes` the `owner` of the file `hello` to the user `betty`.

* 4-empty:- a script that `creates` an `empty file` called `hello`.

* 5-execute:- a script that adds `execute permission` to the `owner` of the file `hello`.

* 6-multiple_permissions:- a script that adds `execute permission` to the `owner` and the `group owner`, and `read permission` to `other users` to the file `hello`.

* 7-everybody:- a script that adds `execution permission` to the `owner`, the `group owner` and the `other users`, to the file `hello`.

* 8-James_Bond :- a script that `sets` the `permission` to the file `hello` as follows:
  * __Owner__: `no permissions`
  * __Group__: `no permissions`
  * __Other users__: `all permissions`

* 9-John_Doe :- a script that `sets` the `mode` of the file `hello` to this:
```
-rwxr-x-wx 1 kidusmik kidusmik 05 Sep 21 12:16 hello
```
* 10-mirror_permissions :- a script that `sets` the `mode` of the file `hello` the same as `olleh`’s `mode`, both the f iles are located in the same directory.

* 11-directories_permissions :- a script that adds `execute permission` to all `subdirectories` of the `current directory` for the `owner`, the `group owner` and all `other users`. Regular files will not be changed.

* 12-directory_permissions :- a script that creates a `directory` called `my_dir` with permissions `in the working directory.

* 13-change_group :- a script that `changes` the `group owner` to `school` for the file `hello`.

* 100-change_owner_and_group :- a script that `changes` the `owner` to `vincent` and the `group owner` to `staff` for all the `files` and `directories` in the working directory.

* 101-symbolic_link_permissions :- a script that `changes` the `owner` and the `group owner` of file `_hello` to `vincent` and `staff` respectively, the file `_hello` is a `symbolic link`.

* 102-if_only :- a script that `changes` the `owner` of the file `hello` to `betty` only if it is owned by the user `guillaume`.

* 103-Star_Wars :- a script that will `play` the `StarWars IV` episode in the `terminal`.
