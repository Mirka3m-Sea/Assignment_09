#------------------------------------------#
# Title: CD_Inventory.py
# Desc: The CD Inventory App main Module
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Extended functionality to add tracks
# Miroslava, 2022-Mar-26, Added functions to add tracks
# Miroslava, 2022-Mar-27, corrected errors in the way variables values were set within loops.
#                           i.e. confussion on whe strChoice should be compared with = or ==
#------------------------------------------#
"""
Main script, this is the scritp that runs the rest of the modules.

For this assignment, I added the submenu to handle individually tracks within a CD.

"""


import ProcessingClasses as PC
import IOClasses as IO

lstFileNames = ['AlbumInventory.txt', 'TrackInventory.txt']
lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)

while True:
    IO.ScreenIO.print_menu()
    strChoice = IO.ScreenIO.menu_choice()
    """"
    
    """
    if strChoice == 'x':
        break
    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled:\t')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            lstOfCDObjects = IO.FileIO.load_inventory(lstFileNames)
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'a':
        tplCdInfo = IO.ScreenIO.get_CD_info()
        PC.DataProcessor.add_CD(tplCdInfo, lstOfCDObjects)
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'd':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        continue  # start loop back at top.
    elif strChoice == 'c':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        cd_idx = int(input('Select the CD / Album index:')) ### I made this int to try to match it
        cd = PC.DataProcessor.select_cd(lstOfCDObjects, cd_idx)


        # TO DO add code to handle tracks on an individual CD
        while True:
            """" the submenu options are: 
               [a] Add track [d] Display cd / Album details
               [r] Remove track  [x] exit to Main Menu
               
               arguments:
                   
                   strChoice (integer): Menu choice 
                   track_id (integer): track index, that denotes location to be erased.
                   cd (list of objects) : contains a list of objects
                   cd_idx (integer) : integer picked by the user to select a track
               """
            IO.ScreenIO.print_CD_menu()
            strChoice = IO.ScreenIO.menu_CD_choice() #@Laura: This was a mistake that took me long to fix, Ihad a double ==
            if strChoice == 'x':
                break
            elif strChoice =='a':
            #Checking IOClasses, function get_track_info()
                track_info= IO.ScreenIO.get_track_info()
                PC.DataProcessor.add_track(track_info, cd)
            elif strChoice =='d':
                IO.ScreenIO.show_tracks(cd)
            elif strChoice =='r':
                #1 Show the tracks
                IO.ScreenIO.show_tracks(cd)
                flag=1
                while flag:
                    track_id= input('Select the track id to be removed:\t')
                    try:
                        track_id= int(track_id)
                        flag=0
                    except:
                        print('Incorrect Track Id, it must be an integer number.\n')
                cd.rmv_track(track_id)
            else:
                print('\nThat is not a valid option, please select from the menu\n')
                continue

            
    elif strChoice == 's':
        IO.ScreenIO.show_inventory(lstOfCDObjects)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            IO.FileIO.save_inventory(lstFileNames, lstOfCDObjects)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.
    else:
        print('General Error')