# Crystal Linux First Setup
This utility is a fork of [Vanilla OS first-setup](https://github.com/Vanilla-OS/first-setup) and is meant to be used in [Crystal Linux](https://getcryst.al/site)</a> 
as a first-setup wizard. It's purpose is to help the user to configure the 
system to their needs, e.g. by configuring, flatpak, flathub, etc.

## 💡 Features

- Distro agnostic
- Uses accesssible technologies
- Easy to use

## 📚 Documentation

Documentation for this project is available [here](https://docs.getcryst.al)!

**Support** is also available in our [Discord](https://getcryst.al/discord) and the [Matrix](https://matrix.to/#/#space:getcryst.al). If you face any issues with the software, feel free to open an issue on this repository.

## 💾 Installation
### 🏗 From Source

**Install the dependencies**

```
# pacman -S meson ninja libadwaita desktop-file-utils appstream-glib gtk4 sudo polkit grub mkinitcpio
```

**Install first-setup from source using `meson`**
```bash
$ git clone https://git.getcryst.al/crystal/software/first-setup.git && cd first-setup
$ meson build
$ ninja -C build
```

 **Install first-setup using `ninja`**
```bash
# ninja -C build install
$ crystal-first-setup
```


**Using custom recipes**

Place a new recipe in `/etc/vanilla-first-setup/recipe.json` or launch the
utility with the `VANILLA_CUSTOM_RECIPE` environment variable set to the path
of the recipe.

## 📸 Screenshots

![App Screenshot](/data/screenshot-1.png)

## 🙌 Contributing

If you'd like to contribute to **First Setup**, please follow the [Crystal Linux contributing guidelines](https://git.getcryst.al/crystal/info/-/blob/main/CONTRIBUTING.md)!

We are also constantly looking for translators for our i18n-enabled projects! If you speak more than one language, consider helping out on our [Weblate](https://i18n.getcryst.al)!

![https://i18n.getcryst.al/engage/crystal-linux/](https://i18n.getcryst.al/widgets/crystal-linux/-/287x66-black.png)


## 📜 License

[GPLv3-only](https://choosealicense.com/licenses/gpl-3.0/)

![](https://git.getcryst.al/crystal/misc/branding/-/raw/main/banners/README-banner.png)
