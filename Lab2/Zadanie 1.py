import pygame as py
py.init()

screen = py.display.set_mode((600,600))
BLACK = (255,255,0)
WHITE = (255,255,255)
GREEN = (0,255,0)
X=600
Y=600
running = True
#canvas = py.Surface((600,600))
#py.draw.polygon(canvas,GREEN,[(150,300),(193.934,193.934),(300,150),(406.066,193.934),(450,300),(406.066,406.066),(300,450),(193.934,406.066)])
canvas = py.Surface((X//2,Y//2))
canvas.fill(BLACK)
screen.fill(BLACK)
py.draw.polygon(canvas,GREEN,[(0,150),(43.934,43.934),(150,0),(256.066,43.934),(300,150),(256.066,256.066),(150,300),(43.934,256.066)])
screen.blit(canvas,(150,150))
py.display.update()
while running:
    for event in py.event.get():
        if event.type == py.QUIT:
            running = False
        if event.type == py.KEYDOWN:
            if event.key == py.K_1:
                screen.fill(BLACK)
                canvas_2 = py.transform.scale(canvas,(200,200))
                screen.blit(canvas_2,(X//2-canvas_2.get_width()//2,Y//2-canvas_2.get_height()//2))
                py.display.update()
            if event.key == py.K_2:
                screen.fill(BLACK)
                canvas_2 = py.transform.rotate(canvas,45)
                screen.blit(canvas_2,(X//2-canvas_2.get_width()//2,Y//2-canvas_2.get_height()//2))
                py.display.update()
            if event.key == py.K_3:
                screen.fill(BLACK)
                canvas_2 = py.transform.scale(canvas,(X//4,Y//2))
                canvas_2 = py.transform.rotate(canvas_2,180)
                screen.blit(canvas_2,(X//2-canvas_2.get_width()//2,Y//2-canvas_2.get_height()//2))
                py.display.update()
            if event.key == py.K_4:
                screen.fill(BLACK)
                canvas_2 = py.transform.scale(canvas,(X//2,Y//2))
                canvas_3 = py.Surface((X,Y//2))
                canvas_3.blit(canvas_2,(0,0))
                pxar = py.PixelArray(canvas_3)
                j=0
                while j < Y//2:
                    i=X//2
                    while i > 0:   
                        pxar[i+j,j] = pxar[i,j]
                        pxar[i,j] = (0,0,0)
                        i=i-1
                    j=j+1
                pxar.close()
                screen.blit(canvas_3,(X//2-canvas_3.get_width()//2,Y//2-canvas_3.get_height()//2))
                py.display.update()
            if event.key == py.K_5:
                screen.fill(BLACK)
                canvas_2 = py.transform.scale(canvas,(X//2,Y//4))
                screen.blit(canvas_2,(X//2-canvas_2.get_width()//2,0))
                py.display.update()
            if event.key == py.K_6:
                screen.fill(BLACK)
                canvas_2 = py.transform.scale(canvas,(X//2,Y//2))
                canvas_3 = py.Surface((X,Y//2))
                canvas_3.blit(canvas_2,(0,0))
                pxar = py.PixelArray(canvas_3)
                j=0
                while j < Y//2:
                    i=X//2
                    while i > 0:   
                        pxar[i+j,j] = pxar[i,j]
                        pxar[i,j] = (0,0,0)
                        i=i-1
                    j=j+1
                pxar.close()
                canvas_3 = py.transform.rotate(canvas_3,90)
                screen.blit(canvas_3,(X//2-canvas_3.get_width()//2,Y//2-canvas_3.get_height()//2))
                py.display.update()
            if event.key == py.K_7:
                screen.fill(BLACK)
                canvas_2 = py.transform.scale(canvas,(X//4,Y//2))
                canvas_2 = py.transform.rotate(canvas_2,180)
                canvas_2 = py.transform.flip(canvas_2,1,0)
                screen.blit(canvas_2,(X//2-canvas_2.get_width()//2,Y//2-canvas_2.get_height()//2))
                py.display.update()
            if event.key == py.K_8:
                screen.fill(BLACK)
                canvas_2 = py.transform.scale(canvas,(X//2,Y//4))
                canvas_2 = py.transform.rotate(canvas_2,-22.5)
                screen.blit(canvas_2,(X//2-canvas_2.get_width()//2,Y//2))
                py.display.update()
            if event.key == py.K_9:
                screen.fill(BLACK)
                canvas_2 = py.transform.scale(canvas,(X//2,Y//2))
                canvas_3 = py.Surface((X,Y//2))
                canvas_3.blit(canvas_2,(0,0))
                pxar = py.PixelArray(canvas_3)
                j=0
                while j < Y//2:
                    i=X//2
                    while i > 0:   
                        pxar[i+j,j] = pxar[i,j]
                        pxar[i,j] = (0,0,0)
                        i=i-1
                    j=j+1
                pxar.close()
                canvas_3 = py.transform.rotate(canvas_3,150)
                screen.blit(canvas_3,(X//2-canvas_3.get_width()//2 + 165,Y//2-canvas_3.get_height()//2))
                py.display.update()
    #Tutaj jest koło o średnicy 150 pikseli
    #py.draw.circle(screen,WHITE,(300,300), 150)
py.quit()
