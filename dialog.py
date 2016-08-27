#!/usr/bin/env python

import gtk, pygtk
if gtk.pygtk_version < (2,3,90):
    print 'upgrade gtk'
    raise SystemExit

dialog=gtk.FileChooserDialog('title open',None,
        gtk.FILE_CHOOSER_ACTION_OPEN,
        (gtk.STOCK_CANCEL,gtk.RESPONSE_CANCEL,
        gtk.STOCK_OPEN,gtk.RESPONSE_OK))

dialog.set_default_response(gtk.RESPONSE_OK)
filter=gtk.FileFilter()
filter.set_name("all file you")
filter.add_pattern("*")
dialog.add_filter(filter)


response=dialog.run()
if response == gtk.RESPONSE_OK:
    print dialog.get_filename(),'you ok'
elif response == gtk.RESPONSE_CANCEL:
    print 'you cancel'
