# -*- coding: utf-8 -*-
from ui import ui_elements
from ui import ui_handler


class my_text(ui_elements.Text):

	def start(self, args):
		self.set_text(args["text"])
		self.set_pos((0, 0))
		self.set_size(60)
		self.set_color((0, 0, 255))

	def mouse_over(self):
		pos = self.get_pos()
		new_pos = (pos[0] + 1, pos[1] + 1)
		self.set_pos(new_pos)


def init(screen):
	MyText = my_text(text="Just a Test UI element")
	my_handler = ui_handler.Handler(screen)
	my_handler.register(MyText)
	return my_handler