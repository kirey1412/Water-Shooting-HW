import pgzrun, random

TITLE="Water Gun"
WIDTH=680
HEIGHT=460

speed=5

bullets=[]
enemies=[]

score=0
defender=Actor("watergun.png")
for i in range(7):
    enemy=Actor("bubbles.png")
    enemies.append(enemy)
    enemies[-1].x=WIDTH+100 #to update recently added element
    enemies[-1].y=100+90*i

defender.pos=(50, HEIGHT/2)

def draw():
    screen.clear()
    screen.fill("skyblue")
    defender.draw()
    for i in enemies:
        i.draw()
    screen.draw.text(str(score), (50,50), color="navy")
    for i in bullets:
        i.draw()

def update():
    global score
    if keyboard.left:
        defender.y+=speed
        if defender.y>HEIGHT-50:
            defender.y=HEIGHT-50
    elif keyboard.right:
        defender.y-=speed
        if defender.y<50:
            defender.y=50
    for e in enemies:
        e.x-=2
        if e.x<0:
            e.x-=100
            e.y=random.randint(50, HEIGHT-50)
        for a in bullets:
            if e.colliderect(a):
                enemies.remove(e)
                bullets.remove(a)
                score+=20

    for b in bullets:
        b.x+=5
        if b.x>WIDTH:
            bullets.remove(b)

def on_key_down(key):
    if key==keys.SPACE:
        bullets.append(Actor("water"))
        bullets[-1].y=defender.y
        bullets[-1].x=defender.x+80

pgzrun.go()