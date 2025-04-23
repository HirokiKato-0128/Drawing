import os
import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
import numpy as np

# Uncomment the following line to connect to a running instance of Tecplot 360:
# tp.session.connect()

import sys
if '-c' in sys.argv:
    tp.session.connect()

tp.macro.execute_command('$!LoadColorMap "C:\\Users\\hirok\\Documents\\01_Lab\\01_Research-20231023\\77_TecPlot関係-航空写真など\\Colarmap-v01.map"')
tp.macro.execute_command('$!LoadColorMap "C:\\Users\\hirok\\Documents\\01_Lab\\01_Research-20231023\\77_TecPlot関係-航空写真など\\Colarmap-v02-20240301.map"')
tp.macro.execute_command('$!LoadColorMap "C:\\Users\\hirok\\Documents\\01_Lab\\01_Research-20231023\\77_TecPlot関係-航空写真など\\Colarmap-v03-20240801.map"')

output_folder_png="./01_PNG/Fig07"
os.makedirs(output_folder_png, exist_ok=True)


print("Start Frame01")
input_folder="TecEnergy_plt"
for file_name in os.listdir(input_folder):
    bn, en =  os.path.splitext( file_name )
    tp.new_layout()
    # Frame1 zbの描画 3D
    datafile=os.path.join(input_folder, file_name)
    dataset = tp.data.load_tecplot(datafile)
    tp.active_frame().plot_type=PlotType.Cartesian3D
    tp.active_frame().plot().axes.x_axis.variable_index=0
    tp.active_frame().plot().axes.y_axis.variable_index=1
    tp.active_frame().plot().axes.z_axis.variable_index=3

    tp.active_frame().plot().fieldmaps(0).shade.color=Color.Custom9

    tp.active_frame().plot().axes.grid_area.filled=False
    axes =tp.active_frame().plot().axes
    axes.preserve_scale=True

    xaxis = axes.x_axis
    xaxis.show = True
    xaxis.title.show = False
    xaxis.title.text = 'xp'
    xaxis.title.title_mode = AxisTitleMode.UseText
    xaxis.min = 5.0 #10.0  #4.0
    xaxis.max = 40.0  #25.0   #41.0
    xaxis.line.show=True
    xaxis.tick_labels.font.size = 12.5    #10
    xaxis.grid_lines.show = True

    yaxis = axes.y_axis
    yaxis.show = True
    yaxis.line.show=True
    yaxis.grid_lines.show = True
    yaxis.title.show = False
    yaxis.tick_labels.show=False
    yaxis.tick_labels.show_on_opposite_edge = True
    yaxis.tick_labels.font.size = 12.5
    yaxis.min = -4.0  #10.0  #4.0
    yaxis.max =  4.0 #25.0   #41.0

    zaxis = axes.z_axis
    zaxis.show = False
    zaxis.line.show=False
    zaxis.grid_lines.show = False
    zaxis.title.show = False
    zaxis.line.show_on_opposite_edge = False
    zaxis.ticks.show_on_opposite_edge = False
    zaxis.tick_labels.show_on_opposite_edge = False
    zaxis.tick_labels.font.size = 5
    zaxis.min = 2.0
    zaxis.max = 4.0


    tp.active_frame().plot().axes.orientation_axis.show = False
    tp.active_frame().plot().activate()
    tp.active_frame().plot().view.width = 44.9685 
    tp.active_frame().plot().view.alpha = 0 
    tp.active_frame().plot().view.theta = 0.00 
    tp.active_frame().plot().view.psi   = 0

    tp.active_frame().plot().view.position = (22.5, 0.0, 234.533)
    tp.active_frame().plot().view.distance = 219.138209469  


    # Frame2 
    print("Start Frame02")
    tp.active_page().add_frame(position=(-0.58451,0.29334),
        size=(12.1,7.8613))
    tt,uu=bn.split('=')
    fn='./TecScatter_plt/TecScatter_kt='+ uu +'.plt'
    dataset2 = tp.data.load_tecplot(fn)
    tp.active_frame().plot_type=PlotType.Cartesian3D
    tp.active_frame().plot().frame.show_border=False
    tp.active_frame().plot().frame.transparent=True
    tp.macro.execute_command('''$!FrameControl ActivateByNumber
      Frame = 1''')
    tp.active_frame().plot().linking_between_frames.link_frame_size_and_position=True
    tp.active_frame().plot().linking_between_frames.link_view=True
    tp.macro.execute_command('''$!PropagateLinking 
      LinkType = BetweenFrames
      FrameCollection = All''')
    tp.macro.execute_command('''$!FrameControl ActivateByNumber
      Frame = 2''')
    tp.active_frame().plot().show_shade=False
    tp.active_frame().plot().show_scatter=True
    tp.active_frame().plot().scatter.variable_index=3
    tp.active_frame().plot().fieldmaps(0).scatter.symbol().shape=GeomShape.Sphere
    tp.active_frame().plot().fieldmaps(0).scatter.size_by_variable=True
    
    tp.active_frame().plot().contour(0).variable_index=4
    tp.active_frame().plot().contour(0).levels.reset_levels([0.5,1.5])
    tp.active_frame().plot().contour(0).colormap_name='Small Rainbow modified (2)'
    tp.active_frame().plot().fieldmaps(0).scatter.color=tp.active_frame().plot().contour(0)

    # Frame3 
    print("Start Frame03")
    tp.active_page().add_frame(position=(-0.27248,0.39735),
        size=(11.233,6.5612))
    dataset3 = tp.data.load_tecplot(datafile)
    tp.active_frame().plot_type=PlotType.Cartesian3D
    tp.active_frame().plot().frame.show_border=False
    tp.active_frame().plot().frame.transparent=True
    tp.macro.execute_command('''$!FrameControl ActivateByNumber
      Frame = 1''')
    tp.macro.execute_command('''$!PropagateLinking 
      LinkType = BetweenFrames
      FrameCollection = All''')
    tp.macro.execute_command('''$!FrameControl ActivateByNumber
      Frame = 3''')
    tp.active_frame().plot(PlotType.Cartesian3D).use_translucency=True
    tp.active_frame().plot().scatter.variable_index=4
    tp.active_frame().plot().fieldmaps(0).shade.color=Color.Cyan
    tp.active_frame().plot().value_blanking.constraint(0).variable_index=7
    tp.active_frame().plot().value_blanking.constraint(0).active=True
    tp.active_frame().plot().value_blanking.active=True
    tp.active_frame().plot().value_blanking.constraint(0).variable_index=0

    tp.active_frame().plot().value_blanking.active = True

    constraint = tp.active_frame().plot().value_blanking.constraint(1)
    constraint.active = True
    constraint.compare_by = ConstraintOp2Mode.UseConstant
    constraint.comparison_operator = RelOp.LessThanOrEqual             
    constraint.comparison_value = 0.0
    constraint.variable = dataset.variable('DaverageH')

    constraint2 = tp.active_frame().plot().value_blanking.constraint(2)
    constraint2.active = False
    constraint2.compare_by = ConstraintOp2Mode.UseConstant
    constraint2.comparison_operator = RelOp.EqualTo             
    constraint2.comparison_value = 1
    constraint2.variable = dataset.variable('DaverageH')

    fname = os.path.basename(file_name)
    bname, ext =  os.path.splitext( fname )

    fpath=output_folder_png + '/' + bname + '.png'
    tp.export.save_png(fpath, 2400, supersample=3)

print("Finish !!")