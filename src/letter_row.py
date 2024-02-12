# MIT License
#
# Copyright (c) 2024 Andrey Maksimov
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.
#
# SPDX-License-Identifier: MIT

from gi.repository import Adw
from gi.repository import Gtk, Gio


@Gtk.Template(resource_path='/com/tenderowl/paperpie/ui/letter_row.ui')
class LetterRow(Gtk.Box):
    __gtype_name__ = 'LetterRow'

    avatar: Adw.Avatar = Gtk.Template.Child()
    sender_label: Gtk.Label = Gtk.Template.Child()
    subject_label: Gtk.Label = Gtk.Template.Child()
    body_label: Gtk.Label = Gtk.Template.Child()
    received_label: Gtk.Label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
