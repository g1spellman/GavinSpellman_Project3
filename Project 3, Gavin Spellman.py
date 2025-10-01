import dearpygui.dearpygui as drawing
import comp151Colors
#Rabbit
drawing.create_context()
drawing.create_viewport(title='My Drawing', width=900, height=900)
with drawing.window(label='Rabbit', width=900, height=900):
    with drawing.drawlist(width=900, height=900):
        #Sky
        drawing.draw_rectangle((0, 0), (1000, 1000),
                               color=comp151Colors.BLUE, fill=comp151Colors.BLUE)
        #Tail
        drawing.draw_circle((600, 500), 40, color=comp151Colors.WHITE,
                            fill=comp151Colors.WHITE)
        # Body
        drawing.draw_ellipse((585, 290), (320, 600), color=comp151Colors.BLACK,
                             fill=comp151Colors.PINK)
        drawing.draw_ellipse((550, 325), (350, 550), color=comp151Colors.BLACK,
                             fill=comp151Colors.WHITE)
        #Ears
        drawing.draw_triangle((300,0), (400,150), (210,150),
                              color=comp151Colors.BLACK, fill=comp151Colors.PINK)
        drawing.draw_triangle((600, 0),(700,150), (500,150),
                              color=comp151Colors.BLACK, fill=comp151Colors.PINK)
        #Head
        drawing.draw_circle((450, 200), 100,
                            color=comp151Colors.BLACK, fill=comp151Colors.PINK)
        #Nose
        drawing.draw_rectangle((400, 230), (500, 200),
                               color=comp151Colors.BLACK, fill=comp151Colors.BLACK)
        #Mouth
        drawing.draw_line((400,250), (500,250), color=comp151Colors.BLACK,
                  thickness=3)
        #Eyes
        drawing.draw_circle((400, 175), 25, color=comp151Colors.WHITE,
                            fill=comp151Colors.BLACK)
        drawing.draw_circle((500, 175), 25, color=comp151Colors.WHITE,
                            fill=comp151Colors.BLACK)
        drawing.draw_circle((400, 175), 15, color=comp151Colors.WHITE,
                            fill=comp151Colors.WHITE)
        drawing.draw_circle((500, 175), 15, color=comp151Colors.WHITE,
                            fill=comp151Colors.WHITE)
        #Feet
        drawing.draw_ellipse((500, 500), (750, 600),color=comp151Colors.BLACK,
                            fill = comp151Colors.PINK)
        drawing.draw_ellipse((150, 500), (400, 600), color=comp151Colors.BLACK,
                             fill=comp151Colors.PINK)
        #Text
        drawing.draw_text((300, 600), "By Gavin Spellman",
                               color=comp151Colors.RED, size=32)
        #Sun
        drawing.draw_circle((0, 0), 150, color=comp151Colors.YELLOW,
                            fill=comp151Colors.YELLOW)
        drawing.draw_arrow((150, 150), (0, 0),
                                color=comp151Colors.YELLOW, thickness=5)
        drawing.draw_arrow((200, 50), (0, 0),
                           color=comp151Colors.YELLOW, thickness=5)
        drawing.draw_arrow((25, 200), (0, 0),
                           color=comp151Colors.YELLOW, thickness=5)




drawing.setup_dearpygui()
drawing.show_viewport()
drawing.start_dearpygui()
drawing.destroy_context()