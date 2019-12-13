### import Python scripts and/or Python Modules - i.e.:    import myPythonScript
import nuke
import sys

import os
from ambassadors.menu.utils import build_menu

### add menu item to existing Nuke menu - i.e.:    nodeMenu = nuke.menu('Nuke').findItem('Edit/Node').addCommand('myMenuElement', 'myPythonScript.myFunction()', 'myHotkey')    # Modifiers: Shift= shift+, Alt/Option = alt+, Control/Command = ctrl+

dennis_menu_map = [
    ("customcontactsheet", "import customcontactsheet; reload(customcontactsheet); customcontactsheet.custom_contactsheet()", "alt+ctrl+c"),
    ("basic_ui", "import basic_ui; reload(basic_ui); basic_ui.showpanel()")
]

build_menu("Dennis", dennis_menu_map)