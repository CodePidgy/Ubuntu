# system imports --------------------------------------------------------------------------------- #
import subprocess

subprocess.call(["sudo", "apt", "update"])

desktop = ["dconf-editor", "gnome-shell-extension-manager", "gnome-tweaks", "gparted"]

subprocess.call(["sudo", "apt", "install", "-y"] + desktop)
