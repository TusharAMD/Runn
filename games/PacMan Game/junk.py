    def checkEvents(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == KEYDOWN:
                if event.key == K_SPACE:
                    if self.pacman.alive:
                        self.pause.setPause(playerPaused=True)
                        if not self.pause.paused:
                            #newtext::self.textgroup.hideText()
                            self.showEntities()
                        else:
                            #newtext::self.textgroup.showText(PAUSETXT)
                            self.hideEntities()