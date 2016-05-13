# -*- coding: utf-8 -*-
import pygame

pygame.init()

screen = pygame.display.set_mode((600, 600), pygame.RESIZABLE)

t = pygame.font.Font(None, 80)
direct = 1
t_surf = t.render(".", 1, (255, 255, 255))
t_rect = t_surf.get_rect()


def move_dot(screen_):
	global direct
	global t_rect
	if direct == 1:
		if screen.get_rect().contains(t_rect.move((1, 0))):
			t_rect = t_rect.move(1, 0)
		else:
			direct = 2
	elif direct == 2:
		if screen.get_rect().contains(t_rect.move((0, 1))):
			t_rect = t_rect.move(0, 1)
		else:
			direct = 3
	elif direct == 3:
		if screen.get_rect().contains(t_rect.move((-1, 0))):
			t_rect = t_rect.move(-1, 0)
		else:
			direct = 4
	elif direct == 4:
		if screen.get_rect().contains(t_rect.move((0, -1))):
			t_rect = t_rect.move(0, -1)
		else:
			direct = 1


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			exit()  # lint:ok
	screen.fill((0, 0, 0))
	screen.blit(t_surf, t_rect)
	pygame.display.flip()
	move_dot(screen)

