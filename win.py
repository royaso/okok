#!/usr/bin/env python
import pygtk
pygtk.require("2.0")
import gtk

class Base:
    def combo_text(self,widget):
        self.win.set_title(widget.get_active_text())

    def textchange(self,widget):
        self.win.set_title(self.textbox.get_text())

    def relabel(self,widget):
        self.label.set_text('xxxxxxxx')
        self.textbox.set_text('uuuu')

    def myhide(self,widget):
        self.button.hide()
        self.combo.append_text(self.textbox.get_text())

    def destroy(self,widget,data=None):
        print "dsafasdf"
        gtk.main_quit()

    def __init__(self):
        self.win=gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.win.set_position(gtk.WIN_POS_CENTER)
        self.win.set_size_request(333,1333)
        self.win.set_title("my title")
        self.win.set_tooltip_text("dasfsad\nuuuuuu")

        self.button=gtk.Button("exit")
        self.button.set_tooltip_text("aasaaa")
        self.button.connect("clicked",self.destroy)

        self.label=gtk.Label("dbalalalal")

        self.button2=gtk.Button("hide")
        self.button2.connect("clicked",self.myhide)
        
        self.button4=gtk.Button("relabel")
        self.button4.connect("clicked",self.relabel)

        #fixed=gtk.Fixed();
        #fixed.put(self.button,20,33)
        #fixed.put(self.button2,120,33)

        self.textbox=gtk.Entry()
        self.textbox.connect("changed",self.textchange)

        self.combo=gtk.combo_box_entry_new_text()
        self.combo.connect("changed",self.combo_text)
        self.combo.append_text("111")
        self.combo.append_text("222")

        self.pix=gtk.gdk.pixbuf_new_from_file_at_size("/home/roya/small.png",122,133)
        self.image=gtk.Image()
        self.image.set_from_pixbuf(self.pix)

        self.box=gtk.VBox()
        self.box.pack_start(self.button2)
        self.box.pack_start(self.button)
        self.box.pack_start(self.label)
        self.box.pack_start(self.button4)
        self.box.pack_start(self.image)

        self.box2=gtk.HBox()
        self.box2.pack_start(self.box)
        self.box2.pack_start(self.textbox)
        self.box2.pack_start(self.combo)

        self.win.add(self.box2)
        self.win.show_all()
        self.win.connect("destroy",self.destroy)

    def main(self):
        gtk.main()

if __name__ == "__main__":
    base=Base()
    base.main()
