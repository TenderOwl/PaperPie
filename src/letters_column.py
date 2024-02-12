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

from .letter_row import LetterRow
from .letter import Letter

@Gtk.Template(resource_path='/com/tenderowl/paperpie/ui/letters_column.ui')
class LettersColumn(Gtk.Box):
    __gtype_name__ = 'LettersColumn'

    list_view: Gtk.ListView = Gtk.Template.Child()
    list_store: Gio.ListStore = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        self.list_view.remove_css_class('view')
        self.list_store = self.populate_store(self.list_store)

    
    def populate_store(self, store: Gio.ListStore) ->  Gio.ListStore:
        store.remove_all()

        letters = [
            Letter(subject='Letter 1', body='Letter 1 content', sender='Adam W', received='8:32'),
            Letter(subject='Letter 2', body='Letter 2 content', sender='Maria F', received='7:14'),
            Letter(subject='Letter 3', body='Letter 3 content', sender='Adam W', received='yesterday'),
            Letter(subject='Letter 4', body='Letter 4 content', sender='Johnny M', received='yesterday'),
            Letter(subject='Letter 5', body='Letter 5 content', sender='Steve A', received='10.02.2024'),
            Letter(subject='Letter 6', body='Letter 6 content', sender='Thom Y', received='08.02.2024'),
        ]

        for letter in letters:
            store.append(letter)

        return store

    @Gtk.Template.Callback()
    def _on_item_setup(self, factory, item: Gtk.ListItem):
        label = LetterRow()
        item.set_child(label)

    @Gtk.Template.Callback()
    def _on_item_bind(self, factory, item: Gtk.ListItem):
        row: LetterRow = item.get_child()
        value: Letter = item.get_item()

        row.avatar.set_text(value.sender)
        row.sender_label.set_label(value.sender)
        row.subject_label.set_label(value.subject)
        row.body_label.set_label(f'{value.body}')
        row.received_label.set_label(value.received)
        