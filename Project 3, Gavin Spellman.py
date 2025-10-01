import dearpygui.dearpygui as drawing
import comp151Colors
#lets draw a rabbit
drawing.create_context()
drawing.create_viewport(title='Face', width=900, height=900)
with drawing.window(label='Face', width=900, height=900):
    with drawing.drawlist(width=900, height=900):
        drawing.draw_circle((450,450), 300,
                         color=comp151Colors.RED, fill=comp151Colors.ORANGE)
        drawing.draw_triangle((305,300), (395,410), (210,410),
                              color=comp151Colors.BLACK, fill=comp151Colors.GREEN)
        drawing.draw_triangle((650, 300),(740,410), (555,410),
                              color=comp151Colors.BLACK, fill=comp151Colors.GREEN)
        drawing.draw_rectangle((400,430), (500,460),
                               color=comp151Colors.BLACK, fill=comp151Colors.GREEN)
        drawing.draw_ellipse((300,550),(600,650),
                             color=comp151Colors.RED, fill=comp151Colors.GREEN)

drawing.setup_dearpygui()
drawing.show_viewport()
drawing.start_dearpygui()
drawing.destroy_context()