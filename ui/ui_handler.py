# -*- coding: utf-8 -*-
import pygame


class Handler():
	"""The UI handler class with handles all actions
	with the UI elements during execution.
	A UI handler is required for layers to funktion.
	Also a UI handler is needed for the predefined
	funktions of the UI elements who should be overriden
	to work."""

	def __init__(self, screen, layers=None):
		self.elements = []
		self.layers = []
		self.screen = screen
		self.mouse_pos = (-1, -1)
		self.pre_mouse_pos = (-1, -1)
		self.mouse_pressed = None
		self.pre_mouse_pressed = None
		if layers is not None:
			if type(layers) is not int:
				raise RuntimeError("Count of layers has to be an integer")
			for i in range(0, layers):
				self.layers.append(pygame.Surface(self.screen.get_size))
		else:
			self.layers = None

	def register(self, obj):
		"""Funktion to register UI Elements to an
		instance of the handler"""
		self.elements.append(obj)

	def update(self):
		"""Causes the Handler and all registered UI elemets
		to update"""
		self._element_update()
		self._update_mouse_info()
		self._exec_mouse_hover()
		self._exec_mouse_clicked()
		if self.layers is None:
			self._nonelayerblit()
		else:
			self._layerblit()

	def _update_mouse_info(self):
		self.pre_mouse_pos = self.mouse_pos
		self.pre_mouse_pressed = self.mouse_pressed
		self.mouse_pos = pygame.mouse.get_pos()
		self.mouse_pressed = pygame.mouse.get_pressed()

	def _element_update(self):
		for obj in self.elements:
			obj.update()

	def _layerblit(self):
		for obj in self.elements:
			target = obj.get_layer()
			obj._blittosurf(self.layers[target - 1])
		for lay in reversed(self.layers):
			self.screen.blit(lay, (0, 0))

	def _nonelayerblit(self):
		for obj in self.elements:
			obj._blittosurf(self.screen)

	def _exec_mouse_hover(self):
		for obj in self.elements:
			if obj._rect.collidepoint(self.mouse_pos):
				obj.mouse_over()
				if not obj._rect.collidepoint(self.pre_mouse_pos):
					obj.mouse_enter()
			elif not obj._rect.collidepoint(self.mouse_pos):
				if obj._rect.collidepoint(self.pre_mouse_pos):
					obj.mouse_leave()

	def _exec_mouse_clicked(self):
		for obj in self.elements:
			if obj._rect.collidepoint(self.mouse_pos):
				if True in self.mouse_pressed:
					obj.mouse_clicked(self.mouse_pressed)
					if not True in self.pre_mouse_pressed:
						obj.mouse_down(self.mouse_pressed)
				if not True in self.mouse_pressed:
					if True in self.pre_mouse_pressed:
						obj.mouse_up(self.pre_mouse_pressed)