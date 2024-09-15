# VortaroES

A simple application that allows you to access the RAE dictionary, made in Tkinter.

# TODO List

- [ ] Add esperanto dictionary
- [ ] Add English dictionary
- [ ] Add languages to interface

*Advertasing*: Now the application only support search from the search bar but no if you click in the links, that won't work
# AppImage
The AppImage versions (for GNU/Linux users) need `tkinter`, which can be installed with these commands depending on the distro:

```
sudo apt install python3-tk #Ubuntu, Debian, elementary OS, Pop!_OS
sudo dnf install python3-tkinter #Fedora, Ultramarine
sudo zypper install python311-tk #openSUSE
sudo pacman -S tk #Arch, Manjaro, Endeavour OS
```

# Contribution guidelines
- Clone this repository.
```bash
git clone https://codeberg.org/mester/vortaroES.git
```
- Install Tkinter as explained in the section above.
- Create a virtual environment and install the dependencies.
```bash
# On GNU/Linux
python3 -m venv .
source ./bin/activate
./bin/python -m pip install -r requirements.txt
```
- Since the only branch currently available is `main`, make your changes there.
- Ensure everything works and add a summary of your changes in the beginning of the file `CHANGELOG.txt` according to the following format:
```
<ISO DATE> <Author>
    - <Change 1>
    - <Change 2>
    - <Change n>
```
- Create a [Pull Request](https://codeberg.org/mester/vortaroES/pulls).