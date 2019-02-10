import maya.cmds as cmds
import functools
from boids import *
import os
import sys

def createUI( pWindowTitle, pApplyCallback ):
    
    windowID = 'myWindowID'
    
    if cmds.window( windowID, exists=True ):
        cmds.deleteUI( windowID )
        
    cmds.window( windowID, title=pWindowTitle, sizeable=False, resizeToFitChildren=True, width=500 )

    cmds.columnLayout(adj = True)

    #logopath = os.path.dirname(os.path.abspath(__file__))+"/icons/"

    cmds.text( label='Boids' )
    cmds.separator( h=10, style='none' )     

    numberOfShapes = ''
    shapesNames = []
    result = cmds.promptDialog(
        title='Boids Shapes',
        message='Enter number of shapes in Maya:\nZero will make boids from default cubes',
        button=['OK', 'Cancel'],
        defaultButton='OK',
        cancelButton='Cancel',
        dismissString='Cancel')

    if result == 'OK':
        numberOfShapes = cmds.promptDialog(query=True, text=True)
    
    try: 
        ns = int(numberOfShapes)
        if(ns > 0):
            for index in range(ns):
                shapesNames.append( cmds.textFieldGrp( label='Boid shape', text='pCubeShape' + str(index+1)) )
    except ValueError:
        print("error on converting ")
        
    numberOfBoids = cmds.intSliderGrp( label = "Number of boids:", min=0, max=500, field=True, value=77)#, changeCommand=updateLogo)
    boidSize = cmds.floatSliderGrp( label = "Size of boids:", min=0, max=10, field=True, value=1, step=0.001)
    maxSpeed = cmds.floatSliderGrp( label = "Speed limit:", min=0, max=100, field=True, value=10, step=0.001)
    checkBoxes = cmds.checkBoxGrp( numberOfCheckBoxes=3, label='', labelArray3=['Show targets', 'Use goals', 'Random start velocity'], valueArray3=[True, False, False] )
    
    cmds.separator( h=10, style='none' )

    cmds.text( label='If goal is checked, there must be objects named "goal1, goal2, etc"', enable=False, font="obliqueLabelFont" )

    cmds.separator( h=20, style='in' )
    cmds.text( label='Animation' )
    cmds.separator( h=10, style='none' )

    numberOfFrames = cmds.intSliderGrp( label = "Number of frames:", min=1, max=10000, field=True, value=1500)

    cmds.separator( h=20, style='in' )
    cmds.text( label='Rules' )
    cmds.separator( h=10, style='none' )

    cohesionRadius = cmds.floatSliderGrp( label = "Cohesion radius:", min=0, max=100, field=True, value=20, step=0.001)
    cohesionWeight = cmds.floatSliderGrp( label = "Cohesion weight:", min=0, max=10, field=True, value=0.75, step=0.001)
    cmds.separator( h=5, style='none' )

    separationRadius = cmds.floatSliderGrp( label = "Separation radius:", min=0, max=100, field=True, value=10, step=0.001)
    separationWeight = cmds.floatSliderGrp( label = "Separation weight:", min=0, max=10, field=True, value=0.55, step=0.001)
    cmds.separator( h=5, style='none' )

    alignmentRadius = cmds.floatSliderGrp( label = "Alignment radius:", min=0, max=100, field=True, value=6, step=0.001)
    alignmentWeight = cmds.floatSliderGrp( label = "Alignment weight:", min=0, max=10, field=True, value=0.02, step=0.001)


    cmds.separator( h=15, style='in' )

    cmds.rowColumnLayout( numberOfColumns=2, columnWidth=[ (1,250), (2,250) ] )
    
    cmds.button( label='Run', command=functools.partial( pApplyCallback,
                                                  numberOfBoids,
                                                  boidSize,
                                                  numberOfFrames,
                                                  maxSpeed,
                                                  separationWeight,
                                                  separationRadius,
                                                  cohesionWeight,
                                                  cohesionRadius,
                                                  alignmentWeight,
                                                  alignmentRadius,
                                                  checkBoxes ) )
    
    def cancelCallback( *pArgs ):
        if cmds.window( windowID, exists=True ):
            cmds.deleteUI( windowID )
    
    cmds.button( label='Cancel', command=cancelCallback )
    
    #cmds.columnLayout(adj = True, width = 500)

    #cmds.separator( h=15, style='in' )

    #cmds.image("logo", w=500, h=150, image=logopath+"logo2.jpg")

    cmds.showWindow()
 
def applyCallback( pNumberOfBoidsField, pBoidSize, pNFrames, pMaxSpeed, pSeparationWeight, pSeparationRadius, pCohesionWeight, pCohesionRadius, pAlignmentWeight, pAlignmentRadius, pCheckBoxes, *pArgs ):
 
    cBox1 = cmds.checkBoxGrp(pCheckBoxes, query=True, value1=True)
    cBox2 = cmds.checkBoxGrp(pCheckBoxes, query=True, value2=True)
    cBox3 = cmds.checkBoxGrp(pCheckBoxes, query=True, value3=True)    

    nBoids = cmds.intSliderGrp( pNumberOfBoidsField, query=True, value=True )
    bScale = cmds.floatSliderGrp( pBoidSize, query=True, value=True )

    nFrames = cmds.intSliderGrp( pNFrames, query=True, value=True )

    mSpeed = cmds.floatSliderGrp( pMaxSpeed, query=True, value=True )

    cWeight = cmds.floatSliderGrp( pCohesionWeight, query=True, value=True )
    cRadius = cmds.floatSliderGrp( pCohesionRadius, query=True, value=True )

    sWeight = cmds.floatSliderGrp( pSeparationWeight, query=True, value=True )
    sRadius = cmds.floatSliderGrp( pSeparationRadius, query=True, value=True )

    aWeight = cmds.floatSliderGrp( pAlignmentWeight, query=True, value=True )
    aRadius= cmds.floatSliderGrp( pAlignmentRadius, query=True, value=True )

    main(nBoids, bScale, nFrames, mSpeed, cWeight, cRadius, sWeight, sRadius, aWeight, aRadius, cBox1, cBox2, cBox3)





