import os
import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
import numpy as np

# Run this script with "-c" to connect to Tecplot 360 on port 7600
# To enable connections in Tecplot 360, click on:
#   "Scripting" -> "PyTecplot Connections..." -> "Accept connections"
import sys
if '-c' in sys.argv:
    tp.session.connect()


tp.macro.execute_command('$!LoadColorMap "C:\\Users\\hirok\\Documents\\01_Lab\\01_Research-20231023\\77_TecPlot関係-航空写真など\\Colarmap-v01.map"')
tp.macro.execute_command('$!LoadColorMap "C:\\Users\\hirok\\Documents\\01_Lab\\01_Research-20231023\\77_TecPlot関係-航空写真など\\Colarmap-v02-20240301.map"')

xslice=0.0
yslice=0.0
zslice=0.0

#cont_flag=1
for cont_flag in range(4,6):
    if cont_flag == 4:
        output_folder_png="01_png/Fig27"
    elif cont_flag == 5:
        output_folder_png="01_png/Fig28"
    os.makedirs(output_folder_png, exist_ok=True)

    input_folder="Tec3D_Front_plt"
    for file_name in os.listdir(input_folder):
        bn, en =  os.path.splitext( file_name )
        if en == '.plt':
            tp.new_layout()
            tp.macro.execute_command('''$!Pick AddAtPosition
                X = 1.02762730228
                Y = 3.96830985915
                ConsiderStyle = Yes''')
            tp.macro.execute_command('''$!FrameControl ActivateByNumber
                Frame = 1''')
            tp.macro.execute_command('''$!Pick Shift
                X = -2.74756229686
                Y = 0
                PickSubposition = Left''')
            tp.macro.execute_command('''$!Pick Shift
                X = 2.67822318527
                Y = 0
                PickSubposition = Right''')
            
            datafile=os.path.join(input_folder, file_name)

            dataset = tp.data.load_tecplot(datafile)
            
            frame = tp.active_frame()
            frame.plot_type = tp.constant.PlotType.Cartesian3D
            frame.show_border = False
            frame.show_header = False
            frame.transparent = False
            axes = frame.plot().axes

            tp.active_frame().plot().axes.orientation_axis.show = False

            t,u=bn.split('_')
            fn='./TecScatter_plt/TecScatter_'+ u +'.plt'

            dataset2 = tp.data.load_tecplot(fn)

            axes.x_axis.variable = dataset.variable('xp')
            axes.y_axis.variable = dataset.variable('yp')
            axes.z_axis.variable = dataset.variable('zp')

            tp.active_frame().plot().show_shade=False
            tp.active_frame().plot().show_scatter=True
            tp.active_frame().plot().scatter.variable_index=11
            tp.active_frame().plot().fieldmaps(0).scatter.show=False
            tp.active_frame().plot().fieldmaps(1).scatter.symbol().shape=GeomShape.Sphere
            tp.active_frame().plot().fieldmaps(1).scatter.size_by_variable=True
            tp.active_frame().plot().scatter.relative_size=1
            tp.active_frame().plot().rgb_coloring.red_variable_index=6
            tp.active_frame().plot().rgb_coloring.green_variable_index=3
            tp.active_frame().plot().rgb_coloring.blue_variable_index=3
            tp.active_frame().plot().contour(0).variable_index=3  
            tp.active_frame().plot().contour(1).variable_index=13 
            tp.active_frame().plot().contour(2).variable_index=14
            tp.active_frame().plot().contour(3).variable_index=15 
            tp.active_frame().plot().contour(4).variable_index=16 
            tp.active_frame().plot().contour(5).variable_index=22 
            tp.active_frame().plot().contour(6).variable_index=8  
            tp.active_frame().plot().contour(7).variable_index=9  
            tp.active_frame().plot(PlotType.Cartesian3D).show_slices=False
            tp.active_frame().plot().fieldmaps(0).contour.contour_type=ContourType.Overlay
            tp.active_frame().plot().fieldmaps(0).contour.flood_contour_group_index=0
            tp.active_frame().plot().fieldmaps(0).contour.line_group_index=3
            
            levels0 = tp.active_frame().plot().contour(0).levels
            levels0.reset_levels([-1, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6,  6.5,  7])
            tp.active_frame().plot().contour(0).colormap_name='Large Rainbow modified (2)'

            levels1 = tp.active_frame().plot().contour(1).levels
            levels1.reset_levels([0,0.3,0.6,0.9,1.2,1.5,1.8,2.1,2.4,2.7,3.0])
            tp.active_frame().plot().contour(1).colormap_name='Large Rainbow modified (2)'

        
            levels2 = tp.active_frame().plot().contour(2).levels
            levels2.reset_levels([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5])
            tp.active_frame().plot().contour(2).colormap_name='Large Rainbow modified (2)'

            levels3 = tp.active_frame().plot().contour(3).levels
            levels3.reset_levels([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5])
            tp.active_frame().plot().contour(3).colormap_name='Large Rainbow modified (2)'

            levels4 = tp.active_frame().plot().contour(4).levels
            levels4.reset_levels([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5])
            tp.active_frame().plot().contour(4).colormap_name='Large Rainbow modified (2)'
            tp.active_frame().plot().contour(4).legend.header.show = False

            levels5 = tp.active_frame().plot().contour(5).levels
            levels5.reset_levels([-1.5, -1.0, -0.5, 0.0, 0.5, 1.0, 1.5])
            tp.active_frame().plot().contour(5).colormap_name='Large Rainbow modified (2)'
            tp.active_frame().plot().contour(5).legend.header.show = False

            levels6 = tp.active_frame().plot().contour(6).levels
            levels6.reset_levels([0.3])
            tp.active_frame().plot().contour(6).colormap_name='GrayScale'

            levels7 = tp.active_frame().plot().contour(7).levels
            levels7.reset_levels([2.8, 3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2])
            tp.active_frame().plot().contour(7).colormap_name='Large Rainbow'

            tp.active_frame().plot(PlotType.Cartesian3D).vector.u_variable_index=3
            tp.active_frame().plot(PlotType.Cartesian3D).vector.v_variable_index=4
            tp.active_frame().plot(PlotType.Cartesian3D).vector.w_variable_index=5
            tp.active_frame().plot(PlotType.Cartesian3D).vector.even_spacing.z=0.1
            tp.active_frame().plot(PlotType.Cartesian3D).vector.even_spacing.x=0.1
            tp.active_frame().plot(PlotType.Cartesian3D).vector.relative_length=0.1
            tp.active_frame().plot(PlotType.Cartesian3D).vector.arrowhead_fraction=0.5
            tp.active_frame().plot(PlotType.Cartesian3D).vector.relative_length=0.05

            tp.active_frame().plot().contour(0).legend.show=True
            tp.active_frame().plot().contour(0).legend.vertical=False
            tp.active_frame().plot().contour(0).legend.box.box_type=tp.constant.TextBox.None_
            tp.active_frame().plot().contour(0).legend.position = (97.8839, 95.818)

            tp.active_frame().plot().contour(1).legend.show=True
            tp.active_frame().plot().contour(1).legend.vertical=True
            tp.active_frame().plot().contour(1).legend.box.box_type=tp.constant.TextBox.None_
            tp.active_frame().plot().contour(1).legend.position = (95, 80)

            tp.active_frame().plot().contour(2).legend.show=True
            tp.active_frame().plot().contour(2).legend.vertical=True
            tp.active_frame().plot().contour(2).legend.box.box_type=tp.constant.TextBox.None_
            tp.active_frame().plot().contour(2).legend.position = (99.6749, 98.31)
            tp.active_frame().plot().contour(2).color_cutoff.include_min=True
            tp.active_frame().plot().contour(2).color_cutoff.min=-10000

            tp.active_frame().plot().contour(3).legend.show=True
            tp.active_frame().plot().contour(3).legend.vertical=True
            tp.active_frame().plot().contour(3).legend.box.box_type=tp.constant.TextBox.None_
            tp.active_frame().plot().contour(3).legend.position = (99.6749, 98.31)
            tp.active_frame().plot().contour(3).color_cutoff.include_min=True
            tp.active_frame().plot().contour(3).color_cutoff.min=-10000

            tp.active_frame().plot().contour(4).legend.show=True
            tp.active_frame().plot().contour(4).legend.vertical=True
            tp.active_frame().plot().contour(4).legend.box.box_type=tp.constant.TextBox.None_
            tp.active_frame().plot().contour(4).legend.position = (79.8478, 93.3258)
            tp.active_frame().plot().contour(4).color_cutoff.include_min=True
            tp.active_frame().plot().contour(4).color_cutoff.min=0
            tp.active_frame().plot().contour(4).color_cutoff.include_min=True
            tp.active_frame().plot().contour(4).color_cutoff.min=-10000
            tp.active_frame().plot().contour(4).legend.number_font.size=3.5

            tp.active_frame().plot().contour(5).legend.show=True
            tp.active_frame().plot().contour(5).legend.vertical=True
            tp.active_frame().plot().contour(5).legend.box.box_type=tp.constant.TextBox.None_
            tp.active_frame().plot().contour(5).legend.position = (79.8478, 93.3258)
            tp.active_frame().plot().contour(5).color_cutoff.include_min=True
            tp.active_frame().plot().contour(5).color_cutoff.min=-10000
            tp.active_frame().plot().contour(5).legend.number_font.size=3.5
            
            tp.active_frame().plot().contour(6).legend.show=False  
            tp.active_frame().plot().contour(6).legend.vertical=False
            tp.active_frame().plot().contour(6).legend.box.box_type=tp.constant.TextBox.None_
            tp.active_frame().plot().contour(6).legend.position = (88.8365, 89.6425)

            tp.active_frame().plot().contour(7).legend.show=True
            tp.active_frame().plot().contour(7).legend.vertical=True
            tp.active_frame().plot().contour(7).legend.box.box_type=tp.constant.TextBox.None_
            tp.active_frame().plot().contour(7).legend.position = (95, 80)

            if cont_flag == 99:
                tp.active_frame().plot().fieldmaps(1).scatter.color=tp.active_frame().plot().contour(0)
            elif cont_flag == 0:
                tp.active_frame().plot().fieldmaps(1).scatter.color=tp.active_frame().plot().contour(0)
            elif cont_flag == 1:
                tp.active_frame().plot().fieldmaps(1).scatter.color=tp.active_frame().plot().contour(1)
            elif cont_flag == 2:
                tp.active_frame().plot().fieldmaps(1).scatter.color=tp.active_frame().plot().contour(2)
            elif cont_flag == 3:
                tp.active_frame().plot().fieldmaps(1).scatter.color=tp.active_frame().plot().contour(3)
            elif cont_flag == 4:
                tp.active_frame().plot().fieldmaps(1).scatter.color=tp.active_frame().plot().contour(4)
            elif cont_flag == 5:
                tp.active_frame().plot().fieldmaps(1).scatter.color=tp.active_frame().plot().contour(5)
            elif cont_flag == 6:
                tp.active_frame().plot().fieldmaps(1).scatter.color=tp.active_frame().plot().contour(6)
            elif cont_flag == 7:
                tp.active_frame().plot().fieldmaps(1).scatter.color=tp.active_frame().plot().contour(7)

            tp.active_frame().plot().vector.reset_even_spacing()
            tp.active_frame().plot(PlotType.Cartesian3D).vector.even_spacing.x=0.1
            tp.active_frame().plot(PlotType.Cartesian3D).vector.even_spacing.z=0.1


            # isosurface
            tp.active_frame().plot().isosurface(0).show=True
            tp.active_frame().plot().isosurface(0).definition_contour_group_index=6
            tp.active_frame().plot().isosurface(0).isosurface_values[0]=0
            tp.active_frame().plot().isosurface(0).contour.flood_contour_group_index=7
            tp.active_frame().plot(PlotType.Cartesian3D).show_isosurfaces=True
            tp.active_frame().plot().isosurface(0).contour.show=False
            tp.active_frame().plot().isosurface(0).contour.contour_type=ContourType.Overlay
            tp.active_frame().plot().isosurface(0).contour.flood_contour_group_index=7
            tp.active_frame().plot().isosurface(0).contour.line_contour_group_index=7  
            tp.active_frame().plot().isosurface(0).shade.show=True
            tp.active_frame().plot().isosurface(0).shade.color=Color.White 
            tp.active_frame().plot().isosurface(0).effects.use_translucency=True
            tp.active_frame().plot().isosurface(0).effects.surface_translucency=70
            tp.active_frame().plot().isosurface(0).obey_source_zone_blanking=True

            tp.active_frame().plot().isosurface(1).show=True
            tp.active_frame().plot().isosurface(1).definition_contour_group_index=7
            tp.active_frame().plot().isosurface(1).isosurface_values[0]=0
            tp.active_frame().plot().isosurface(1).contour.flood_contour_group_index=7
            tp.active_frame().plot(PlotType.Cartesian3D).show_isosurfaces=True
            tp.active_frame().plot().isosurface(1).contour.show=False
            tp.active_frame().plot().isosurface(1).contour.contour_type=ContourType.Overlay
            tp.active_frame().plot().isosurface(1).contour.flood_contour_group_index=7
            tp.active_frame().plot().isosurface(1).contour.line_contour_group_index=7  
            tp.active_frame().plot().isosurface(1).shade.show=True
            tp.active_frame().plot().isosurface(1).shade.color=Color.Black
            tp.active_frame().plot().isosurface(1).effects.use_translucency=False
            tp.active_frame().plot().isosurface(1).effects.surface_translucency=60
            tp.active_frame().plot().isosurface(1).obey_source_zone_blanking=False

            x_slice_location = -0.01250
            y_start = -2.0
            y_end =    2.0
            z_start = 2.51250 
            z_end = 3.5
            num_left_right_slices = 20  
            num_top_bottom_slices =  5  
            tp.active_frame().plot().show_streamtraces = True
            streamtraces = tp.active_frame().plot().streamtraces
            tp.active_frame().plot().streamtraces.color=tp.active_frame().plot().contour(0)
            streamtraces.show_paths = True

            rod = streamtraces.rod_ribbon
            rod.width = .03
            rod.contour.show = True

            for z in np.linspace(z_start, z_end, num=num_top_bottom_slices):
                tp.active_frame().plot().streamtraces.add_rake(start_position=[x_slice_location, y_start, z],
                                                                end_position=[x_slice_location, y_end, z],
                                                                stream_type=Streamtrace.VolumeLine,
                                                                num_seed_points=8)
            tp.active_frame().plot().streamtraces.rod_ribbon.contour.show=False
            tp.active_frame().plot().streamtraces.line_thickness=0.4
            tp.active_frame().plot().streamtraces.show_arrows=True
            tp.active_frame().plot().streamtraces.arrowhead_size=3
            tp.active_frame().plot().streamtraces.arrowhead_spacing=5
            tp.active_frame().plot().streamtraces.color=Color.White

            tp.active_frame().plot().axes.grid_area.filled=False
            axes.preserve_scale=True


            xmaxhk=dataset.variable('xp').max()
            xminhk=dataset.variable('xp').min()
            ymaxhk=dataset.variable('yp').max()
            yminhk=dataset.variable('yp').min()
            zmaxhk=dataset.variable('zp').max()
            zminhk=dataset.variable('zp').min()

            xaxis = axes.x_axis
            xaxis.show = True
            xaxis.title.show = True
            xaxis.title.text = 'x[m]'
            xaxis.title.title_mode = AxisTitleMode.UseText
            xaxis.line.show=True
            xaxis.tick_labels.font.size = 5    #10
            xaxis.grid_lines.show = True

            yaxis = axes.y_axis
            yaxis.show = True
            yaxis.line.show=True
            yaxis.grid_lines.show = True
            yaxis.title.show = True
            yaxis.title.text = 'y[m]'
            yaxis.title.title_mode = AxisTitleMode.UseText
            yaxis.tick_labels.font.size = 5
            yaxis.min = -4.0  
            yaxis.max =  4.0 

            zaxis = axes.z_axis
            zaxis.show = False
            zaxis.line.show=False
            zaxis.grid_lines.show = True
            zaxis.title.show = True
            zaxis.title.text = 'z[m]'
            zaxis.title.title_mode = AxisTitleMode.UseText
            zaxis.line.show_on_opposite_edge = True
            zaxis.ticks.show_on_opposite_edge = True
            zaxis.tick_labels.show_on_opposite_edge = True
            zaxis.tick_labels.font.size = 5
            zaxis.min = 2.5 

            tp.macro.execute_command("""$!AttachText 
            AnchorPos
                {
                X = 49.9995
                Y = 85.3738
                }
            TextShape
                {
                IsBold = No
                Height = 25
                }
            Text = 'time=&(solutiontime)[s]'""")
            
            tp.macro.execute_command("""$!AttachText 
                AnchorPos
                    {
                    X = 22.6623
                    Y = 8.55905
                    }
                TextShape
                    {
                    IsBold = No
                    Height = 20
                    }
                Text = 'Front position'""")
            
            tp.macro.execute_command("""$!AttachText 
                AnchorPos
                    {
                    X = 60.634
                    Y = 74.2145
                    }
                TextShape
                    {
                    IsBold = No
                    Height = 20
                    }
                Text = 'Flow'""")
            
            if cont_flag == 4:
                tp.macro.execute_command("""$!AttachText 
                    AnchorPos
                        {
                        X = 68.9253
                        Y = 92.3077
                        }
                    TextShape
                        {
                        FontFamily = 'Century Schoolbook'
                        IsBold = No
                        }
                    Text = 'F<sup>f</sup><sub>x</sub> / mgsin<greek>q</greek>'""")
            elif cont_flag == 5:
                tp.macro.execute_command("""$!AttachText 
                    AnchorPos
                        {
                        X = 68.9253
                        Y = 92.3077
                        }
                    TextShape
                        {
                        FontFamily = 'Century Schoolbook'
                        IsBold = No
                        }
                    Text = 'F<sup>f</sup><sub>z</sub> / mgcos<greek>q</greek>'""")
            

            line0 = frame.add_polyline([[30.3528,12.6761], [33.7775,16.5764]], coord_sys=CoordSys.Frame)
            line0.arrowhead.attachment = ArrowheadAttachment.AtEnd
            line0.line_thickness = 0.5
            line0.arrowhead.style = ArrowheadStyle.Filled
            line0.arrowhead.angle = 22
            line0.arrowhead.size = 2

            line1 = frame.add_polyline([[59.0118,70.8559], [62.857,65.2221]], coord_sys=CoordSys.Frame)
            line1.arrowhead.attachment = ArrowheadAttachment.AtEnd
            line1.line_thickness = 0.5
            line1.arrowhead.style = ArrowheadStyle.Filled
            line1.arrowhead.angle = 22
            line1.arrowhead.size = 2

            tp.active_frame().plot().value_blanking.active = True

            constraint = tp.active_frame().plot().value_blanking.constraint(1)
            constraint.active = False
            constraint.compare_by = ConstraintOp2Mode.UseConstant
            constraint.comparison_operator = RelOp.LessThan                
            constraint.comparison_value = 0.3 
            constraint.variable = dataset.variable('vrx')

            constraint2 = tp.active_frame().plot().value_blanking.constraint(2)
            constraint2.active = False
            constraint2.compare_by = ConstraintOp2Mode.UseConstant
            constraint2.comparison_operator = RelOp.GreaterThan               
            constraint2.comparison_value = yslice + 0.3 
            constraint2.variable = dataset.variable('yp')
            #constraint2.variable_index=17 


            constraint3 = tp.active_frame().plot().value_blanking.constraint(3)
            constraint3.active = False
            constraint3.compare_by = ConstraintOp2Mode.UseConstant
            constraint3.comparison_operator = RelOp.LessThan               
            constraint3.comparison_value = yslice - 0.3 
            constraint3.variable = dataset.variable('yp')

            constraint4 = tp.active_frame().plot().value_blanking.constraint(4)
            constraint4.active = False
            constraint4.compare_by = ConstraintOp2Mode.UseConstant
            constraint4.comparison_operator = RelOp.LessThan               
            constraint4.comparison_value = 0.0
            constraint4.variable = dataset.variable('sf-zp')

            constraint4 = tp.active_frame().plot().value_blanking.constraint(5)
            constraint4.active = True
            constraint4.compare_by = ConstraintOp2Mode.UseConstant
            constraint4.comparison_operator = RelOp.GreaterThan                 
            constraint4.comparison_value = 0.0
            constraint4.variable = dataset.variable('zbp-zp')

            tp.active_frame().plot().axes.orientation_axis.show = False

            tp.active_frame().plot().activate()
            tp.active_frame().plot().view.width = 20.3776
            tp.active_frame().plot().view.alpha = -8.67 
            tp.active_frame().plot().view.theta = -41.14 
            tp.active_frame().plot().view.psi   = 49.69 

            tp.active_frame().plot().view.position = (xmaxhk+34, -43.1939, 53.1403)
            tp.active_frame().plot().view.distance = 76.7287083735  


            fname = os.path.basename(file_name)

            bname, ext =  os.path.splitext( fname )

            fpath= output_folder_png + '/' + bname  + '.png'

            tp.export.save_png(fpath, 1200, supersample=3)
            print(bname)
