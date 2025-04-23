
import os
import tecplot as tp
from tecplot.exception import *
from tecplot.constant import *
import numpy as np


import sys
if '-c' in sys.argv:
    tp.session.connect()

tp.macro.execute_command('$!LoadColorMap "C:\\Users\\hirok\\Documents\\01_Lab\\01_Research-20231023\\77_TecPlot関係-航空写真など\\Colarmap-v01.map"')
tp.macro.execute_command('$!LoadColorMap "C:\\Users\\hirok\\Documents\\01_Lab\\01_Research-20231023\\77_TecPlot関係-航空写真など\\Colarmap-v02-20240301.map"')

xslice=0.0
yslice=0.0
zslice=0.0

input_folder="plt_journal"

for view_flag in range(1,2):
    for ContourIndex_Flood in range(0,1):
        KokuSyashin_flag=0
        vec_flag=1
        vecplace_flag=0
        iso_flag=0
        contour_flag=1
        shade_flag=0
        ContourType_flag=0
        blanking_flag = 1
        ContourIndex_Line = 2
        if view_flag == 1:
            kyorihyo_flag=0
            if ContourIndex_Flood == 0 :
                output_folder_png="./07_PNG/v01_u"
        os.makedirs(output_folder_png, exist_ok=True)
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
                frame.plot_type = tp.constant.PlotType.Cartesian2D
                frame.show_border = False
                frame.show_header = False
                frame.transparent = False
                axes = frame.plot().axes
                tp.active_frame().plot().show_shade=False

                ta,tb,tc=bn.split('_')
                tt,uu=tc.split('=')
                print(uu)
                tp.active_frame().plot().axes.x_axis.variable_index=0
                tp.active_frame().plot().axes.y_axis.variable_index=1
                tp.active_frame().plot().contour(0).variable_index=3     
                tp.active_frame().plot().contour(1).variable_index=4     
                tp.active_frame().plot().contour(2).variable_index=6     
                tp.active_frame().plot().contour(3).variable_index=7    
                tp.active_frame().plot().contour(4).variable_index=8     
                tp.active_frame().plot().contour(5).variable_index=9     
                tp.active_frame().plot().contour(6).variable_index=7     
                tp.active_frame().plot().contour(7).variable_index=7     
                tp.active_frame().plot().fieldmaps(0).contour.contour_type=ContourType.Overlay
                tp.active_frame().plot().fieldmaps(0).contour.flood_contour_group_index=0 
                tp.active_frame().plot().fieldmaps(0).contour.line_group_index=2 
                if contour_flag==0:
                    tp.active_frame().plot().show_contour=False
                elif contour_flag==1:
                    tp.active_frame().plot().show_contour=True
                tp.active_frame().plot().show_contour=True

                frame = tp.active_frame()
                axes = frame.plot().axes
                tp.active_frame().plot().fieldmaps(0).contour.line_thickness=0.25
                
                levels0 = tp.active_frame().plot().contour(0).levels
                levels0.reset_levels([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
                tp.active_frame().plot().contour(0).legend.position = (98, 98)
                tp.active_frame().plot().contour(0).colormap_name='Diverging - Brown/Green'
                tp.active_frame().plot().contour(0).legend.show=False
                tp.active_frame().plot().contour(0).legend.vertical=False
                tp.active_frame().plot().contour(0).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(0).legend.auto_resize=False
                tp.active_frame().plot().contour(0).labels.step=1

                levels1 = tp.active_frame().plot().contour(1).levels
                levels1.reset_levels([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
                tp.active_frame().plot().contour(1).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(1).legend.show=False
                tp.active_frame().plot().contour(1).legend.vertical=False
                tp.active_frame().plot().contour(1).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(1).legend.position = (98, 100)
                tp.active_frame().plot().contour(1).legend.auto_resize=True
                
                levels2 = tp.active_frame().plot().contour(2).levels
                levels2.reset_levels([1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600])
                tp.active_frame().plot().contour(2).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(2).legend.show=False
                tp.active_frame().plot().contour(2).legend.vertical=False
                tp.active_frame().plot().contour(2).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(2).legend.position = (98, 100)
                tp.active_frame().plot().contour(2).legend.auto_resize=True

                levels3 = tp.active_frame().plot().contour(3).levels
                levels3.reset_levels([0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000])
                tp.active_frame().plot().contour(3).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(3).legend.show=False
                tp.active_frame().plot().contour(3).legend.position = (98, 90)
                tp.active_frame().plot().contour(3).legend.vertical=False
                tp.active_frame().plot().contour(3).legend.box.box_type=tp.constant.TextBox.None_            
                tp.active_frame().plot().contour(3).legend.auto_resize=True

                levels4 = tp.active_frame().plot().contour(4).levels
                levels4.reset_levels([0]) 
                tp.active_frame().plot().contour(4).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(4).legend.show=True
                tp.active_frame().plot().contour(4).legend.vertical=False
                tp.active_frame().plot().contour(4).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(4).legend.position = (90, 100)
                tp.active_frame().plot().contour(4).legend.auto_resize=True

                levels5 = tp.active_frame().plot().contour(5).levels
                levels5.reset_levels([0]) 
                tp.active_frame().plot().contour(5).colormap_name='Large Rainbow modified (1)'
                tp.active_frame().plot().contour(5).legend.show=True
                tp.active_frame().plot().contour(5).legend.vertical=False
                tp.active_frame().plot().contour(5).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(5).legend.position = (87.959, 77.7249)
                tp.active_frame().plot().contour(5).legend.position = (87.959, 100)  
                tp.active_frame().plot().contour(5).legend.auto_resize=True
                
                levels6 = tp.active_frame().plot().contour(6).levels
                levels6.reset_levels([0]) 
                tp.active_frame().plot().contour(6).colormap_name='Large Rainbow modified (1)'
                tp.active_frame().plot().contour(6).legend.show=True
                tp.active_frame().plot().contour(6).legend.vertical=False
                tp.active_frame().plot().contour(6).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(6).legend.position = (95, 80)
                tp.active_frame().plot().contour(6).legend.position = (95, 100)  
                tp.active_frame().plot().contour(6).legend.auto_resize=True
                
                # contour_index = 7 の設定
                levels7 = tp.active_frame().plot().contour(7).levels
                if view_flag == 1:
                    levels7.reset_levels([35,35.25,35.5,35.75,36,36.25,36.5,36.75,37,37.25,37.5,37.75,38,38.25,38.5,38.75,39,39.25,39.5,39.75,40,40.25,40.5,40.75,41,41.25,41.5,41.75,42,42.25,42.5,42.75,43,43.25,43.5,43.75,44,44.25,44.5,44.75,45,45.25,45.5,45.75,46,46.25,46.5,46.75,47,47.25,47.5,47.75,48,48.25,48.5,48.75,49,49.25,49.5,49.75,50,50.25,50.5,50.75,51,51.25,51.5,51.75,52,52.25,52.5,52.75,53,53.25,53.5,53.75,54,54.25,54.5,54.75,55,55.25,55.5,55.75,56,56.25,56.5,56.75,57,57.25,57.5,57.75,58,58.25,58.5,58.75,59,59.25,59.5,59.75,60]) 
                elif view_flag == 2 :
                    levels7.reset_levels([55,55.5,56,56.5,57,57.5,58,58.5,59,59.5,60,60.5,61,61.5,62,62.5,63,63.5,64,64.5,65,65.5,66,66.5,67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72.5,73,73.5,74,74.5,75,75.5,76,76.5,77,77.5,78,78.5,79,79.5,80,80.5,81,81.5,82,82.5,83,83.5,84,84.5,85,85.5,86,86.5,87,87.5,88,88.5,89,89.5,90,90.5,91,91.5,92,92.5,93,93.5,94,94.5,95])
                elif view_flag == 3 :
                    levels7.reset_levels([35,35.5,36,36.5,37,37.5,38,38.5,39,39.5,40,40.5,41,41.5,42,42.5,43,43.5,44,44.5,45,45.5,46,46.5,47,47.5,48,48.5,49,49.5,50,50.5,51,51.5,52,52.5,53,53.5,54,54.5,55,55.5,56,56.5,57,57.5,58,58.5,59,59.5,60,60.5,61,61.5,62,62.5,63,63.5,64,64.5,65,65.5,66,66.5,67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72.5,73,73.5,74,74.5,75])
                elif view_flag == 4 :
                    levels7.reset_levels([65,65.25,65.5,65.75,66,66.25,66.5,66.75,67,67.25,67.5,67.75,68,68.25,68.5,68.75,69,69.25,69.5,69.75,70,70.25,70.5,70.75,71,71.25,71.5,71.75,72,72.25,72.5,72.75,73,73.25,73.5,73.75,74,74.25,74.5,74.75,75,75.25,75.5,75.75,76,76.25,76.5,76.75,77,77.25,77.5,77.75,78,78.25,78.5,78.75,79,79.25,79.5,79.75,80])
                elif view_flag == 5 :
                    levels7.reset_levels([46,46.5,47,47.5,48,48.5,49,49.5,50,50.5,51,51.5,52,52.5,53,53.5,54,54.5,55,55.5,56])
                elif view_flag == 6 :
                    levels7.reset_levels([48,48.2,48.4,48.6,48.8,49,49.2,49.4,49.6,49.8,50,50.2,50.4,50.6,50.8,51,51.2,51.4,51.6,51.8,52])
                elif view_flag == 8 :
                    levels7.reset_levels([75,75.2,75.4,75.6,75.8,76,76.2,76.4,76.6,76.8,77,77.2,77.4,77.6,77.8,78,78.2,78.4,78.6,78.8,79,79.2,79.4,79.6,79.8,80,80.2,80.4,80.6,80.8,81,81.2,81.4,81.6,81.8,82,82.2,82.4,82.6,82.8,83,83.2,83.4,83.6,83.8,84,84.2,84.4,84.6,84.8,85,85.2,85.4,85.6,85.8,86,86.2,86.4,86.6,86.8,87,87.2,87.4,87.6,87.8,88,88.2,88.4,88.6,88.8,89,89.2,89.4,89.6,89.8,90]) #zb
                tp.active_frame().plot().contour(7).colormap_name='Elevation - Above Ground Level'
                tp.active_frame().plot().contour(7).legend.show=True
                tp.active_frame().plot().contour(7).legend.vertical=False
                tp.active_frame().plot().contour(7).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(7).legend.position = (95, 100)  
                tp.active_frame().plot().contour(7).legend.auto_resize=True

                tp.active_frame().plot(PlotType.Cartesian2D).vector.u_variable_index=3
                tp.active_frame().plot(PlotType.Cartesian2D).vector.v_variable_index=4
                tp.active_frame().plot(PlotType.Cartesian2D).vector.relative_length=0.09
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.line_thickness=0.3 
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.arrowhead_style=ArrowheadStyle.Filled 
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.color=Color.Red 
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.vector_type=VectorType.TailAtPoint 
                tp.active_frame().plot(PlotType.Cartesian2D).vector.arrowhead_fraction=0.4
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.show=True
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.label.show=True
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.magnitude=4
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.position=(74.788,86.934)
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.line_thickness = 0.4
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.color=Color.Red
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.label.font.size=5

                tp.active_frame().plot().fieldmaps(0).points.points_to_plot = PointsToPlot.SurfaceNodes
                tp.active_frame().plot().fieldmaps(0).points.step = (20,2)
                tp.active_frame().plot(PlotType.Cartesian2D).show_vector = True

       
                tp.macro.execute_command("""$!AttachText 
                  AnchorPos
                      {
                      X = 19.1853
                      Y = 89.1094
                      }
                  TextShape
                      {
                      IsBold = No
                      Height = 25
                      }
                  Text = 'time=&(solutiontime)[s]'""")
            
                tp.active_frame().plot().value_blanking.active = True

                tp.active_frame().plot().value_blanking.cell_mode=ValueBlankCellMode.PrimaryValue 

                constraint = tp.active_frame().plot().value_blanking.constraint(1)
                constraint.active = True
                constraint.compare_by = ConstraintOp2Mode.UseConstant
                constraint.comparison_operator = RelOp.LessThanOrEqual                  
                constraint.comparison_value = 0
                constraint.variable = dataset.variable('dsf')

            
                tp.active_frame().plot().axes.grid_area.filled=False
                axes.preserve_scale=False

                xaxis = tp.active_frame().plot().axes.x_axis
                xaxis.show = True
                xaxis.title.show = True
                xaxis.title.text = 'x[m]'
                xaxis.title.title_mode = AxisTitleMode.UseText
                xaxis.line.show=True
                xaxis.tick_labels.font.size = 5   
                xaxis.grid_lines.show = False
                xaxis.show = True

                yaxis = tp.active_frame().plot().axes.y_axis
                yaxis.show = True
                yaxis.line.show=True
                yaxis.grid_lines.show = False
                yaxis.title.show = True
                yaxis.title.text = 'z[m]'
                yaxis.tick_labels.font.size = 5
                yaxis.show = True

                

                if uu == "00050000":
                    xmax=14+1
                elif uu == "00060000":
                    xmax=15+1
                elif uu == "00070000":
                    xmax=16+1
                elif uu == "00080000":
                    xmax=17.5+1
                elif uu == "00090000":
                    xmax=18+1
                elif uu == "00100000":
                    xmax=19.5+1
                elif uu == "00110000":
                    xmax=20.8+1
                elif uu == "00120000":
                    xmax=21.5+1
                elif uu == "00130000":
                    xmax=22+1
                elif uu == "00140000":
                    xmax=23.5+1
                elif uu == "00150000":
                    xmax=24.5+1
                elif uu == "00160000":
                    xmax=25.1+1
                elif uu == "00170000":
                    xmax=26+1
                elif uu == "00180000":
                    xmax=27.8+1
                elif uu == "00190000":
                    xmax=30+1
                elif uu == "00200000":
                    xmax=33+1

                yaxis.min =  1.3
                yaxis.max =  6.5
                xaxis.min =  xmax-7.5
                xaxis.max =  xmax
                
                
            
                xaxis.show = True
                yaxis.show = True

                #print("ai")


                tp.active_page().add_frame(position=(1.0016,0.29334),
                                            size=(9.0054,7.9307))
                tp.active_frame().plot_type=PlotType.Cartesian2D

                if shade_flag == 0 :
                    tp.active_frame().plot().show_shade=False                      
                elif shade_flag == 1 :
                    tp.active_frame().plot().show_shade=True

                tp.active_frame().plot().frame.show_border=False               
                tp.active_frame().plot().frame.transparent=True               
                tp.active_frame().plot().rgb_coloring.red_variable_index=6
                tp.active_frame().plot().rgb_coloring.green_variable_index=3
                tp.active_frame().plot().rgb_coloring.blue_variable_index=3

                tp.active_frame().plot().contour(0).variable_index=3     
                tp.active_frame().plot().contour(1).variable_index=4     
                tp.active_frame().plot().contour(2).variable_index=6     
                tp.active_frame().plot().contour(3).variable_index=7     
                tp.active_frame().plot().contour(4).variable_index=8     
                tp.active_frame().plot().contour(5).variable_index=9     
                tp.active_frame().plot().contour(6).variable_index=7    
                tp.active_frame().plot().contour(7).variable_index=7     
               
                tp.active_frame().plot().fieldmaps(0).contour.contour_type=ContourType.Overlay
                tp.active_frame().plot().fieldmaps(0).contour.flood_contour_group_index=0 #ContourIndex_Flood
                tp.active_frame().plot().fieldmaps(0).contour.line_group_index=2 #ContourIndex_Line
               
                tp.active_frame().plot().show_contour=True

             

                frame = tp.active_frame()
                axes = frame.plot().axes

                tp.active_frame().plot().fieldmaps(0).contour.line_thickness=0.25
                

                levels0 = tp.active_frame().plot().contour(0).levels
                levels0.reset_levels([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
                tp.active_frame().plot().contour(0).legend.position = (78, 98)
                tp.active_frame().plot().contour(0).colormap_name='Diverging - Brown/Green'
                tp.active_frame().plot().contour(0).legend.show=True
                tp.active_frame().plot().contour(0).legend.vertical=False
                tp.active_frame().plot().contour(0).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(0).legend.auto_resize=False
                tp.active_frame().plot().contour(0).labels.step=1

                levels1 = tp.active_frame().plot().contour(1).levels
                levels1.reset_levels([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
                tp.active_frame().plot().contour(1).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(1).legend.show=False
                tp.active_frame().plot().contour(1).legend.vertical=False
                tp.active_frame().plot().contour(1).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(1).legend.position = (98, 100)
                tp.active_frame().plot().contour(1).legend.auto_resize=True
                
                levels2 = tp.active_frame().plot().contour(2).levels
                levels2.reset_levels([1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600])
                tp.active_frame().plot().contour(2).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(2).legend.show=False
                tp.active_frame().plot().contour(2).legend.vertical=False
                tp.active_frame().plot().contour(2).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(2).legend.position = (98, 100)
                tp.active_frame().plot().contour(2).legend.auto_resize=True

                levels3 = tp.active_frame().plot().contour(3).levels
                levels3.reset_levels([0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000])
                tp.active_frame().plot().contour(3).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(3).legend.show=False
                tp.active_frame().plot().contour(3).legend.position = (98, 90)
                tp.active_frame().plot().contour(3).legend.vertical=False
                tp.active_frame().plot().contour(3).legend.box.box_type=tp.constant.TextBox.None_            
                tp.active_frame().plot().contour(3).legend.auto_resize=True

                levels4 = tp.active_frame().plot().contour(4).levels
                levels4.reset_levels([0]) 
                tp.active_frame().plot().contour(4).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(4).legend.show=True
                tp.active_frame().plot().contour(4).legend.vertical=False
                tp.active_frame().plot().contour(4).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(4).legend.position = (90, 100)
                tp.active_frame().plot().contour(4).legend.auto_resize=True

                levels5 = tp.active_frame().plot().contour(5).levels
                levels5.reset_levels([0]) 
                tp.active_frame().plot().contour(5).colormap_name='Large Rainbow modified (1)'
                tp.active_frame().plot().contour(5).legend.show=True
                tp.active_frame().plot().contour(5).legend.vertical=False
                tp.active_frame().plot().contour(5).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(5).legend.position = (87.959, 77.7249)
                tp.active_frame().plot().contour(5).legend.position = (87.959, 100)  
                tp.active_frame().plot().contour(5).legend.auto_resize=True
                
                levels6 = tp.active_frame().plot().contour(6).levels
                levels6.reset_levels([0]) 
                tp.active_frame().plot().contour(6).colormap_name='Large Rainbow modified (1)'
                tp.active_frame().plot().contour(6).legend.show=True
                tp.active_frame().plot().contour(6).legend.vertical=False
                tp.active_frame().plot().contour(6).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(6).legend.position = (95, 80)
                tp.active_frame().plot().contour(6).legend.position = (95, 100)  
                tp.active_frame().plot().contour(6).legend.auto_resize=True
                
                levels7 = tp.active_frame().plot().contour(7).levels
                if view_flag == 1:
                    levels7.reset_levels([35,35.25,35.5,35.75,36,36.25,36.5,36.75,37,37.25,37.5,37.75,38,38.25,38.5,38.75,39,39.25,39.5,39.75,40,40.25,40.5,40.75,41,41.25,41.5,41.75,42,42.25,42.5,42.75,43,43.25,43.5,43.75,44,44.25,44.5,44.75,45,45.25,45.5,45.75,46,46.25,46.5,46.75,47,47.25,47.5,47.75,48,48.25,48.5,48.75,49,49.25,49.5,49.75,50,50.25,50.5,50.75,51,51.25,51.5,51.75,52,52.25,52.5,52.75,53,53.25,53.5,53.75,54,54.25,54.5,54.75,55,55.25,55.5,55.75,56,56.25,56.5,56.75,57,57.25,57.5,57.75,58,58.25,58.5,58.75,59,59.25,59.5,59.75,60]) 
                elif view_flag == 2 :
                    levels7.reset_levels([55,55.5,56,56.5,57,57.5,58,58.5,59,59.5,60,60.5,61,61.5,62,62.5,63,63.5,64,64.5,65,65.5,66,66.5,67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72.5,73,73.5,74,74.5,75,75.5,76,76.5,77,77.5,78,78.5,79,79.5,80,80.5,81,81.5,82,82.5,83,83.5,84,84.5,85,85.5,86,86.5,87,87.5,88,88.5,89,89.5,90,90.5,91,91.5,92,92.5,93,93.5,94,94.5,95])
                elif view_flag == 3 :
                    levels7.reset_levels([35,35.5,36,36.5,37,37.5,38,38.5,39,39.5,40,40.5,41,41.5,42,42.5,43,43.5,44,44.5,45,45.5,46,46.5,47,47.5,48,48.5,49,49.5,50,50.5,51,51.5,52,52.5,53,53.5,54,54.5,55,55.5,56,56.5,57,57.5,58,58.5,59,59.5,60,60.5,61,61.5,62,62.5,63,63.5,64,64.5,65,65.5,66,66.5,67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72.5,73,73.5,74,74.5,75])
                elif view_flag == 4 :
                    levels7.reset_levels([65,65.25,65.5,65.75,66,66.25,66.5,66.75,67,67.25,67.5,67.75,68,68.25,68.5,68.75,69,69.25,69.5,69.75,70,70.25,70.5,70.75,71,71.25,71.5,71.75,72,72.25,72.5,72.75,73,73.25,73.5,73.75,74,74.25,74.5,74.75,75,75.25,75.5,75.75,76,76.25,76.5,76.75,77,77.25,77.5,77.75,78,78.25,78.5,78.75,79,79.25,79.5,79.75,80])
                elif view_flag == 5 :
                    levels7.reset_levels([46,46.5,47,47.5,48,48.5,49,49.5,50,50.5,51,51.5,52,52.5,53,53.5,54,54.5,55,55.5,56])
                elif view_flag == 6 :
                    levels7.reset_levels([48,48.2,48.4,48.6,48.8,49,49.2,49.4,49.6,49.8,50,50.2,50.4,50.6,50.8,51,51.2,51.4,51.6,51.8,52])
                elif view_flag == 8 :
                    levels7.reset_levels([75,75.2,75.4,75.6,75.8,76,76.2,76.4,76.6,76.8,77,77.2,77.4,77.6,77.8,78,78.2,78.4,78.6,78.8,79,79.2,79.4,79.6,79.8,80,80.2,80.4,80.6,80.8,81,81.2,81.4,81.6,81.8,82,82.2,82.4,82.6,82.8,83,83.2,83.4,83.6,83.8,84,84.2,84.4,84.6,84.8,85,85.2,85.4,85.6,85.8,86,86.2,86.4,86.6,86.8,87,87.2,87.4,87.6,87.8,88,88.2,88.4,88.6,88.8,89,89.2,89.4,89.6,89.8,90]) #zb
                tp.active_frame().plot().contour(7).colormap_name='Elevation - Above Ground Level'
                tp.active_frame().plot().contour(7).legend.show=True
                tp.active_frame().plot().contour(7).legend.vertical=False
                tp.active_frame().plot().contour(7).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(7).legend.position = (95, 100)  # 京王線v02
                tp.active_frame().plot().contour(7).legend.auto_resize=True

                tp.active_frame().plot(PlotType.Cartesian2D).vector.u_variable_index=3
                tp.active_frame().plot(PlotType.Cartesian2D).vector.v_variable_index=4
                tp.active_frame().plot(PlotType.Cartesian2D).vector.relative_length=0.35
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.line_thickness=0.3 
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.arrowhead_style=ArrowheadStyle.Filled 
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.color=Color.Blue #White #Black
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.vector_type=VectorType.TailAtPoint 
                tp.active_frame().plot(PlotType.Cartesian2D).vector.arrowhead_fraction=0.4
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.show=True
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.label.show=True
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.magnitude=1
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.position=(74.788,77.617)
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.line_thickness = 0.4
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.color=Color.Blue
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.label.font.size=5

                tp.active_frame().plot().fieldmaps(0).points.points_to_plot = PointsToPlot.SurfaceNodes
                tp.active_frame().plot().fieldmaps(0).points.step = (20,2)
                
                tp.active_frame().plot(PlotType.Cartesian2D).show_vector = True

                tp.active_frame().plot().value_blanking.active = True

                tp.active_frame().plot().value_blanking.cell_mode=ValueBlankCellMode.PrimaryValue 

                constraint = tp.active_frame().plot().value_blanking.constraint(1)
                constraint.active = True
                constraint.compare_by = ConstraintOp2Mode.UseConstant
                constraint.comparison_operator = RelOp.LessThanOrEqual                 
                constraint.comparison_value = 0
                constraint.variable = dataset.variable('dzb')


                if uu == "00050000":
                    xmax=14+1
                elif uu == "00060000":
                    xmax=15+1
                elif uu == "00070000":
                    xmax=16+1
                elif uu == "00080000":
                    xmax=17.5+1
                elif uu == "00090000":
                    xmax=18+1
                elif uu == "00100000":
                    xmax=19.5+1
                elif uu == "00110000":
                    xmax=20.8+1
                elif uu == "00120000":
                    xmax=21.5+1
                elif uu == "00130000":
                    xmax=22+1
                elif uu == "00140000":
                    xmax=23.5+1
                elif uu == "00150000":
                    xmax=24.5+1
                elif uu == "00160000":
                    xmax=25.1+1
                elif uu == "00170000":
                    xmax=26+1
                elif uu == "00180000":
                    xmax=27.8+1
                elif uu == "00190000":
                    xmax=30+1
                elif uu == "00200000":
                    xmax=33+1

                xaxis = tp.active_frame().plot().axes.x_axis
                xaxis.show = False
                yaxis = tp.active_frame().plot().axes.y_axis
                yaxis.show = False
                yaxis.min =  1.3
                yaxis.max =  6.5
                xaxis.min =  xmax-7.5
                xaxis.max =  xmax

                tp.macro.execute_command('''$!FrameControl ActivateByNumber
                                        Frame = 1''')
                tp.active_frame().plot().linking_between_frames.link_frame_size_and_position=True
                tp.active_frame().plot().linking_between_frames.link_x_axis_range=True
                tp.active_frame().plot().linking_between_frames.link_y_axis_range=True
                tp.active_frame().plot().linking_between_frames.link_axis_position=True

                tp.macro.execute_command('''$!PropagateLinking 
                                            LinkType = BetweenFrames
                                            FrameCollection = All''')

        
                tp.active_page().add_frame(position=(1.0016,0.29334),
                                            size=(9.0054,7.9307))
                tp.active_frame().plot_type=PlotType.Cartesian2D

                if shade_flag == 0 :
                    tp.active_frame().plot().show_shade=False                     
                elif shade_flag == 1 :
                    tp.active_frame().plot().show_shade=True

                tp.active_frame().plot().frame.show_border=False              
                tp.active_frame().plot().frame.transparent=True                
                tp.active_frame().plot().rgb_coloring.red_variable_index=6
                tp.active_frame().plot().rgb_coloring.green_variable_index=3
                tp.active_frame().plot().rgb_coloring.blue_variable_index=3

                tp.active_frame().plot().contour(0).variable_index=3     
                tp.active_frame().plot().contour(1).variable_index=4     
                tp.active_frame().plot().contour(2).variable_index=6     
                tp.active_frame().plot().contour(3).variable_index=7     
                tp.active_frame().plot().contour(4).variable_index=8     
                tp.active_frame().plot().contour(5).variable_index=9     
                tp.active_frame().plot().contour(6).variable_index=7     
                tp.active_frame().plot().contour(7).variable_index=7     
               
                tp.active_frame().plot().fieldmaps(0).contour.contour_type=ContourType.Lines
                tp.active_frame().plot().fieldmaps(0).contour.line_group_index=4
                tp.active_frame().plot().fieldmaps(0).contour.line_color=Color.White
               
                tp.active_frame().plot().show_contour=True

                frame = tp.active_frame()
                axes = frame.plot().axes

                tp.active_frame().plot().fieldmaps(0).contour.line_thickness=0.4
                
                levels0 = tp.active_frame().plot().contour(0).levels
                levels0.reset_levels([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
                tp.active_frame().plot().contour(0).legend.position = (98, 98)
                tp.active_frame().plot().contour(0).colormap_name='Diverging - Brown/Green'
                tp.active_frame().plot().contour(0).legend.show=False
                tp.active_frame().plot().contour(0).legend.vertical=False
                tp.active_frame().plot().contour(0).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(0).legend.auto_resize=False
                tp.active_frame().plot().contour(0).labels.step=1

                levels1 = tp.active_frame().plot().contour(1).levels
                levels1.reset_levels([0,0.5,1,1.5,2,2.5,3,3.5,4,4.5,5])
                tp.active_frame().plot().contour(1).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(1).legend.show=False
                tp.active_frame().plot().contour(1).legend.vertical=False
                tp.active_frame().plot().contour(1).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(1).legend.position = (98, 100)
                tp.active_frame().plot().contour(1).legend.auto_resize=True
                

                levels2 = tp.active_frame().plot().contour(2).levels
                levels2.reset_levels([1100,1200,1300,1400,1500,1600,1700,1800,1900,2000,2100,2200,2300,2400,2500,2600])
                tp.active_frame().plot().contour(2).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(2).legend.show=False
                tp.active_frame().plot().contour(2).legend.vertical=False
                tp.active_frame().plot().contour(2).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(2).legend.position = (98, 100)
                tp.active_frame().plot().contour(2).legend.auto_resize=True

                levels3 = tp.active_frame().plot().contour(3).levels
                levels3.reset_levels([0,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,11000,12000,13000,14000,15000,16000,17000,18000,19000,20000])
                tp.active_frame().plot().contour(3).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(3).legend.show=False
                tp.active_frame().plot().contour(3).legend.position = (98, 90)
                tp.active_frame().plot().contour(3).legend.vertical=False
                tp.active_frame().plot().contour(3).legend.box.box_type=tp.constant.TextBox.None_            
                tp.active_frame().plot().contour(3).legend.auto_resize=True

                levels4 = tp.active_frame().plot().contour(4).levels
                levels4.reset_levels([0]) 
                tp.active_frame().plot().contour(4).colormap_name='Large Rainbow modified (2)'
                tp.active_frame().plot().contour(4).legend.show=False
                tp.active_frame().plot().contour(4).legend.vertical=False
                tp.active_frame().plot().contour(4).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(4).legend.position = (90, 100)
                tp.active_frame().plot().contour(4).legend.auto_resize=True

                levels5 = tp.active_frame().plot().contour(5).levels
                levels5.reset_levels([0]) 
                tp.active_frame().plot().contour(5).colormap_name='Large Rainbow modified (1)'
                tp.active_frame().plot().contour(5).legend.show=True
                tp.active_frame().plot().contour(5).legend.vertical=False
                tp.active_frame().plot().contour(5).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(5).legend.position = (87.959, 77.7249)
                tp.active_frame().plot().contour(5).legend.position = (87.959, 100)  
                tp.active_frame().plot().contour(5).legend.auto_resize=True
                
                levels6 = tp.active_frame().plot().contour(6).levels
                levels6.reset_levels([0]) 
                tp.active_frame().plot().contour(6).colormap_name='Large Rainbow modified (1)'
                tp.active_frame().plot().contour(6).legend.show=True
                tp.active_frame().plot().contour(6).legend.vertical=False
                tp.active_frame().plot().contour(6).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(6).legend.position = (95, 80)
                tp.active_frame().plot().contour(6).legend.position = (95, 100)  
                tp.active_frame().plot().contour(6).legend.auto_resize=True
                
                levels7 = tp.active_frame().plot().contour(7).levels
                if view_flag == 1:
                    levels7.reset_levels([35,35.25,35.5,35.75,36,36.25,36.5,36.75,37,37.25,37.5,37.75,38,38.25,38.5,38.75,39,39.25,39.5,39.75,40,40.25,40.5,40.75,41,41.25,41.5,41.75,42,42.25,42.5,42.75,43,43.25,43.5,43.75,44,44.25,44.5,44.75,45,45.25,45.5,45.75,46,46.25,46.5,46.75,47,47.25,47.5,47.75,48,48.25,48.5,48.75,49,49.25,49.5,49.75,50,50.25,50.5,50.75,51,51.25,51.5,51.75,52,52.25,52.5,52.75,53,53.25,53.5,53.75,54,54.25,54.5,54.75,55,55.25,55.5,55.75,56,56.25,56.5,56.75,57,57.25,57.5,57.75,58,58.25,58.5,58.75,59,59.25,59.5,59.75,60]) 
                elif view_flag == 2 :
                    levels7.reset_levels([55,55.5,56,56.5,57,57.5,58,58.5,59,59.5,60,60.5,61,61.5,62,62.5,63,63.5,64,64.5,65,65.5,66,66.5,67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72.5,73,73.5,74,74.5,75,75.5,76,76.5,77,77.5,78,78.5,79,79.5,80,80.5,81,81.5,82,82.5,83,83.5,84,84.5,85,85.5,86,86.5,87,87.5,88,88.5,89,89.5,90,90.5,91,91.5,92,92.5,93,93.5,94,94.5,95])
                elif view_flag == 3 :
                    levels7.reset_levels([35,35.5,36,36.5,37,37.5,38,38.5,39,39.5,40,40.5,41,41.5,42,42.5,43,43.5,44,44.5,45,45.5,46,46.5,47,47.5,48,48.5,49,49.5,50,50.5,51,51.5,52,52.5,53,53.5,54,54.5,55,55.5,56,56.5,57,57.5,58,58.5,59,59.5,60,60.5,61,61.5,62,62.5,63,63.5,64,64.5,65,65.5,66,66.5,67,67.5,68,68.5,69,69.5,70,70.5,71,71.5,72,72.5,73,73.5,74,74.5,75])
                elif view_flag == 4 :
                    levels7.reset_levels([65,65.25,65.5,65.75,66,66.25,66.5,66.75,67,67.25,67.5,67.75,68,68.25,68.5,68.75,69,69.25,69.5,69.75,70,70.25,70.5,70.75,71,71.25,71.5,71.75,72,72.25,72.5,72.75,73,73.25,73.5,73.75,74,74.25,74.5,74.75,75,75.25,75.5,75.75,76,76.25,76.5,76.75,77,77.25,77.5,77.75,78,78.25,78.5,78.75,79,79.25,79.5,79.75,80])
                elif view_flag == 5 :
                    levels7.reset_levels([46,46.5,47,47.5,48,48.5,49,49.5,50,50.5,51,51.5,52,52.5,53,53.5,54,54.5,55,55.5,56])
                elif view_flag == 6 :
                    levels7.reset_levels([48,48.2,48.4,48.6,48.8,49,49.2,49.4,49.6,49.8,50,50.2,50.4,50.6,50.8,51,51.2,51.4,51.6,51.8,52])
                elif view_flag == 8 :
                    levels7.reset_levels([75,75.2,75.4,75.6,75.8,76,76.2,76.4,76.6,76.8,77,77.2,77.4,77.6,77.8,78,78.2,78.4,78.6,78.8,79,79.2,79.4,79.6,79.8,80,80.2,80.4,80.6,80.8,81,81.2,81.4,81.6,81.8,82,82.2,82.4,82.6,82.8,83,83.2,83.4,83.6,83.8,84,84.2,84.4,84.6,84.8,85,85.2,85.4,85.6,85.8,86,86.2,86.4,86.6,86.8,87,87.2,87.4,87.6,87.8,88,88.2,88.4,88.6,88.8,89,89.2,89.4,89.6,89.8,90]) 
                tp.active_frame().plot().contour(7).colormap_name='Elevation - Above Ground Level'
                tp.active_frame().plot().contour(7).legend.show=True
                tp.active_frame().plot().contour(7).legend.vertical=False
                tp.active_frame().plot().contour(7).legend.box.box_type=tp.constant.TextBox.None_
                tp.active_frame().plot().contour(7).legend.position = (95, 100)  # 京王線v02
                tp.active_frame().plot().contour(7).legend.auto_resize=True

             
                tp.active_frame().plot(PlotType.Cartesian2D).vector.u_variable_index=3
                tp.active_frame().plot(PlotType.Cartesian2D).vector.v_variable_index=4
                tp.active_frame().plot(PlotType.Cartesian2D).vector.relative_length=0.09
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.line_thickness=0.3 
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.arrowhead_style=ArrowheadStyle.Filled 
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.color=Color.Red #White #Black
                tp.active_frame().plot(PlotType.Cartesian2D).fieldmaps(0).vector.vector_type=VectorType.TailAtPoint 
                tp.active_frame().plot(PlotType.Cartesian2D).vector.arrowhead_fraction=0.4
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.show=True
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.label.show=True
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.magnitude=5
                tp.active_frame().plot(PlotType.Cartesian2D).vector.reference_vector.position=(74.788,86.934)

                tp.active_frame().plot().fieldmaps(0).points.points_to_plot = PointsToPlot.SurfaceNodes
                tp.active_frame().plot().fieldmaps(0).points.step = (20,2)
                
                tp.active_frame().plot(PlotType.Cartesian2D).show_vector = False

                tp.macro.execute_command("""$!AttachText 
                    AnchorPos
                        {
                        X = 42.7296
                        Y = 81.5818
                        }
                    TextShape
                        {
                        IsBold = No
                        Height = 20
                        }
                    Color = Black
                    Text = 'volocity vectors in the fluidized layer'""")
                
                tp.macro.execute_command("""$!AttachText 
                    AnchorPos
                        {
                        X = 30.8935
                        Y = 72.481
                        }
                    TextShape
                        {
                        IsBold = No
                        Height = 20
                        }
                    Color = Black
                    Text = 'volocity vectors in the stationary sedimentary layer'""")
                
                tp.macro.execute_command("""$!AttachText 
                    AnchorPos
                        {
                        X = 77.5169
                        Y = 82.1235
                        }
                    TextShape
                        {
                        IsBold = No
                        Height = 20
                        }
                    Color = Black
                    Text = '[m/s]'""")
                
                tp.macro.execute_command("""$!AttachText 
                    AnchorPos
                        {
                        X = 77.5169
                        Y = 72.481
                        }
                    TextShape
                        {
                        IsBold = No
                        Height = 20
                        }
                    Color = Black
                    Text = '[m/s]'""")
                
                tp.macro.execute_command("""$!AttachText 
                    AnchorPos
                        {
                        X = 71.5689
                        Y = 67.2806
                        }
                    TextShape
                        {
                        IsBold = No
                        Height = 20
                        }
                    Color = Black
                    Text = 'Front position'""")
                

                line0 = frame.add_polyline([[78,66.1075], [78,61.9]], coord_sys=CoordSys.Frame)
                line0.arrowhead.attachment = ArrowheadAttachment.AtEnd
                line0.line_thickness = 0.1
                line0.arrowhead.style = ArrowheadStyle.Filled
                line0.arrowhead.angle = 14
                line0.arrowhead.size = 2


                tp.active_frame().plot().value_blanking.active = False

                tp.active_frame().plot().value_blanking.cell_mode=ValueBlankCellMode.PrimaryValue 


                if uu == "00050000":
                    xmax=14+1
                elif uu == "00060000":
                    xmax=15+1
                elif uu == "00070000":
                    xmax=16+1
                elif uu == "00080000":
                    xmax=17.5+1
                elif uu == "00090000":
                    xmax=18+1
                elif uu == "00100000":
                    xmax=19.5+1
                elif uu == "00110000":
                    xmax=20.8+1
                elif uu == "00120000":
                    xmax=21.5+1
                elif uu == "00130000":
                    xmax=22+1
                elif uu == "00140000":
                    xmax=23.5+1
                elif uu == "00150000":
                    xmax=24.5+1
                elif uu == "00160000":
                    xmax=25.1+1
                elif uu == "00170000":
                    xmax=26+1
                elif uu == "00180000":
                    xmax=27.8+1
                elif uu == "00190000":
                    xmax=30+1
                elif uu == "00200000":
                    xmax=33+1

                xaxis = tp.active_frame().plot().axes.x_axis
                yaxis = tp.active_frame().plot().axes.y_axis
                yaxis.min =  1.3
                yaxis.max =  6.5
                xaxis.min =  xmax-7.5
                xaxis.max =  xmax

                tp.active_frame().plot().axes.grid_area.filled=False
                axes.preserve_scale=False

                xaxis = tp.active_frame().plot().axes.x_axis
                xaxis.show = True
                xaxis.title.show = True
                xaxis.title.text = 'x[m]'
                xaxis.title.title_mode = AxisTitleMode.UseText
                xaxis.line.show=True
                xaxis.tick_labels.font.size = 4    
                xaxis.grid_lines.show = False
                xaxis.show = True

                yaxis = tp.active_frame().plot().axes.y_axis
                yaxis.show = True
                yaxis.line.show=True
                yaxis.grid_lines.show = False
                yaxis.title.show = True
                yaxis.title.text = 'z[m]'
                yaxis.title.title_mode = AxisTitleMode.UseText
                yaxis.tick_labels.font.size = 4
                yaxis.show = True

                tp.macro.execute_command('''$!FrameControl ActivateByNumber
                                        Frame = 1''')
                tp.active_frame().plot().linking_between_frames.link_frame_size_and_position=True
                tp.active_frame().plot().linking_between_frames.link_x_axis_range=True
                tp.active_frame().plot().linking_between_frames.link_y_axis_range=True
                tp.active_frame().plot().linking_between_frames.link_axis_position=True

                tp.macro.execute_command('''$!PropagateLinking 
                                            LinkType = BetweenFrames
                                            FrameCollection = All''')

                if uu == "00050000":
                    xmax=14+1
                elif uu == "00060000":
                    xmax=15+1
                elif uu == "00070000":
                    xmax=16+1
                elif uu == "00080000":
                    xmax=17.5+1
                elif uu == "00090000":
                    xmax=18+1
                elif uu == "00100000":
                    xmax=19.5+1
                elif uu == "00110000":
                    xmax=20.8+1
                elif uu == "00120000":
                    xmax=21.5+1
                elif uu == "00130000":
                    xmax=22+1
                elif uu == "00140000":
                    xmax=23.5+1
                elif uu == "00150000":
                    xmax=24.5+1
                elif uu == "00160000":
                    xmax=25.1+1
                elif uu == "00170000":
                    xmax=26+1
                elif uu == "00180000":
                    xmax=27.8+1
                elif uu == "00190000":
                    xmax=30+1
                elif uu == "00200000":
                    xmax=33+1

                xaxis = tp.active_frame().plot().axes.x_axis
                xaxis.show = False
                yaxis = tp.active_frame().plot().axes.y_axis
                yaxis.show = False
                yaxis.min =  1.3
                yaxis.max =  6.5
                xaxis.min =  xmax-7.5
                xaxis.max =  xmax
                

                # fname:ファイル名パスなし
                fname = os.path.basename(file_name)

                # bname:ファイル名拡張子なし, ext:拡張子
                bname, ext =  os.path.splitext( fname )

                # パス ＋ ファイル名拡張子なし + 拡張子
                fpath=output_folder_png + '/' + bname + '.png'

                tp.export.save_png(fpath, 2400, supersample=3)
                print(fpath)
