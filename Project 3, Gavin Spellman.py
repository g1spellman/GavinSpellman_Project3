import dearpygui.dearpygui as drawing
import comp151Colors
#lets draw a rabbit
drawing.create_context()
drawing.create_viewport(title='My Drawing', width=900, height=900)
with drawing.window(label='My Drawing', width=900, height=900):
    with drawing.drawlist(width=900, height=900):
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
        drawing.draw_circle((400, 175), 25, color=comp151Colors.RED,
                            fill=comp151Colors.BLACK)
        drawing.draw_circle((500, 175), 25, color=comp151Colors.RED,
                            fill=comp151Colors.BLACK)
        drawing.draw_circle((400, 175), 15, color=comp151Colors.WHITE,
                            fill=comp151Colors.WHITE)
        drawing.draw_circle((500, 175), 15, color=comp151Colors.WHITE,
                            fill=comp151Colors.WHITE)
        #Feet
        drawing.draw_ellipse((500, 500), (750, 600),color=comp151Colors.BLACK,
                            fill = comp151Colors.PINK)
        drawing.draw_ellipse((100, 500), (350, 600), color=comp151Colors.BLACK,
                             fill=comp151Colors.PINK)
        #Body


drawing.setup_dearpygui()
drawing.show_viewport()
drawing.start_dearpygui()
drawing.destroy_context()