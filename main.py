from pyjoycon import get_R_id, get_L_id, JoyCon
import time
import pygame

idsR = get_R_id()
idsL = get_L_id()

joyconR = JoyCon(idsR[0], idsR[1])
joyconL = JoyCon(idsL[0], idsL[1])

lastHitR = 0
lastHitL = 0

lastHit = ""
lastHitTime = 0

prevXR = 0
prevXL = 0

prevDeltaXR = 0
prevDeltaXL = 0

pygame.mixer.init()
pygame.font.init()

font_pad = pygame.font.Font(None, 28)
font_pad.set_bold(True)

font_title = pygame.font.Font(None, 64)
font_title.set_bold(True)

font_instr = pygame.font.Font(None, 24)

kickdrum = pygame.mixer.Sound("sounds/kickdrum.wav")
cymbal = pygame.mixer.Sound("sounds/cymbal.wav")
snare = pygame.mixer.Sound("sounds/snare.wav")
hihat = pygame.mixer.Sound("sounds/hihat.wav")

screen = pygame.display.set_mode((900, 500))
pygame.display.set_caption("AirDrums")

running = True

circulos = {
    "hihat":  {"pos": (150, 260), "color": (0, 255, 120), "label": "HI-HAT"},
    "cymbal": {"pos": (350, 300), "color": (255, 215, 0), "label": "CYMBAL"},
    "kick":   {"pos": (550, 300), "color": (255, 140, 0), "label": "KICK"},
    "snare":  {"pos": (750, 260), "color": (0, 200, 255), "label": "SNARE"},
}

RADIO = 60

try:
    while running:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.mixer.stop()
                running = False

        if joyconR.get_button_b():
            pygame.mixer.stop()
            break

        # Lectura
        xR = joyconR.get_accel_x()
        yR = joyconR.get_accel_y()
        zR = joyconR.get_accel_z()

        xL = joyconL.get_accel_x()
        yL = joyconL.get_accel_y()
        zL = joyconL.get_accel_z()

        buttonZR = joyconR.get_button_zr()
        buttonZL = joyconL.get_button_zl()

        vectorAccelR = (xR**2 + yR**2 + zR**2)**0.5
        vectorAccelL = (xL**2 + yL**2 + zL**2)**0.5

        deltaXR = xR - prevXR
        deltaXL = xL - prevXL

        # DERECHA
        if (
            vectorAccelR > 7000 and
            prevDeltaXR < -450 and
            deltaXR > -200 and
            (time.time() - lastHitR) > 0.125
        ):
            lastHitR = time.time()

            if buttonZR:
                snare.play()
                lastHit = "snare"
                lastHitTime = time.time()
            else:
                kickdrum.play()
                lastHit = "kick"
                lastHitTime = time.time()

        # IZQUIERDA
        if (
            vectorAccelL > 7000 and
            prevDeltaXL < -450 and
            deltaXL > -200 and
            (time.time() - lastHitL) > 0.125
        ):
            lastHitL = time.time()

            if buttonZL:
                hihat.play()
                lastHit = "hihat"
                lastHitTime = time.time()
            else:
                cymbal.play()
                lastHit = "cymbal"
                lastHitTime = time.time()

        prevXR = xR
        prevXL = xL
        prevDeltaXR = deltaXR
        prevDeltaXL = deltaXL

        # UI
        screen.fill((10, 10, 15))

        title = font_title.render("AIRDRUMS", True, (255,255,255))
        title_rect = title.get_rect(center=(450, 60))
        screen.blit(title, title_rect)

        instr = font_instr.render("L = CYMBAL | R = KICK | + ZR/ZL = SNARE / HI-HAT", True, (180,180,180))
        instr_rect = instr.get_rect(center=(450, 110))
        screen.blit(instr, instr_rect)

        for nombre, c in circulos.items():
            pos = c["pos"]
            base_color = c["color"]

            t = time.time() - lastHitTime
            intensidad = max(0, 1 - t / 0.2) if lastHit == nombre else 0

            extra = int(25 * intensidad)
            radio = RADIO + extra

            color = (
                min(255, int(base_color[0] + 100 * intensidad)),
                min(255, int(base_color[1] + 100 * intensidad)),
                min(255, int(base_color[2] + 100 * intensidad)),
            )

            pygame.draw.circle(screen, color, pos, radio)
            pygame.draw.circle(screen, (255,255,255), pos, radio, 2)

            label = font_pad.render(c["label"], True, (255,255,255))
            label_rect = label.get_rect(center=pos)
            screen.blit(label, label_rect)

        pygame.display.flip()
        time.sleep(0.01)

except KeyboardInterrupt:
    pygame.mixer.stop()
    print("\nDetenido")
except Exception:
    pygame.mixer.stop()
    print("\nJoycon desconectado")