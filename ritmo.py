import sys,pygame,random
def header(message,pos,scale,color = (0,0,0)):
    textfont = pygame.font.SysFont('Calibri Light (Headings)',int(scale))
    textfont = textfont.render(message,1,color)
    pantalla.blit(textfont,pos)
def draw(image,scale,pos):
    imagen = pygame.image.load(image)
    imagen = pygame.transform.scale(imagen,scale)
    pantalla.blit(imagen,pos)
    rect = imagen.get_rect()
    rect.topleft = pos
    return rect
def personajeEnLaEsquina():
    global clickedPer1
    global clickedPer2
    global clickedPer3
    global clickedPer4
    if clickedPer1:
        draw('images\personaje1.png',(pantalla.get_width()/10,pantalla.get_width()/10),(pantalla.get_width()/1.2,pantalla.get_height()/25))
    if clickedPer2:
        draw('images\personaje2.png',(pantalla.get_width()/10,pantalla.get_width()/10),(pantalla.get_width()/1.2,pantalla.get_height()/25))
    if clickedPer3:
        draw('images\personaje3.png',(pantalla.get_width()/10,pantalla.get_width()/10),(pantalla.get_width()/1.2,pantalla.get_height()/25))
    if clickedPer4:
        draw('images\personaje4.png',(pantalla.get_width()/10,pantalla.get_width()/10),(pantalla.get_width()/1.2,pantalla.get_height()/25))
class LoadingBar:
    def __init__(self,limit,progress):
        self.limit = limit
        self.progress = progress
    
    def increaseProgress(self):
        self.progress += 1
    
    def draw(self):
        global pantalla
        global interiorBarra
        global exteriorBarra
        interiorBarra = pygame.transform.scale(interiorBarra,((pantalla.get_width()/6*self.progress)/self.limit,pantalla.get_height()/12))
        exteriorBarra = pygame.transform.scale(exteriorBarra,(pantalla.get_width()/6,pantalla.get_height()/12))
        pantalla.blit(exteriorBarra,(pantalla.get_width()/25,pantalla.get_height()/25))
        pantalla.blit(interiorBarra,(pantalla.get_width()/25,pantalla.get_height()/25))


pygame.init()
pygame.mixer.music.load('audio\inicio.wav')
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(1)
pantalla = pygame.display.set_mode((1290,748))
icono = pygame.image.load('images\icon.png')
pygame.display.set_icon(icono)
pygame.display.set_caption('RITMO')


terminado = False
cambioAleatorio = False
pasoAlNivel2 = False
pasoAlNivel3 = False
pasoAlNivel4 = False
escuchoTodos = False
finBarra = False
contador = 0
diapositiva = -1
tiempoInicial = 0
tiempoTranscurrido = 0
instrumentosEscuchados = []
aleatorio = None

clickedPer1 = False
clickedPer2 = False
clickedPer3 = False
clickedPer4 = False

bateriaSound = pygame.mixer.Sound('audio\\baterySound.wav')
xilofonoSound = pygame.mixer.Sound('audio\\xilofonoSound.wav')
tamborSound = pygame.mixer.Sound('audio\\tamborSound.wav')
pianoSound = pygame.mixer.Sound('audio\\pianoSound.wav')
platillosSound = pygame.mixer.Sound('audio\\platilloSound.wav')
clavesSound = pygame.mixer.Sound('audio\\clavesSound.wav')
bpm60 = pygame.mixer.Sound('audio\\60bpm.wav')
bpm90 = pygame.mixer.Sound('audio\\90bpm.wav')
bpm120 = pygame.mixer.Sound('audio\\120bpm.wav')
bongosSound = pygame.mixer.Sound('audio\\bongosSound.wav')
maracasSound = pygame.mixer.Sound('audio\\maracasSound.wav')
platosSound = pygame.mixer.Sound('audio\\platosSound.wav')
interiorBarra = pygame.image.load('images\\green.png')
exteriorBarra = pygame.image.load('images\\rectangle.png')
barraNivel1 = LoadingBar(15,0)
barraNivel2 = LoadingBar(16,0)
barraNivel3 = LoadingBar(17,0)

rectSiguiente = None
rectAnterior = None
rectMundo1 = None
rectNivel1 = None
rectBateria = None
rectTambor = None
rectXilofono = None
rectBongos = None
rectMaracas = None
rectPlatos = None
rectClaves = None
rectPiano = None
rectPlatillo = None
rectPer1 = None
rectPer2 = None
rectPer3 = None
rectPer4 = None
rectFin = None

