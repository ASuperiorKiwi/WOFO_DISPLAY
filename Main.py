import guizero

from guizero import App, Window, Text, Picture, PushButton, Drawing

control = App(title="Control Window")
pos = Window(control, title="POS", bg="Black")
pos.tk.attributes("-fullscreen",True)


#Image Assignment
scene_list = []


blackout = Picture(pos, image="blackout.png")
blackout.hide()
scene_list.append(blackout)

scene_cover = Picture(pos, image="Poster Widescreen Projector Aspect.png")
scene_cover.hide()
scene_list.append(scene_cover)

scene_1 = Picture(pos, image="white.png")
scene_1.hide()
scene_list.append(scene_1)

scene_11_balloon_stationary = Picture(pos, image="Scene 11 - Balloon Stationary.png")
scene_11_balloon_stationary.hide()
scene_list.append(scene_11_balloon_stationary)

scene_11_balloon_ascension = Picture(pos, image="Scene 11 - Balloon Ascension.gif")
scene_11_balloon_ascension.hide()
scene_list.append(scene_11_balloon_ascension)




#Definition Control


def switch_scene(_scene):
    for scene in scene_list:
        scene.hide()

    scene_list[_scene].show()


#Button Note argument is indexed not based on scene name or number

    #blackout
PushButton(control, text="Blackout", command=switch_scene, args=[0])

    #Cover
Text(control, text="Cover")
PushButton(control, text="Scene 0 Cover", command=switch_scene, args=[1])

    #scene 1
Text(control, text="Scene 1")
PushButton(control, text="Scene 1", command=switch_scene, args=[2])

    #scene 11
Text(control, text="Scene 11")
PushButton(control, text="Scene 11 - Balloon Stationary", command=switch_scene, args=[3])
PushButton(control, text="Scene 11 - Balloon Ascension", command=switch_scene, args=[4])

control.display()

