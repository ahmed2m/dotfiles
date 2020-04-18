Place to save configs to restore my environment/programs, Inspired by a number of dotfiles I saw.

It has three scripts:

  - `collect.sh` - to sync all configs in `list` and `list_files` from the system.
  - `commit.sh` - to commit the changes `collect.sh` made.
  - `spread.sh` - to sync all configs in `list` and `list_files` from github repo clone to the system
  - use `pacman -Qqetn > arch-pkglist.txt` to export arch pkgs
  - use `pacman -Qetm > arch-aur.txt` to export aur pkgs
  - use `sudo pacman -S - < arch-pkglist.txt` to restore the official packages 

TODO:

  - Setup params or some kind of rules to opt out configs for special setups like AWESOMEWM and Qtile and KDE
  - Find a way to track packages from other managers, snap and flatpak.
  - Find cleaner way to do bash :") or even shift to python 
