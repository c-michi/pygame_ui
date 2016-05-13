# -*- coding: utf-8 -*-
import pygame


class Handler():
	"""The UI handler class with handles all actions
	with the UI elements during execution.
	A UI handler is required for layers to funktion"""

	def __init__(self, screen, layers=None):
		self.elements = []
		self.layers = []
		self.screen = screen
		if layers is not None:
			if type(layers) is not int:
				raise RuntimeError("Count of layers has to be an integer")
			for i in range(0, layers):
				self.layers.append(pygame.Surface(self.screen.get_size))
		self.layers = False

	def register(self, obj):
		"""Funktion to register UI Elements to an
		instance of the handler"""
		self.elements.append(obj)

	def _layerblit(self):
		for obj in self.elements:
			target = obj.get_layer()
			obj._blittosurf(self.layers[target - 1])
		for lay in reversed(self.layers):
			self.screen.blit(lay, (0, 0))

	def _nonelayerblit(self):
		for obj in self.elements:
			obj._blittosurf(self.screen)