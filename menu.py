'''

menu.py for Ben McEwan's Tools

'''

import nuke
import os

# Add Plugin Paths
nuke.pluginAddPath('./gizmos')
nuke.pluginAddPath('./gizmos/icons')
nuke.pluginAddPath('./python')

# Stores file path of menu.py
file_path = os.path.dirname(__file__)

# Creates "Ben McEwan" menu in the toolbar
toolbar = nuke.menu( 'Nodes' )
toolbar.addMenu( 'Ben McEwan', icon= 'bmicon.png' )

# Adds Ben's gizmos and nuke scripts, except the ones already in Nuke Survival Toolkit
toolbar.addCommand( "Ben McEwan/bm_EdgeMatte", "nuke.createNode('bm_EdgeMatte')", icon='bm_EdgeMatte_icon.png' )
toolbar.addCommand( "Ben McEwan/bm_OpticalLightwrap", "nuke.createNode('bm_OpticalLightwrap')", icon='bm_OpticalLightwrap_icon.png' )
toolbar.addCommand( "Ben McEwan/Breakdownerizationer", "nuke.createNode('Breakdownerizationer')" )
toolbar.addCommand( "Ben McEwan/DeepMerge_Advanced", "nuke.createNode('DeepMerge_Advanced')" )
toolbar.addCommand( "Ben McEwan/Cloudtastic", "nuke.nodePaste(\"" + os.path.join(file_path + "/gizmos/Cloudtastic.nk") + "\")")

# Imports Ben's python scripts
import bm_AutoContactSheet
import bm_CurveUtilities
import bm_EnableTrackerTRS
import bm_JumpToKeyframe
import bm_MultiIBK
#import bm_NodeComment
import bm_NodeSandwich
import bm_NukeColourConverter
import bm_OperationSwitcher
import bm_QuickKeys
import bm_SmartMerge
import bm_Smoothie
import bm_SwapInOut
import bm_ViewerToggle
#import netCopy