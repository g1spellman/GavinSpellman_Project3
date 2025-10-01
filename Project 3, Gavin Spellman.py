import dearpygui.dearpygui as drawing
import comp151Colors
#lets draw a rabbit
drawing.create_context()
drawing.create_viewport(title='My Drawing', width=900, height=900)
with drawing.window(label='My Drawing', width=900, height=900):
    with drawing.drawlist(width=900, height=900):
        drawing.draw_triangle((300,0), (400,150), (210,150),
                              color=comp151Colors.BLACK, fill=comp151Colors.PINK)
        drawing.draw_triangle((600, 0),(700,150), (500,150),
                              color=comp151Colors.BLACK, fill=comp151Colors.PINK)
        drawing.draw_circle((450, 200), 100,
                            color=comp151Colors.BLACK, fill=comp151Colors.PINK)
        drawing.draw_rectangle((400, 230), (500, 200),
                               color=comp151Colors.BLACK, fill=comp151Colors.BLACK)
        drawing.draw_line((300,200), (300,500), color=comp151Colors.BLACK,
                  thickness=2)

drawing.setup_dearpygui()
drawing.show_viewport()
drawing.start_dearpygui()
drawing.destroy_context()