while not terminado:
    personajeEnLaEsquina()
    pygame.display.flip()
    mPos = pygame.mouse.get_pos()
    if pygame.mixer.get_busy():
        pygame.mixer.music.pause()
    else:
        pygame.mixer.music.unpause()

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            terminado = True
        if evento.type == pygame.MOUSEBUTTONDOWN and rectSiguiente != None and rectSiguiente.collidepoint(mPos) and diapositiva == -1:
            pygame.mixer.music.stop()
            rectSiguiente = None
            diapositiva = 0

        if evento.type == pygame.MOUSEBUTTONDOWN and rectSiguiente != None and rectSiguiente.collidepoint(mPos) and diapositiva == 0:
            rectSiguiente = None
            diapositiva = 1
        if (clickedPer1 or clickedPer2 or clickedPer3 or clickedPer4) and rectSiguiente != None and rectSiguiente.collidepoint(mPos) and evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 1:
            diapositiva = 2
            cambioAleatorio = False
        if evento.type==pygame.MOUSEBUTTONDOWN and (rectPer1 != None and rectPer1.collidepoint(mPos) or rectPer2 != None and rectPer2.collidepoint(mPos) or rectPer3 != None and rectPer3.collidepoint(mPos) or rectPer4 != None and rectPer4.collidepoint(mPos)) and diapositiva == 1:
            if rectPer1.collidepoint(mPos):
                clickedPer1 = True
                clickedPer2,clickedPer3,clickedPer4 = [False,False,False]
            if rectPer2.collidepoint(mPos):
                clickedPer2 = True
                clickedPer1,clickedPer3,clickedPer4 = [False,False,False]
            if rectPer3.collidepoint(mPos):
                clickedPer3 = True
                clickedPer1,clickedPer2,clickedPer4 = [False,False,False]
            if rectPer4.collidepoint(mPos):
                clickedPer4 = True
                clickedPer1,clickedPer2,clickedPer3 = [False,False,False]
        
        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 2 and rectMundo1 != None and rectMundo1.collidepoint(mPos):
             cambioAleatorio = False
             diapositiva = 2.5
        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 2 and rectAnterior != None and rectAnterior.collidepoint(mPos):
            diapositiva = 1
            cambioAleatorio = False
            rectAnterior = None
        
        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 2.5 and rectNivel1 != None and rectNivel1.collidepoint(mPos):
             diapositiva = 3

        if evento.type == pygame.MOUSEBUTTONDOWN and rectSiguiente != None and rectSiguiente.collidepoint(mPos) and diapositiva == 3:
            diapositiva = 4
            cambioAleatorio = False
            rectSiguiente = None
        
        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 4 and rectSiguiente != None and rectSiguiente.collidepoint(mPos):
            bateriaSound.stop()
            xilofonoSound.stop()
            tamborSound.stop()
            diapositiva = 5
            rectSiguiente = None

        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 5 and rectSiguiente != None and rectSiguiente.collidepoint(mPos):
            rectSiguiente = None
            instrumentosEscuchados = []
            if pasoAlNivel2 == False:
                diapositiva = 6
                cambioAleatorio = True
            if pasoAlNivel2 == True and pasoAlNivel3 == False:
                diapositiva = 12
                cambioAleatorio = False
            if pasoAlNivel3== True:
                diapositiva = 15
                cambioAleatorio = False

        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 5 and rectAnterior != None and rectAnterior.collidepoint(mPos):
            rectAnterior = None
            instrumentosEscuchados = []
            if pasoAlNivel2 == False:
                diapositiva = 4
                cambioAleatorio = False
            if pasoAlNivel2 == True and pasoAlNivel3 == False:
                diapositiva = 11
                cambioAleatorio = False
            if pasoAlNivel3== True:
                diapositiva = 14
                cambioAleatorio = False

        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 6 and rectSiguiente != None and rectSiguiente.collidepoint(mPos):
            diapositiva = 7
            cambioAleatorio = False
            rectSiguiente = None

        if evento.type == pygame.MOUSEBUTTONDOWN and rectBateria != None and rectBateria.collidepoint(mPos) and diapositiva == 7 and escuchoTodos == False:
            bateriaSound.stop()
            xilofonoSound.stop()
            tamborSound.stop()
            if aleatorio == 0:
                diapositiva = 8
                instrumentosEscuchados.append('bateria')
            else:
                diapositiva = 10
        if evento.type == pygame.MOUSEBUTTONDOWN and rectXilofono != None and rectXilofono.collidepoint(mPos) and diapositiva == 7 and escuchoTodos == False:
            bateriaSound.stop()
            xilofonoSound.stop()
            tamborSound.stop()
            if aleatorio == 1:
                diapositiva = 8
                instrumentosEscuchados.append('xilofono')
            else:
                diapositiva = 10
        if evento.type == pygame.MOUSEBUTTONDOWN and rectTambor != None and rectTambor.collidepoint(mPos) and diapositiva == 7 and escuchoTodos == False:
            bateriaSound.stop()
            xilofonoSound.stop()
            tamborSound.stop()
            if aleatorio == 2:
                diapositiva = 8
                instrumentosEscuchados.append('tambor')
            else:
                diapositiva = 10
        if evento.type == pygame.MOUSEBUTTONDOWN and rectSiguiente != None and rectSiguiente.collidepoint(mPos) and diapositiva == 7:
            diapositiva = 8


        if evento.type == pygame.KEYDOWN and cambioAleatorio == True and diapositiva== 8:
                tiempoInicial = pygame.time.get_ticks()
                cambioAleatorio = False
        if evento.type == pygame.KEYDOWN and cambioAleatorio == False and ((pygame.time.get_ticks()-tiempoInicial)!=0) and diapositiva==8:
                tiempoTranscurrido = pygame.time.get_ticks()
                diferenciaTemporal = tiempoTranscurrido-tiempoInicial
                if diferenciaTemporal>=800 and diferenciaTemporal<=1200:
                    barraNivel1.increaseProgress()
                contador += diferenciaTemporal
                cambioAleatorio = True

        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 9 and rectSiguiente != None and rectSiguiente.collidepoint(mPos):
            rectSiguiente = None
            instrumentosEscuchados = []
            if pasoAlNivel3 == True and pasoAlNivel4 == False:
                pasoAlNivel4 = True
            if pasoAlNivel3 == False and pasoAlNivel2 == True:
                pasoAlNivel3 = True
            if pasoAlNivel2 == False:
                pasoAlNivel2 = True

            if pasoAlNivel3 == True and pasoAlNivel4 == False:
                diapositiva = 14
            if pasoAlNivel2 == True and pasoAlNivel3== False:
                diapositiva = 11
            cambioAleatorio = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 9 and rectAnterior != None and rectAnterior.collidepoint(mPos) and len(instrumentosEscuchados)!=3:
            rectAnterior = None
            cambioAleatorio = False
            if pasoAlNivel2 == True:
                diapositiva = 12
            if pasoAlNivel2 == False:
                diapositiva = 7

        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 9 and rectAnterior != None and rectAnterior.collidepoint(mPos) and len(instrumentosEscuchados)==3:
            cambioAleatorio = False
        
        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 10 and rectSiguiente != None and rectSiguiente.collidepoint(mPos):
            cambioAleatorio = False
            rectSiguiente = None
            if pasoAlNivel2 == False:
                diapositiva = 7
            if pasoAlNivel2 == True and pasoAlNivel3 == False:
                diapositiva = 12
            if pasoAlNivel3 == True:
                diapositiva = 15

        if evento.type == pygame.MOUSEBUTTONDOWN and rectSiguiente != None and rectSiguiente.collidepoint(mPos) and diapositiva == 11:
            bongosSound.stop()
            maracasSound.stop()
            platosSound.stop()
            diapositiva = 5

        if evento.type == pygame.MOUSEBUTTONDOWN and rectBongos != None and rectBongos.collidepoint(mPos) and diapositiva == 12 and escuchoTodos == False:
            bongosSound.stop()
            maracasSound.stop()
            platosSound.stop()
            if aleatorio == 0:
                diapositiva = 13
                instrumentosEscuchados.append('bongos')
            else:
                diapositiva = 10

        if evento.type == pygame.MOUSEBUTTONDOWN and rectMaracas != None and rectMaracas.collidepoint(mPos) and diapositiva == 12 and escuchoTodos == False:
            bongosSound.stop()
            maracasSound.stop()
            platosSound.stop()
            if aleatorio == 1:
                diapositiva = 13
                instrumentosEscuchados.append('maracas')
            else:
                diapositiva = 10
        
        if evento.type == pygame.MOUSEBUTTONDOWN and rectPlatos != None and rectPlatos.collidepoint(mPos) and diapositiva == 12 and escuchoTodos == False:
            bongosSound.stop()
            maracasSound.stop()
            platosSound.stop()
            if aleatorio == 2:
                diapositiva = 13
                instrumentosEscuchados.append('platos')
            else:
                diapositiva = 10
        if evento.type == pygame.MOUSEBUTTONDOWN and rectSiguiente != None and rectSiguiente.collidepoint(mPos) and diapositiva == 12:
            diapositiva = 13

        if evento.type == pygame.KEYDOWN and cambioAleatorio == True and diapositiva== 13:
                tiempoInicial = pygame.time.get_ticks()
                cambioAleatorio = False
        if evento.type == pygame.KEYDOWN and cambioAleatorio == False and ((pygame.time.get_ticks()-tiempoInicial)!=0) and diapositiva==13:
                tiempoTranscurrido = pygame.time.get_ticks()
                diferenciaTemporal = tiempoTranscurrido-tiempoInicial
                if diferenciaTemporal>=500 and diferenciaTemporal<=800:
                    barraNivel2.increaseProgress()
                contador += diferenciaTemporal
                cambioAleatorio = True
        if evento.type == pygame.MOUSEBUTTONDOWN and rectSiguiente != None and rectSiguiente.collidepoint(mPos) and diapositiva == 14:
            clavesSound.stop()
            pianoSound.stop()
            platillosSound.stop()
            diapositiva = 5

        if evento.type == pygame.MOUSEBUTTONDOWN and rectClaves != None and rectClaves.collidepoint(mPos) and diapositiva == 15 and escuchoTodos == False:
            clavesSound.stop()
            pianoSound.stop()
            platillosSound.stop()
            if aleatorio == 0:
                diapositiva = 16
                instrumentosEscuchados.append('claves')
            else:
                diapositiva = 10

        if evento.type == pygame.MOUSEBUTTONDOWN and rectPiano != None and rectPiano.collidepoint(mPos) and diapositiva == 15 and escuchoTodos == False:
            clavesSound.stop()
            pianoSound.stop()
            platillosSound.stop()
            if aleatorio == 1:
                diapositiva = 16
                instrumentosEscuchados.append('piano')
            else:
                diapositiva = 10
        if evento.type == pygame.MOUSEBUTTONDOWN and rectPlatillo != None and rectPlatillo.collidepoint(mPos) and diapositiva == 15 and escuchoTodos == False:
            clavesSound.stop()
            pianoSound.stop()
            platillosSound.stop()
            if aleatorio == 2:
                diapositiva = 16
                instrumentosEscuchados.append('platillo')
            else:
                diapositiva = 10

        if evento.type == pygame.MOUSEBUTTONDOWN and rectSiguiente != None and rectSiguiente.collidepoint(mPos) and diapositiva == 15:
            diapositiva = 16
        if evento.type == pygame.KEYDOWN and cambioAleatorio == True and diapositiva== 16:
                tiempoInicial = pygame.time.get_ticks()
                cambioAleatorio = False

        if evento.type == pygame.KEYDOWN and cambioAleatorio == False and ((pygame.time.get_ticks()-tiempoInicial)!=0) and diapositiva==16:
                tiempoTranscurrido = pygame.time.get_ticks()
                diferenciaTemporal = tiempoTranscurrido-tiempoInicial
                if diferenciaTemporal>=350 and diferenciaTemporal<=650:
                    barraNivel3.increaseProgress()
                contador += diferenciaTemporal
                cambioAleatorio = True

        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 17 and rectAnterior != None and rectAnterior.collidepoint(mPos):
            rectAnterior = None
            if len(instrumentosEscuchados)!=3:
                diapositiva = 15
                cambioAleatorio = False
            else:
                cambioAleatorio = False
        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 17 and rectSiguiente != None and rectSiguiente.collidepoint(mPos):
            rectSiguiente = None
            diapositiva = 18

        if evento.type == pygame.MOUSEBUTTONDOWN and diapositiva == 18 and rectFin != None and rectFin.collidepoint(mPos):
            rectFin = None
            terminado = True
    if diapositiva == -1:
        rectPres = draw('images\present.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        header('JUEGO DE RITMOS',(pantalla.get_width()/5.8,pantalla.get_height()/5.3),(pantalla.get_width()/10),(0,0,0))
        rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))

    if diapositiva == 0:
        rectIntro = draw('images\intro.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))

    if diapositiva == 1:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        rectPer1 = draw('images\personaje1.png',(pantalla.get_width()/6.5,pantalla.get_height()/3.54),(pantalla.get_width()/20,pantalla.get_height()/3.3))
        rectPer2 = draw('images\personaje2.png',(pantalla.get_width()/6.5,pantalla.get_height()/3.54),(pantalla.get_width()/20+pantalla.get_width()/6.5,pantalla.get_height()/3.3))
        rectPer3 = draw('images\personaje3.png',(pantalla.get_width()/6.5,pantalla.get_height()/3.54),(pantalla.get_width()/20,pantalla.get_height()/3.3+pantalla.get_height()/3.54))
        rectPer4 = draw('images\personaje4.png',(pantalla.get_width()/6.5,pantalla.get_height()/3.54),(pantalla.get_width()/20+pantalla.get_width()/6.5,pantalla.get_height()/3.3+pantalla.get_height()/3.54))
        recticon = draw('images\icon.png',(pantalla.get_width()/3,pantalla.get_height()/1.77),(pantalla.get_width()/20+pantalla.get_width()/6.5+pantalla.get_width()/4,pantalla.get_height()/3.5))
        header('Escoge un personaje',(pantalla.get_width()/20,pantalla.get_height()/8),pantalla.get_width()/16)
        if clickedPer1 or clickedPer2 or clickedPer3 or clickedPer4:
            rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))

    if diapositiva == 2:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        rectAnterior= draw('images\\anterior.png',(pantalla.get_width()/8,pantalla.get_height()/6),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()/2))
        rectMundo1 = draw('images\\mundo1.png',(pantalla.get_width()/4.5,pantalla.get_height()/6.75),(pantalla.get_width()/10,pantalla.get_height()/6))
        rectMundo2 = draw('images\\mundo2.png',(pantalla.get_width()/4.5,pantalla.get_height()/6.75),(pantalla.get_width()/3,pantalla.get_height()/2.35))
        rectMundo3 = draw('images\\mundo3.png',(pantalla.get_width()/4.5,pantalla.get_height()/6.75),(pantalla.get_width()/4.5+pantalla.get_width()/2.7,pantalla.get_height()/1.5))
        rectSin = draw('images\sinosoidales.png',(pantalla.get_width()/5,pantalla.get_height()/5.8),(pantalla.get_width()/1.7,pantalla.get_height()/6))
        if rectMundo2.collidepoint(mPos) or rectMundo3.collidepoint(mPos):
            cambioAleatorio = True
        if cambioAleatorio == True:
            header('Debes iniciar el Mundo 1',(pantalla.get_width()/7.2,pantalla.get_height()/1.5),pantalla.get_width()/25)
            header('para desbloquear el Mundo 2 y 3',(pantalla.get_width()/7.2,pantalla.get_height()/1.4),pantalla.get_width()/25)
    if diapositiva == 2.5:
        pantalla.fill((255,255,255))
        header('Mundo 1: Imitando el ritmo',(pantalla.get_width()/12,pantalla.get_height()/7),(pantalla.get_width()/20))
        rectNivel1 = draw('images\\nivel1.png',(pantalla.get_height()/3,pantalla.get_height()/3),(pantalla.get_width()/10,pantalla.get_height()/3))
        rectNivel2 = draw('images\\nivel2.png',(pantalla.get_height()/3,pantalla.get_height()/3),(pantalla.get_width()/2.35,pantalla.get_height()/3))
        rectNivel3 = draw('images\\nivel3.png',(pantalla.get_height()/3,pantalla.get_height()/3),(pantalla.get_width()/1.4,pantalla.get_height()/3))
        rectSin = draw('images\sinosoidales.png',(pantalla.get_width()/5,pantalla.get_height()/5.8),(pantalla.get_width()/1.8,pantalla.get_height()/9))
        if rectNivel2.collidepoint(mPos) or rectNivel3.collidepoint(mPos):
            cambioAleatorio = True
        if cambioAleatorio == True:
            header('Debes iniciar con el Nivel 1',(pantalla.get_width()/7.2,pantalla.get_height()/1.3),pantalla.get_width()/25)
            header('para desbloquear el Nivel 2 y 3',(pantalla.get_width()/7.2,pantalla.get_height()/1.21),pantalla.get_width()/25)

    if diapositiva == 3:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        header('Instrucciones',(pantalla.get_width()/20,pantalla.get_height()/8),pantalla.get_width()/16,color=(255,255,0))
        header('Escoge el instrumento',(pantalla.get_width()/20,pantalla.get_height()/2.5),pantalla.get_width()/13)
        header('correcto y reproduce el ritmo',(pantalla.get_width()/20,pantalla.get_height()/2),pantalla.get_width()/13)
        rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))

    if diapositiva == 4:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        header('Nivel 1',(pantalla.get_width()/2-pantalla.get_width()/16,pantalla.get_height()/8),pantalla.get_width()/16,color=(0,255,255))
        header('Escucha todos los instrumentos, pasando el mouse por ellos, para avanzar',(pantalla.get_width()/8-pantalla.get_width()/26,pantalla.get_height()/4),pantalla.get_width()/30,color=(0,0,0))
        rectBateria = draw('images\\bateria.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/19,pantalla.get_height()/2.5))
        rectXilofono = draw('images\\xilofono.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/2-pantalla.get_width()/11,pantalla.get_height()/2.5))
        rectTambor = draw('images\\tambor.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/20+pantalla.get_width()/1.4,pantalla.get_height()/2.5))
        if 'bateria' in instrumentosEscuchados and 'xilofono' in instrumentosEscuchados and 'tambor' in instrumentosEscuchados:
            rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))
        if rectBateria.collidepoint(mPos) :
            if bateriaSound.get_num_channels() == 0:
                xilofonoSound.stop()
                tamborSound.stop()
                bateriaSound.play()
                instrumentosEscuchados.append('bateria')
                bateriaSound.fadeout(5000)
        if rectXilofono.collidepoint(mPos):
            if xilofonoSound.get_num_channels() == 0:
                bateriaSound.stop()
                tamborSound.stop()
                xilofonoSound.play()
                instrumentosEscuchados.append('xilofono')
                xilofonoSound.fadeout(5000)
        if rectTambor.collidepoint(mPos):
            if tamborSound.get_num_channels() == 0:
                bateriaSound.stop()
                xilofonoSound.stop()
                tamborSound.play()
                instrumentosEscuchados.append('tambor')
                tamborSound.fadeout(5000)
    
    if diapositiva == 5:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        header('¡ EMPECEMOS !',(pantalla.get_width()/6,pantalla.get_height()/2.5),(pantalla.get_width()/8),(255,255,0))
        rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))
        rectAnterior= draw('images\\anterior.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()/7,pantalla.get_height()-pantalla.get_height()/4))
    if diapositiva == 6:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        header('Nivel 1',(pantalla.get_width()/6,pantalla.get_height()/6),(pantalla.get_width()/7),(0,255,255))
        header('Escoge el instrumento que sonó ',(pantalla.get_width()/6,pantalla.get_height()/2.5),(pantalla.get_width()/20),(0,0,0))
        header('y después sigue el ritmo',(pantalla.get_width()/6,pantalla.get_height()/2),(pantalla.get_width()/20),(0,0,0))
        rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))
    
    if diapositiva == 7:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        if cambioAleatorio == False:
            if instrumentosEscuchados == []:
                aleatorio = random.randint(0,2)
            if instrumentosEscuchados == ['tambor']:
                aleatorio = 0
            if instrumentosEscuchados == ['xilofono']:
                aleatorio = 2
            if instrumentosEscuchados == ['bateria']:
                aleatorio = 1
            if 'bateria' in instrumentosEscuchados and 'xilofono' in instrumentosEscuchados:
                aleatorio = 2
            if 'xilofono' in instrumentosEscuchados and 'tambor' in instrumentosEscuchados:
                aleatorio = 0
            if 'tambor' in instrumentosEscuchados and 'bateria' in instrumentosEscuchados:
                aleatorio = 1
        rectBateria = draw('images\\bateria.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/19,pantalla.get_height()/2.5))
        rectXilofono = draw('images\\xilofono.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/2-pantalla.get_width()/11,pantalla.get_height()/2.5))
        rectTambor = draw('images\\tambor.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/20+pantalla.get_width()/1.4,pantalla.get_height()/2.5))
        header('¿Cúal instrumento suena?',(pantalla.get_width()/20,pantalla.get_height()/8),pantalla.get_width()/16)
        if aleatorio == 0 and cambioAleatorio == False and 'bateria' not in instrumentosEscuchados:
            if bateriaSound.get_num_channels() == 0:
                bateriaSound.play()
                bateriaSound.fadeout(10000)
        if aleatorio == 1 and cambioAleatorio == False and 'xilofono' not in instrumentosEscuchados:
            if xilofonoSound.get_num_channels() == 0:
                xilofonoSound.play()
                xilofonoSound.fadeout(10000)
        if aleatorio == 2 and cambioAleatorio == False and 'tambor' not in instrumentosEscuchados:
            if tamborSound.get_num_channels() == 0:
                tamborSound.play()
                tamborSound.fadeout(10000)
        if 'tambor' in instrumentosEscuchados and 'xilofono' in instrumentosEscuchados and 'bateria' in instrumentosEscuchados and escuchoTodos == True:
            rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))
            header('Ya reconociste todos los instrumentos',(pantalla.get_width()/6,pantalla.get_height()/1.3),(pantalla.get_width()/30),(0,0,0))
        cambioAleatorio = True
    if diapositiva == 8:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        if 'tambor' in instrumentosEscuchados and 'xilofono' in instrumentosEscuchados and 'bateria' in instrumentosEscuchados:
            escuchoTodos = True
        if bpm60.get_num_channels() == 0:
            bpm60.play()
        header('Sigue el ritmo',(pantalla.get_width()/5,pantalla.get_height()/2.3),(pantalla.get_width()/10),(0,0,0))
        header('presionando la',(pantalla.get_width()/5,pantalla.get_height()/1.8),(pantalla.get_width()/10),(0,0,0))
        header('barra de espacio',(pantalla.get_width()/5,pantalla.get_height()/1.5),(pantalla.get_width()/10),(0,0,0))
        barraNivel1.draw()
        if finBarra == True:
            finBarra = False
            pygame.time.delay(500)
            bpm60.stop()
            diapositiva = 9
            cambioAleatorio = True
            contador = 0
            tiempoInicial = 0
            escuchoTodos = False
            barraNivel1.progress = 0
        if barraNivel1.limit == barraNivel1.progress:
            finBarra = True
        if contador >= 9000 and barraNivel1.progress < barraNivel1.limit/2 or contador >=18000 and barraNivel1.progress<barraNivel1.limit:
            barraNivel1.progress = 0
            bpm60.stop()
            diapositiva = 10
            cambioAleatorio = True
            contador = 0
            tiempoInicial = 0
            instrumentosEscuchados = []
            escuchoTodos = False

    if diapositiva == 9:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))
        rectEstrella = draw('images\\10notas.png',(pantalla.get_width()/3,pantalla.get_height()/2.5),(pantalla.get_width()/2.3,pantalla.get_height()/4))
        rectAnterior= draw('images\\anterior.png',(pantalla.get_width()/8,pantalla.get_height()/6),(pantalla.get_width()/7,pantalla.get_height()-pantalla.get_height()/4))
        header('Ganaste',(pantalla.get_width()/5,pantalla.get_height()/2.3),(pantalla.get_width()/10),(0,0,0))
        if len(instrumentosEscuchados) == 3 and cambioAleatorio == False:
            header('Ya hizo el ejercicio con los 3 instrumentos',(pantalla.get_width()/4,pantalla.get_height()/1.3),(pantalla.get_width()/25),(0,0,0))
        
    if diapositiva == 10:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        header('!Puedes mejorar¡',(pantalla.get_width()/20,pantalla.get_height()/10),(pantalla.get_width()/10),(255,0,0))
        header('Intentalo nuevamente',(pantalla.get_width()/20,pantalla.get_height()/2.3),(pantalla.get_width()/10),(0,0,0))
        rectSiguiente = draw('images\\reinicio.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))

    if diapositiva == 11:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        header('Nivel 2',(pantalla.get_width()/2-pantalla.get_width()/16,pantalla.get_height()/8),pantalla.get_width()/16,color=(0,255,255))
        header('Escucha todos los instrumentos, pasando el mouse por ellos, para avanzar',(pantalla.get_width()/8-pantalla.get_width()/26,pantalla.get_height()/4),pantalla.get_width()/30,color=(0,0,0))
        rectBongos = draw('images\\bongos.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/19,pantalla.get_height()/2.5))
        rectMaracas = draw('images\\maracas.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/2-pantalla.get_width()/11,pantalla.get_height()/2.5))
        rectPlatos = draw('images\\platos.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/20+pantalla.get_width()/1.4,pantalla.get_height()/2.5))
        if 'bongos' in instrumentosEscuchados and 'maracas' in instrumentosEscuchados and 'platos' in instrumentosEscuchados:
            rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))
        if rectBongos.collidepoint(mPos) :
            if bongosSound.get_num_channels() == 0:
                maracasSound.stop()
                platosSound.stop()
                bongosSound.play()
                instrumentosEscuchados.append('bongos')
                bongosSound.fadeout(5000)
        if rectMaracas.collidepoint(mPos):
            if maracasSound.get_num_channels() == 0:
                platosSound.stop()
                bongosSound.stop()
                maracasSound.play()
                instrumentosEscuchados.append('maracas')
                maracasSound.fadeout(5000)
        if rectPlatos.collidepoint(mPos):
            if platosSound.get_num_channels() == 0:
                bongosSound.stop()
                maracasSound.stop()
                platosSound.play()
                instrumentosEscuchados.append('platos')
                platosSound.fadeout(5000)
    if diapositiva == 12:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        if cambioAleatorio == False:
            if instrumentosEscuchados == []:
                aleatorio = random.randint(0,2)
            if instrumentosEscuchados == ['bongos']:
                aleatorio = 0
            if instrumentosEscuchados == ['maracas']:
                aleatorio = 2
            if instrumentosEscuchados == ['platos']:
                aleatorio = 1
            if 'bongos' in instrumentosEscuchados and 'maracas' in instrumentosEscuchados:
                aleatorio = 2
            if 'maracas' in instrumentosEscuchados and 'platos' in instrumentosEscuchados:
                aleatorio = 0
            if 'bongos' in instrumentosEscuchados and 'platos' in instrumentosEscuchados:
                aleatorio = 1
        rectBongos = draw('images\\bongos.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/19,pantalla.get_height()/2.5))
        rectMaracas = draw('images\\maracas.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/2-pantalla.get_width()/11,pantalla.get_height()/2.5))
        rectPlatos = draw('images\\platos.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/20+pantalla.get_width()/1.4,pantalla.get_height()/2.5))
        header('¿Cúal instrumento suena?',(pantalla.get_width()/20,pantalla.get_height()/8),pantalla.get_width()/16)
        if aleatorio == 0 and cambioAleatorio == False and 'bongos' not in instrumentosEscuchados:
            if bongosSound.get_num_channels() == 0:
                bongosSound.play()
                bongosSound.fadeout(10000)
        if aleatorio == 1 and cambioAleatorio == False and 'maracas' not in instrumentosEscuchados:
            if maracasSound.get_num_channels() == 0:
                maracasSound.play()
                maracasSound.fadeout(10000)
        if aleatorio == 2 and cambioAleatorio == False and 'platos' not in instrumentosEscuchados:
            if platosSound.get_num_channels() == 0:
                platosSound.play()
                platosSound.fadeout(10000)
        if 'platos' in instrumentosEscuchados and 'maracas' in instrumentosEscuchados and 'bongos' in instrumentosEscuchados and escuchoTodos == True:
            rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))
            header('Ya reconociste todos los instrumentos',(pantalla.get_width()/6,pantalla.get_height()/1.3),(pantalla.get_width()/30),(0,0,0))
        cambioAleatorio = True
    if diapositiva == 13:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        if 'platos' in instrumentosEscuchados and 'maracas' in instrumentosEscuchados and 'bongos' in instrumentosEscuchados:
            escuchoTodos = True
        if bpm90.get_num_channels() == 0:
            bpm90.play()
        header('Sigue el ritmo',(pantalla.get_width()/5,pantalla.get_height()/2.3),(pantalla.get_width()/10),(0,0,0))
        header('presionando la',(pantalla.get_width()/5,pantalla.get_height()/1.8),(pantalla.get_width()/10),(0,0,0))
        header('barra de espacio',(pantalla.get_width()/5,pantalla.get_height()/1.5),(pantalla.get_width()/10),(0,0,0))
        barraNivel2.draw()
        if finBarra == True:
            finBarra = False
            pygame.time.delay(500)
            bpm90.stop()
            diapositiva = 9
            cambioAleatorio = True
            contador = 0
            tiempoInicial = 0
            escuchoTodos = False
            barraNivel2.progress = 0

        if barraNivel2.limit == barraNivel2.progress:
            finBarra = True
        if contador >= 6400 and barraNivel2.progress < barraNivel2.limit/2 or contador >=12800 and barraNivel2.progress<barraNivel2.limit:
            barraNivel2.progress = 0
            bpm90.stop()
            diapositiva = 10
            cambioAleatorio = True
            contador = 0
            tiempoInicial = 0
            instrumentosEscuchados = []
            escuchoTodos = False
    if diapositiva == 14:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        header('Nivel 3',(pantalla.get_width()/2-pantalla.get_width()/16,pantalla.get_height()/8),pantalla.get_width()/16,color=(0,255,255))
        header('Escucha todos los instrumentos, pasando el mouse por ellos, para avanzar',(pantalla.get_width()/8-pantalla.get_width()/26,pantalla.get_height()/4),pantalla.get_width()/30,color=(0,0,0))
        rectClaves = draw('images\\claves.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/19,pantalla.get_height()/2.5))
        rectPiano = draw('images\\piano.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/2-pantalla.get_width()/11,pantalla.get_height()/2.5))
        rectPlatillo = draw('images\\platillo.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/20+pantalla.get_width()/1.4,pantalla.get_height()/2.5))
        if 'piano' in instrumentosEscuchados and 'claves' in instrumentosEscuchados and 'platillo' in instrumentosEscuchados:
            rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))
        if rectClaves.collidepoint(mPos) :
            if clavesSound.get_num_channels() == 0:
                pianoSound.stop()
                platillosSound.stop()
                clavesSound.play()
                instrumentosEscuchados.append('claves')
                clavesSound.fadeout(5000)
        if rectPiano.collidepoint(mPos):
            if pianoSound.get_num_channels() == 0:
                platillosSound.stop()
                clavesSound.stop()
                pianoSound.play()
                instrumentosEscuchados.append('piano')
                pianoSound.fadeout(5000)
        if rectPlatillo.collidepoint(mPos):
            if platillosSound.get_num_channels() == 0:
                pianoSound.stop()
                clavesSound.stop()
                platillosSound.play()
                instrumentosEscuchados.append('platillo')
                platillosSound.fadeout(5000)
    if diapositiva == 15:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        if cambioAleatorio == False:
            if instrumentosEscuchados == []:
                aleatorio = random.randint(0,2)
            if instrumentosEscuchados == ['claves']:
                aleatorio = 0
            if instrumentosEscuchados == ['piano']:
                aleatorio = 2
            if instrumentosEscuchados == ['platillo']:
                aleatorio = 1
            if 'claves' in instrumentosEscuchados and 'piano' in instrumentosEscuchados:
                aleatorio = 2
            if 'piano' in instrumentosEscuchados and 'platillo' in instrumentosEscuchados:
                aleatorio = 0
            if 'claves' in instrumentosEscuchados and 'platillo' in instrumentosEscuchados:
                aleatorio = 1
        rectClaves = draw('images\\claves.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/19,pantalla.get_height()/2.5))
        rectPiano = draw('images\\piano.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/2-pantalla.get_width()/11,pantalla.get_height()/2.5))
        rectPlatillo = draw('images\\platillo.png',(pantalla.get_width()/5.5,pantalla.get_height()/3),(pantalla.get_width()/20+pantalla.get_width()/1.4,pantalla.get_height()/2.5))
        header('¿Cúal instrumento suena?',(pantalla.get_width()/20,pantalla.get_height()/8),pantalla.get_width()/16)
        if aleatorio == 0 and cambioAleatorio == False and 'claves' not in instrumentosEscuchados:
            if clavesSound.get_num_channels() == 0:
                clavesSound.play()
                clavesSound.fadeout(10000)
        if aleatorio == 1 and cambioAleatorio == False and 'piano' not in instrumentosEscuchados:
            if pianoSound.get_num_channels() == 0:
                pianoSound.play()
                pianoSound.fadeout(10000)
        if aleatorio == 2 and cambioAleatorio == False and 'platillo' not in instrumentosEscuchados:
            if platillosSound.get_num_channels() == 0:
                platillosSound.play()
                platillosSound.fadeout(10000)
        if 'piano' in instrumentosEscuchados and 'platillo' in instrumentosEscuchados and 'claves' in instrumentosEscuchados and escuchoTodos == True:
            rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))
            header('Ya reconociste todos los instrumentos',(pantalla.get_width()/6,pantalla.get_height()/1.3),(pantalla.get_width()/30),(0,0,0))
        cambioAleatorio = True
    if diapositiva == 16:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        if 'piano' in instrumentosEscuchados and 'claves' in instrumentosEscuchados and 'platillo' in instrumentosEscuchados:
            escuchoTodos = True
        if bpm120.get_num_channels() == 0:
            bpm120.play()
        header('Sigue el ritmo',(pantalla.get_width()/5,pantalla.get_height()/2.3),(pantalla.get_width()/10),(0,0,0))
        header('presionando la',(pantalla.get_width()/5,pantalla.get_height()/1.8),(pantalla.get_width()/10),(0,0,0))
        header('barra de espacio',(pantalla.get_width()/5,pantalla.get_height()/1.5),(pantalla.get_width()/10),(0,0,0))
        barraNivel3.draw()
        if finBarra == True:
            finBarra = False
            pygame.time.delay(500)
            bpm120.stop()
            diapositiva = 17
            cambioAleatorio = True
            contador = 0
            tiempoInicial = 0
            escuchoTodos = False
            barraNivel3.progress = 0
        if barraNivel3.limit == barraNivel3.progress:
            finBarra = True
        if contador >= 5525 and barraNivel3.progress < barraNivel3.limit/2 or contador >=11050 and barraNivel3.progress<barraNivel3.limit:
            barraNivel3.progress = 0
            bpm120.stop()
            diapositiva = 10
            cambioAleatorio = True
            contador = 0
            tiempoInicial = 0
            instrumentosEscuchados = []
            escuchoTodos = False
    if diapositiva == 17:
        pantalla.fill((255,255,255))
        rectBack = draw('images\\background.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        rectAnterior= draw('images\\anterior.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()/7,pantalla.get_height()-pantalla.get_height()/4))
        rectSiguiente = draw('images\\siguiente.png',(pantalla.get_width()/8,pantalla.get_height()/7),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))
        rect3Estrellas = draw('images\\3 estrellas.png',(pantalla.get_width()/1.5,pantalla.get_height()/2.5),(pantalla.get_width()/6,pantalla.get_height()/3.5))
        header('¡Pasaste el mundo 1!',(pantalla.get_width()/5.8,pantalla.get_height()/7.3),(pantalla.get_width()/10),(0,0,0))
        if len(instrumentosEscuchados) == 3 and cambioAleatorio == False:
            header('Ya hizo el ejercicio con los 3 instrumentos',(pantalla.get_width()/4,pantalla.get_height()/1.4),(pantalla.get_width()/25),(0,0,0))
    if diapositiva == 18:
        rectBack = draw('images\\final.png',(pantalla.get_width(),pantalla.get_height()),(0,0))
        rectFin = draw('images\\restart.png',(pantalla.get_width()/8,pantalla.get_height()/6),(pantalla.get_width()-pantalla.get_width()/5,pantalla.get_height()-pantalla.get_height()/4))