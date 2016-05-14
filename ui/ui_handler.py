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
		self._exec_mouse_over()
		if self.layers is None:
			self._nonelayerblit()
		else:
			self._layerblit()

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

	def _exec_mouse_over(self):
		mouse_pos = pygame.mouse.get_pos()
		for obj in self.elements:
			if obj._rect.collidepoint(mouse_pos):
				obj.mouse_over()