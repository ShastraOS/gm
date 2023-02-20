# done.py
#
# Copyright 2022 mirkobrombin
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundationat version 3 of the License.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

import subprocess
import os
from sys import intern
from gi.repository import Gtk, Adw


@Gtk.Template(resource_path='/al/getcryst/FirstSetup/gtk/done.ui')
class VanillaDone(Adw.Bin):
    __gtype_name__ = 'VanillaDone'

    status_page = Gtk.Template.Child()
    btn_reboot = Gtk.Template.Child()
    btn_retry = Gtk.Template.Child()
    btn_close = Gtk.Template.Child()
    log_box = Gtk.Template.Child()
    log_output = Gtk.Template.Child()

    def __init__(self, window, log_file, reboot: bool=True, title: str="", description: str="", fail_title: str="", fail_description: str="", **kwargs):
        super().__init__(**kwargs)
        self.__window = window
        self.__fail_title = fail_title
        self.__fail_description = fail_description
        self.__log_file = log_file

        if not title and not description:
            self.status_page.set_description(
                _("Restart your device to enjoy your {} experience.").format(
                    self.__window.recipe["distro_name"]
                )
            )
        else:
            self.status_page.set_title(title)
            self.status_page.set_description(description)

        if reboot:
            self.btn_reboot.connect("clicked", self.__on_reboot_clicked)
        else:
            self.btn_reboot.set_visible(False)
            self.btn_close.set_visible(True)

        self.btn_close.connect("clicked", self.__on_close_clicked)
        self.btn_retry.connect("clicked", self.__on_retry_clicked)

    def set_result(self, result):
        if not result:
            self.status_page.set_title(self.__fail_title)
            self.status_page.set_description(self.__fail_description)
            self.btn_reboot.set_visible(False)
            self.btn_close.set_visible(True)
            self.log_box.set_visible(True)
            self.log_output.set_text(open(self.__log_file).read())
        else:
            self.log_box.set_visible(False)
            return

    def __on_reboot_clicked(self, button):
        if not "GNOME" in os.environ.get("XDG_CURRENT_DESKTOP"):
            subprocess.Popen(["reboot"])
        else:
            subprocess.run(['gnome-session-quit', '--reboot'])

    def __on_close_clicked(self, button):
        self.__window.close()

    def __on_retry_clicked(self, button):
        self.__window.back()
