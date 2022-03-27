#------------------------------------------#
# Title: Data Classes
# Desc: A Module for Data Classes
# Change Log: (Who, When, What)
# DBiesinger, 2030-Jan-01, Created File
# DBiesinger, 2030-Jan-02, Modified to add Track class, added methods to CD class to handle tracks
# MMeza, 2022-Mar-26 modiffied the starter adding Track Class, methods, and CD class.
# Miroslava, 2022-Mar-27, finished updating and correcting minor errors. Added notes and updated doc-string
#------------------------------------------#

if __name__ == '__main__':
    raise Exception('This file is not meant to run by itself')

class Track():
    """Stores Data about a single Track:

    properties:
        position: (int) with Track position on CD / Album
        title: (str) with Track title
        length: (str) with length / playtime of Track
    methods:
        get_record() -> (str)

    Assignment09: Added the class Track.
    
    # I made a mistake by not using the proper __init__ constructor and had an error that said
    Track() cannot take values. It took me  some time to figure out the typo and to fix it.
    """
    # TO-DO add Track class code
    # -- Constructor -- #
    def __init__(self, pos, ttl, lgth): #A typo in this line generated my first roadblock.
        #--- Attributes ---#
        try:
            self.__position = int(pos)
            self.__title = str(ttl)
            self.__length =str(lgth)
        except Exception as e:
            raise Exception('Initial values are incorrect, please review the format\n' + str(e))
    
     # -- Properties -- #
    # Track position
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self,value):
        try:
            self.__position= int(value)
        except Exception as e:
            raise Exception('Position needs to be integer\n' + str(e))
    
    #Track Title
    @property
    def title(self):
        return self.__title
    
    @title.setter
    def title(self, value):
        try:
            self.__title = str(value)
        except Exception:
            raise Exception('Title needs to be string')
    
    #Track length
    @property
    def length(self):
        return self.__length
    
    @length.setter
    def length(self,value):
        try:
            self.__length = str(value)
        except Exception:
            raise Exception('Length needs to be a string')
    
    
    # -- Methods -- #
    # TO-DO Add Track class methods
    def __str__(self):
        """Returns Track details as formatted string
        Added the return line"""
        return '{:>2}. {} ({})'.format(self.position, self.title, self.length)

    def get_record(self) -> str:
        """Returns: Track record formatted for saving to file"""
        return '{},{},{}\n'.format(self.position, self.title, self.length)


class CD:
    """Stores data about a CD / Album:

    properties:
        cd_id: (int) with CD  / Album ID
        cd_title: (string) with the title of the CD / Album
        cd_artist: (string) with the artist of the CD / Album
        cd_tracks: (list) with track objects of the CD / Album #added to the starter document by Mirka
    methods:
        get_record() -> (str)
        add_track(track) -> None
        rmv_track(int) -> None
        get_tracks() -> (str)
        get_long_record() -> (str)

        #Assignment 09, added cd_tracks to the original starter script
        
    """
    # TO-DO Modify CD class as required
    # -- Constructor -- #
    def __init__(self, cd_id: int, cd_title: str, cd_artist: str) -> None:
#    def __init__(self, cd_id: int, cd_title: str, cd_artist: str, cd_tracks: list) -> None:
        """Set ID, Title, Artist of a new CD Object
       """
        #    -- Attributes  -- #
        try:
            self.__cd_id = int(cd_id)
            self.__cd_title = str(cd_title)
            self.__cd_artist = str(cd_artist)
            self.__tracks = [] #Added Assg. 09
        except Exception as e:
            raise Exception('Error setting initial values:\n' + str(e))

    # -- Properties -- #
    # CD ID
    @property
    def cd_id(self):
        return self.__cd_id

    @cd_id.setter
    def cd_id(self, value):
        try:
            self.__cd_id = int(value)
        except Exception:
            raise Exception('ID needs to be Integer')

    # CD title
    @property
    def cd_title(self):
        return self.__cd_title

    @cd_title.setter
    def cd_title(self, value):
        try:
            self.__cd_title = str(value)
        except Exception:
            raise Exception('Title needs to be String!')

    # CD artist
    @property
    def cd_artist(self):
        return self.__cd_artist

    @cd_artist.setter
    def cd_artist(self, value):
        try:
            self.__cd_artist = str(value)
        except Exception:
            raise Exception('Artist needs to be String!')

    # CD tracks
    @property
    def cd_tracks(self):
        return self.__cd_tracks #Note to self:This is the path needed for adding, erasing, or sorting.

# I tried to create a cd_tracks.setter, but I could not make it work without erros, see below my failed attempt.    
    #@cd_tracks.setter
    #    def cd_tracks(self, value):
    #        try:
    #            self.__cd_tracks == list(value)
    #        except Exception:
    #            raise Exception('Track needs to be a list')

    # -- Methods -- #
    def __str__(self):
        """Returns: CD details as formatted string"""
        return '{:>2}\t{} (by: {})'.format(self.cd_id, self.cd_title, self.cd_artist) #TO DO added one more bracket for the Cd. Tracks. display

    def get_record(self):
        """Returns: CD record formatted for saving to file"""
        return '{},{},{}\n'.format(self.cd_id, self.cd_title, self.cd_artist)

    def add_track(self, track: Track) -> None:
        """Adds a track to the CD / Album


        Args:
            track (Track): Track object to be added to CD / Album.

        Returns:
            None.

        """
        # TO-DO append track
        if type(track) is Track:
            self.__tracks.append(track)
        # TO-DO sort tracks
        # This can be done only if the appending happens first.
            self.__sort_tracks() ## @ Laura, This was challenging, I tried to add values inside of the parenthesis "value, track, etc."
        else:
            raise Exception('The track information is not in the correct format. \n')
            
        
    def rmv_track(self, track_id: int) -> None:
        """Removes the track identified by track_id from Album


        Args:
            track_id (int): ID of track to be removed.

        Returns:
            None.

        """
        # TO-DO remove track
        # Notes to self. It was useful to see the script lines provided for __sort_tracks below.
        try:
            if track_id<= len(self.__tracks): # is it >= or <=
                #Make sure to find "n", the location of the 
                n=track_id -1 #the location starts in 0, we need to substract 1.
                self.__tracks.pop(n) #this removes the track.
                #like in the add_track option. Sort them afterwards.
        
	# TO-DO sort tracks using the function already provided in the starter (see below).
                self.__sort_tracks()
        except:
            raise Exception('The track identifier was not revomed, it was not within the available list of tracks.\n')
		#continue
       

    def __sort_tracks(self):
        """Sorts the tracks using Track.position. Fills blanks with None"""
        n = len(self.__tracks)
        for track in self.__tracks:
            if (track is not None) and (n < track.position):
                n = track.position
        tmp_tracks = [None] * n
        for track in self.__tracks:
            if track is not None:
                tmp_tracks[track.position - 1] = track
        self.__tracks = tmp_tracks

    def get_tracks(self) -> str:
        """Returns a string list of the tracks saved for the Album

        Raises:
            Exception: If no tracks are saved with album.

        Returns:
            result (string):formatted string of tracks.

        """
        self.__sort_tracks()
        if len(self.__tracks) < 1:
            raise Exception('No tracks saved for this Album')
        result = ''
        for track in self.__tracks:
            if track is None:
                result += 'No Information for this track\n'
            else:
                result += str(track) + '\n'
        return result

    def get_long_record(self) -> str:
        """gets a formatted long record of the Album: Album information plus track details


        Returns:
            result (string): Formatted information about ablum and its tracks.

        """
        result = self.get_record() + '\n'
        result += self.get_tracks() + '\n'
        return result




