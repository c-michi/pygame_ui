# -*- coding: utf-8 -*-
import pygame


class Text():

	def __init__(self, **kwargs):
		self._layer = 0
		self._text = ""
		self._pos = (0, 0)
		self._text_size = 10
		self._text_font = None
		self._color = (255, 255, 255)
		self._bold = False
		self._italic = False
		self._underline = False
		self._align = "center"
		self._antialias = True
		self._background = None  # currently no use
		self.status = 2
		self._generate_font()
		self._render_text()
		self._generate_rect()
		self.start(kwargs)

	def _generate_font(self):
		self._font = pygame.font.SysFont(self._text_font, self._text_size, self._bold, self._italic)
		self.status = 1

	def _render_text(self):
		self._surf = self._font.render(self._text, self._antialias, self._color)
		self.status = 0

	def _generate_rect(self):
		self._rect = self._surf.get_rect()
		if self._align == "center":
			self._rect.center = self._pos
		elif self._align == "bottom_right":
			self._rect.topleft = self._pos
		#TODO add all possibilities
		self.status = 0

	def _blittosurf(self, surface):
		if self.status > 0:
			if self.status == 2:
				self._generate_font()
			if self.status == 1:
				self._render_text()
			self._generate_rect()
		elif self.status == 0:
			surface.blit(self._surf, self._rect)

	def set_layer(self, layer):
		"""Sets the layer the Element
		should be renderd on"""
		self._layer = layer

	def get_layer(self):
		return self._layer

	def set_text(self, text):
		if type(text) not in [str, unicode]:
			raise RuntimeError("Text has to be a string")
		else:
			self._text = text
		if self.status < 1 or self.status == 3:
			self.status = 1

	def set_size(self, size):
		if type(size) is not int:
			raise RuntimeError("Size has to be an integer")
		else:
			self._text_size = size
		if self.status < 2 or self.status == 3:
			self.status = 2

	def set_color(self, color):
		if type(color) not in [list, tuple, dict]:
			raise RuntimeError("Color has to be an interable (r,g,b)")
		else:
			self._color = color
		if self.status == 0:
			self.status = 3
		if self.status < 1 or self.status == 3:
			self.status = 1

	def set_pos(self, pos):
		if type(pos) not in [list, tuple, dict]:
			raise RuntimeError("Position has to be an interable")
		else:
			self._pos = pos
		if self.status == 0:
			self.status = 3

	def get_pos(self):
		return self._pos

	def start(self, args):
		pass

	def update(self):
		pass

	def mouse_over(self):
		pass

	def mouse_enter(self):
		pass

	def mouse_leave(self):
		pass

	def mouse_clicked(self, buttons):
		pass

	def mouse_down(self, buttons):
		pass

	def mouse_up(self, released_buttons):
		pass


class Panel():

	def __init__(self, **kwargs):
		self._layer = 0
		self._pos = (0, 0)
		self._color = (255, 255, 255)
		self._align = "center"
		self._antialias = True
		self._image = None
		self.status = 2
		self._generate_font()
		self._render_text()
		self._generate_rect()
		self.start(kwargs)

	def start(kwarg):
		pass